# WordNet Bahasa

Snapshot WordNet Bahasa yang difilter ke lemma Bahasa Indonesia dengan kualitas
`Y` (hand-checked) atau `O` (automatic high quality). Data dipisahkan dari
sinonim/antonim karena satu lemma dapat berada di beberapa synset dan file
sumber tidak memberi graf antonim langsung.

## Berkas

- [`wordnet_indonesian__JSON.json`](wordnet_indonesian__JSON.json) — `13.933`
  keanggotaan lemma-synset.
- [`wordnet_indonesian_definitions__JSON.json`](wordnet_indonesian_definitions__JSON.json)
  — `13.099` definisi synset berbahasa Indonesia.
- [`wordnet_indonesian_enrichment__JSON.json`](wordnet_indonesian_enrichment__JSON.json)
  — `13.933` baris join-ready, satu baris untuk setiap keanggotaan lemma-synset.

Root key pertama berisi `synset`, `lang`, `goodness`, dan `lemma`. Root key
kedua berisi `synset` dan `definition`. Root key ketiga berisi field membership
yang sama, `definitions` sebagai array (bisa kosong), dan `has_definition`.
Satu synset dapat memiliki banyak lemma; jangan menganggap setiap baris sebagai
pasangan sinonim tanpa menjaga batas synset.

Keanggotaan mencakup `10.311` synset unik. Definisi mencakup `13.093` synset,
dengan irisan `1.820` synset; `8.491` synset membership tidak memiliki definisi
di file definisi sumber. Enam synset memiliki lebih dari satu baris definisi.
Enrichment sengaja mempertahankan baris tanpa definisi agar join tidak kehilangan
lemma.

## Sumber dan reproduksibilitas

- [Halaman WordNet Bahasa](https://wn-msa.sourceforge.net/eng/index.html)
- [README format data](https://sourceforge.net/p/wn-msa/tab/HEAD/tree/trunk/Readme)
- [Lisensi MIT](https://sourceforge.net/p/wn-msa/tab/HEAD/tree/trunk/LICENSE)
- File sumber bertanggal `2019-05-05` pada release `r24`.
- SHA-256 `wn-msa-all.tab` input:
  `f66698eb836bd3289db2271eb6499587d52f9066f1e7d47d2b653e5f64e0894b`.
- SHA-256 `wn-ind-def.tab` input:
  `5b34e879b2908e730721d9a31563c28aea70e7ba5c6dd42c6a003356b822e9e0`.

README sumber menyatakan data dirilis di bawah MIT. Salinan dan distribusi
harus mempertahankan notice berikut: Francis Bond, David Moeljadi, Hannah
Choi, Muhammad Zulhelmy Mohamed Rosman, Nurril Hirfana Mohamed Noor, Suerya
Sapuan, Hammam Riza, dan Tan Enya Kong.
