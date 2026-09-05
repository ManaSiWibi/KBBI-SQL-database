# Leipzig Indonesian Wikipedia 2021

Snapshot 100K kalimat dari korpus resmi `ind_wikipedia_2021`, yaitu korpus
Bahasa Indonesia yang bersumber khusus dari Wikipedia dan menggunakan materi
tahun 2021. Dataset ini disimpan terpisah dari `ind_mixed_2013` karena genre
sumbernya berbeda.

## Berkas

- [`leipzig_metadata__JSON.json`](leipzig_metadata__JSON.json): identitas
  corpus, statistik corpus penuh, hash arsip, dan catatan provenance.
- [`leipzig_words__JSON.json`](leipzig_words__JSON.json): `151.524` tipe kata.
- [`leipzig_sentences__JSON.json`](leipzig_sentences__JSON.json): `100.000`
  kalimat.
- [`leipzig_word_sentence_index__JSON.json`](leipzig_word_sentence_index__JSON.json):
  indeks kata ke kalimat.
- [`leipzig_neighbour_cooccurrences__JSON.json`](leipzig_neighbour_cooccurrences__JSON.json):
  `64.537` pasangan kata bertetangga.
- [`leipzig_sentence_cooccurrences__JSON.json`](leipzig_sentence_cooccurrences__JSON.json):
  `322.026` pasangan kata dalam kalimat yang sama.

Struktur JSON dan field relasi sama dengan dataset Leipzig 2013 agar pemakai
dapat mengganti direktori corpus tanpa mengubah parser. `sources`, `inv_so`,
SQL import, dan posisi kata tidak disalin ke format kanonis.

## Mengapa genre berbeda?

`ind_mixed_2013` adalah corpus campuran: sumbernya menggabungkan beberapa jenis
materi sehingga frekuensi kata mencerminkan campuran berita, web, dan sumber
lain yang tersedia pada snapshot tersebut. `ind_wikipedia_2021` hanya memakai
dump Wikipedia. Wikipedia cenderung ensiklopedis, diedit komunitas, dan lebih
seragam secara gaya; corpus campuran memiliki variasi register dan topik yang
lebih luas.

Karena genre memengaruhi kosakata, frekuensi, dan cooccurrence, corpus 2021
lebih baru tetapi bukan pengganti statistik langsung untuk corpus campuran 2013.
Gunakan 2021 untuk konteks ensiklopedis yang lebih mutakhir dan 2013 untuk
cakupan sumber yang lebih beragam.

## Reproduksi fitur Tutur

Gunakan script yang sama dengan memilih direktori dataset:

```sh
python3 scripts/build_leipzig_similarity.py \
  --dataset-dir leipzig-wikipedia-2021 \
  --word bahasa --top-k 20 --output /tmp/bahasa-wikipedia-2021-similarity.json
```

Hasil similarity adalah derivasi lokal cosine dari profil biner `co_n` dan
`co_s`, bukan tabel portal `sim_w_co` yang disalin.

## Sumber dan provenance

- [Halaman resmi Indonesian Wikipedia 2021](https://dict.wortschatz-leipzig.de/en?corpusId=ind_wikipedia_2021)
- [Arsip resmi 100K](https://downloads.wortschatz-leipzig.de/corpora/ind_wikipedia_2021_100K.tar.gz)
- [Katalog unduhan Indonesia](https://wortschatz-leipzig.de/en/download/ind#ind_wikipedia_2021)
- [Spesifikasi format](https://wortschatz.informatik.uni-leipzig.de/documents/Format_Download_File-eng.pdf)
- [FAQ data Leipzig](https://wortschatz-leipzig.de/en/faq-data)
- [Ketentuan penggunaan](https://wortschatz-leipzig.de/en/usage)

Statistik corpus penuh menurut halaman resmi: `2.225.906` kalimat,
`35.769.652` token, dan `1.007.466` tipe kata. Arsip yang diimpor berukuran
`20.518.968` byte dengan SHA-256:

`5a90a9d92c1058aafca1bfaeb20d3c6ed898442b230ee88d435bc585912335da`

Dokumentasi Leipzig menyatakan data unduhan tersedia dengan atribusi CC BY;
ketentuan sumber asal tetap berlaku untuk materi Wikipedia.
