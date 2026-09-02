import { createWriteStream } from "node:fs";
import { readFile, mkdir, rm, writeFile } from "node:fs/promises";
import { once } from "node:events";
import { fileURLToPath } from "node:url";

const sourceFiles = {
  dictionary: new URL("../../edisi-IV/dictionary__JSON.json", import.meta.url),
  bakuNonbaku: new URL(
    "../../baku-nonbaku/dictionary_baku_nonbaku__JSON.json",
    import.meta.url,
  ),
  sinonim: new URL(
    "../../sinonim/dictionary_sinonim__JSON.json",
    import.meta.url,
  ),
  antonim: new URL(
    "../../antonim/dictionary_antonim__JSON.json",
    import.meta.url,
  ),
};

const outputDirectory = fileURLToPath(
  new URL("../public/data/", import.meta.url),
);
const dictionaryDirectory = fileURLToPath(
  new URL("../public/data/dictionary/", import.meta.url),
);

async function readCollection(url, rootKey) {
  const sourcePath = fileURLToPath(url);
  const parsed = JSON.parse(await readFile(sourcePath, "utf8"));
  const collection = parsed[rootKey];

  if (!Array.isArray(collection)) {
    throw new TypeError(`Expected an array at "${rootKey}" in ${sourcePath}`);
  }

  return collection;
}

function normalizeWord(record, collectionName) {
  if (typeof record?.word !== "string") {
    throw new TypeError(`Invalid word in ${collectionName}`);
  }

  return { ...record, word: record.word.trim() };
}

function getLetter(word) {
  const firstCharacter = Array.from(word.toLowerCase())[0];

  if (firstCharacter && /^[a-z]$/.test(firstCharacter)) {
    return firstCharacter;
  }

  if (firstCharacter && /^[0-9]$/.test(firstCharacter)) {
    return "0-9";
  }

  return "other";
}

async function writeJson(path, value) {
  await writeFile(path, JSON.stringify(value), "utf8");
}

async function writeJsonArray(path, records) {
  const stream = createWriteStream(path, { encoding: "utf8" });
  stream.write("[");

  for (let index = 0; index < records.length; index += 1) {
    const chunk = `${index === 0 ? "" : ","}${JSON.stringify(records[index])}`;
    if (!stream.write(chunk)) {
      await once(stream, "drain");
    }
  }

  stream.end("]");
  await once(stream, "finish");
}

async function main() {
  const [rawDictionary, bakuNonbaku, sinonim, antonim] = await Promise.all([
    readCollection(sourceFiles.dictionary, "dictionary"),
    readCollection(sourceFiles.bakuNonbaku, "quiz_baku"),
    readCollection(sourceFiles.sinonim, "dictionary_sinonim"),
    readCollection(sourceFiles.antonim, "dictionary_antonim"),
  ]);

  const dictionary = rawDictionary.map((record) =>
    normalizeWord(record, "dictionary"),
  );
  const dictionaryIndex = [];
  const shards = new Map();

  for (const record of dictionary) {
    const letter = getLetter(record.word);
    dictionaryIndex.push({ id: record._id, word: record.word, letter });

    const shard = shards.get(letter) ?? [];
    shard.push(record);
    shards.set(letter, shard);
  }

  await rm(outputDirectory, { recursive: true, force: true });
  await mkdir(dictionaryDirectory, { recursive: true });

  const shardWrites = [...shards.entries()]
    .sort(([left], [right]) => left.localeCompare(right))
    .map(([letter, records]) =>
      writeJsonArray(`${dictionaryDirectory}/${letter}.json`, records),
    );

  const manifest = {
    generatedAt: new Date().toISOString(),
    count: {
      dictionary: dictionary.length,
      bakuNonbaku: bakuNonbaku.length,
      sinonim: sinonim.length,
      antonim: antonim.length,
    },
  };

  await Promise.all([
    writeJson(`${outputDirectory}/manifest.json`, manifest),
    writeJsonArray(`${outputDirectory}/dictionary-index.json`, dictionaryIndex),
    writeJson(`${outputDirectory}/baku-nonbaku.json`, bakuNonbaku),
    writeJson(`${outputDirectory}/sinonim.json`, sinonim),
    writeJson(`${outputDirectory}/antonim.json`, antonim),
    ...shardWrites,
  ]);

  console.log(
    `Prepared ${dictionary.length} dictionary entries in ${shards.size} shards.`,
  );
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
