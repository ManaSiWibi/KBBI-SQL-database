# Indonesian Wikipedia 2026 (derived 100K)

Snapshot `100.000` kalimat yang diturunkan dari dump Indonesian Wikipedia
bertanggal `2026-09-01`. Ini **bukan** korpus resmi Leipzig; enam berkasnya
hanya memakai bentuk relasi yang kompatibel dengan dataset Leipzig agar fitur
konteks di Tutur dapat memakai parser yang sama.

## Berkas

- [`leipzig_metadata__JSON.json`](leipzig_metadata__JSON.json): sumber, hash,
  metode sampling, normalisasi, dan statistik hasil.
- [`leipzig_words__JSON.json`](leipzig_words__JSON.json): `106.005` tipe token.
- [`leipzig_sentences__JSON.json`](leipzig_sentences__JSON.json): `100.000`
  kalimat.
- [`leipzig_word_sentence_index__JSON.json`](leipzig_word_sentence_index__JSON.json):
  indeks `106.005` token ke kalimat.
- [`leipzig_neighbour_cooccurrences__JSON.json`](leipzig_neighbour_cooccurrences__JSON.json):
  `105.563` bigram tetangga berarah setelah filter frekuensi minimum `3`.
- [`leipzig_sentence_cooccurrences__JSON.json`](leipzig_sentence_cooccurrences__JSON.json):
  `402.198` pasangan dalam kalimat setelah filter frekuensi minimum `6`.

Grafik relasi mentah berisi `848.391` bigram tetangga dan `8.182.525`
pasangan satu-kalimat. Pasangan langka tidak disimpan untuk menjaga ukuran
repositori; nilai `significance` untuk dataset turunan ini adalah Dice
coefficient dikali `100`, bukan skor Leipzig resmi.

## Cakupan dan batasan

Sumbernya adalah bagian awal berkas multistream resmi, yaitu rentang byte
`0–16.777.215` (`16 MiB`), bukan seluruh dump `1.245.213.196` byte. Dari
rentang tersebut, builder mempertahankan kalimat artikel namespace utama
pertama yang lolos filter panjang `20–5.000` karakter sampai mencapai `100.000`
kalimat. Sampel ini deterministik tetapi bias terhadap urutan artikel di dump;
angka 2026 menunjukkan tanggal dump, bukan tanggal setiap isi artikel.

Wikitext dibersihkan dengan regex konservatif: template, tabel, referensi,
tautan, HTML, dan markup format dihapus. Token dibuat casefold dengan tokenizer
Unicode sederhana. Pasangan satu-kalimat memakai token unik; ekspansi dibatasi
`100` token unik per kalimat untuk mencegah ledakan `O(n²)`.

Untuk membuat keluaran ulang:

```sh
curl -fL -A 'KBBI-SQL-database research/1.0' -r 0-16777215 \
  -o /tmp/idwiki-20260901-prefix-16MiB.bz2 \
  'https://dumps.wikimedia.org/idwiki/20260901/idwiki-20260901-pages-articles1.xml-p1p1500000.bz2'
python3 scripts/build_wikipedia_derived.py \
  --input /tmp/idwiki-20260901-prefix-16MiB.bz2 \
  --output leipzig-wikipedia-2026 \
  --sample-sentences 100000 \
  --minimum-neighbour-frequency 3 \
  --minimum-sentence-frequency 6 \
  --corpus-id idwiki-20260901-prefix-16MiB-100K \
  --dump-id idwiki-20260901 \
  --source-url https://dumps.wikimedia.org/idwiki/20260901/idwiki-20260901-pages-articles.xml.bz2 \
  --source-stream-url https://dumps.wikimedia.org/idwiki/20260901/idwiki-20260901-pages-articles1.xml-p1p1500000.bz2 \
  --source-sha1 f76d6700ddcb6aedca033b5a052647a21e6246e0 \
  --source-bytes 1245213196 \
  --source-part-sha1 4dfa0f4dda40be12aaa9930846fbcec78d3e2246 \
  --source-part-bytes 435610924
```

The exact prefix in this repository has SHA-256
`2cdaa80292d2e3b167ebdf0cb28d2e4bb2e4ff7354676bd087f0563b92e6c3d0`.

Similarity queries use the shared derivation script:

```sh
python3 scripts/build_leipzig_similarity.py \
  --dataset-dir leipzig-wikipedia-2026 \
  --word bahasa --top-k 20 --output /tmp/bahasa-wikipedia-2026-similarity.json
```

## Sumber dan lisensi

- [Wikimedia Indonesian Wikipedia dump 2026-09-01](https://dumps.wikimedia.org/idwiki/20260901/)
- [Berkas dump penuh](https://dumps.wikimedia.org/idwiki/20260901/idwiki-20260901-pages-articles.xml.bz2)
- [Berkas multistream yang dipakai](https://dumps.wikimedia.org/idwiki/20260901/idwiki-20260901-pages-articles1.xml-p1p1500000.bz2)
- [Wikimedia Terms of Use](https://meta.wikimedia.org/wiki/Terms_of_use/en)

Konten Wikimedia/Wikipedia tunduk pada ketentuan CC BY-SA, GFDL, dan kemungkinan
pengecualian pihak ketiga. Periksa ketentuan penggunaan, pertahankan atribusi,
dan tinjau kewajiban share-alike sebelum mendistribusikan hasil turunan.
