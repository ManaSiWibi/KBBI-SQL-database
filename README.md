<h1 align="center">KBBI SQL Database</h1>

<p align="center">
  Basadata (Database) Kamus Besar Bahasa Indonesia (KBBI) yang menyediakan ribuan entri kata lengkap dengan data pendukung seperti sinonim, antonim, kata baku/nonbaku, normalisasi bahasa alay, serta frekuensi dan akar kata untuk kebutuhan pengembangan aplikasi.
</p>

<p align="center">
  <a href="#format-standar">Format Standar</a> •
  <a href="#ikhtisar-direktori-data">Ikhtisar Data</a> •
  <a href="#integrasi-api">Integrasi API</a> •
  <a href="#contoh-aplikasi">Contoh Aplikasi</a>
</p>

---

## Format Standar

JSON adalah satu-satunya format data kanonis di repositori ini. Setiap direktori
dataset menyimpan berkas JSON dan README yang menjelaskan struktur serta sumber
datanya.

## Ringkasan Data

Repositori ini menyimpan total data bahasa Indonesia dengan rincian sebagai berikut:

- **Kamus Utama (Edisi IV):** `115.978` kata
- **KBBI Edisi V (snapshot):** `146.280` objek terstruktur
- **KBBI Edisi VI (snapshot):** `194.692` entri terstruktur
- **Kata Baku & Nonbaku:** `2.847` pasangan kata
- **Sinonim (Padanan Kata):** `4.625` entri data
- **Antonim (Lawan Kata):** `550` entri data
- **Kamus Alay:** `4.459` pemetaan slang ke bentuk normal
- **IndoLeX:** `131.534` bentuk kata dan `26.956` akar kata berfrekuensi
- **Enrichment KBBI Edisi IV dari IndoLeX:** `38.364` kata yang dapat dijoin
- **Kaikki Bahasa Indonesia:** `47.945` objek dari `47.403` kata
- **Kaikki Bahasa Indonesia Peranakan:** `1.667` objek/kata
- **Tesaurus Pusat Bahasa:** `20.139` entri
- **Antonim Tesaurus:** `30.171` pasangan berarah unik
- **WordNet Bahasa Indonesia:** `13.933` keanggotaan synset dan `13.099` definisi
- **MALINDO Morph:** `255.941` baris analisis morfologi Melayu/Indonesia
- **Leipzig Indonesian 2013 (100K):** `133.046` tipe kata, `100.000` kalimat,
  `71.456` relasi tetangga, dan `378.892` relasi satu kalimat

---

## Ikhtisar Direktori Data

Seluruh data dikelompokkan ke dalam direktori terstruktur berdasarkan fungsinya masing-masing:

### [1. KBBI Edisi IV (Kamus)](edisi-IV/README.md)

Berisi pangkalan data utama Kamus Besar Bahasa Indonesia Edisi IV dalam format JSON kanonis.

### [2. Baku & Nonbaku](baku-nonbaku/README.md)

Menyediakan daftar perbandingan kata baku dan tidak baku untuk validasi ejaan berdasarkan standar KBBI.

### [3. Sinonim (Padanan Kata)](sinonim/README.md)

Berisi kumpulan relasi sinonim antarkata dalam bahasa Indonesia.

### [4. Antonim (Lawan Kata)](antonim/README.md)

Berisi hubungan oposisi makna atau lawan kata dalam bahasa Indonesia.

### [5. Kamus Alay](kamus-alay/README.md)

Berisi pemetaan kata slang bahasa Indonesia ke bentuk normal beserta kategori
perubahannya. Konteks komentar sumber tidak disertakan.

### [6. IndoLeX](indolex/README.md)

Berisi frekuensi bentuk kata, hubungan ke akar kata, frekuensi akar, dan tabel
enrichment yang dapat digabungkan dengan kamus utama.

### [7. KBBI Edisi VI](kbbi-v6/README.md)

Snapshot JSON terstruktur KBBI Edisi VI dengan definisi, contoh, kata turunan,
gabungan kata, peribahasa, pelafalan, dan etimologi. Data disimpan terpisah
dari KBBI Edisi IV karena struktur dan status lisensinya berbeda.

### [8. KBBI Edisi V](kbbi-v5/README.md)

Snapshot KBBI V dari dataset Lyon28, disimpan terpisah karena formatnya
diratakan per baris makna dan memiliki catatan hak penggunaan tersendiri.

### [9. Kaikki / Wiktionary](kaikki/README.md)

Data machine-readable Wiktionary Bahasa Indonesia dan Bahasa Indonesia
Peranakan dengan sense, bentuk kata, kategori, dan contoh.

### [10. Tesaurus Pusat Bahasa](tesaurus-pusat-bahasa/README.md)

Snapshot tesaurus dengan relasi sinonim dan antonim dari sumber Pusat Bahasa.

### [11. Antonim Tesaurus](antonim-tesaurus/README.md)

Pasangan antonim hasil pemrosesan teks tesaurus; dipisahkan dari antonim kurasi.

### [12. WordNet Bahasa](wordnet-bahasa/README.md)

Keanggotaan lemma-synset dan definisi WordNet Bahasa untuk Bahasa Indonesia.

### [13. MALINDO Morph](malindo-morph/README.md)

Kamus morfologi bahasa Melayu/Indonesia dengan akar, bentuk jadian, imbuhan,
reduplikasi, stem, dan lema.

### [14. Leipzig Corpora Collection](leipzig/README.md)

Snapshot korpus penggunaan bahasa Indonesia dengan kalimat, indeks kata-ke-
kalimat, cooccurrence tetangga, dan cooccurrence dalam kalimat untuk
enrichment berbasis konteks.

---

## Integrasi API

Apabila data lokal yang tersedia di repositori ini kurang lengkap, Anda dapat mengintegrasikannya dengan layanan eksternal berikut:

- **[API KBBI PHP CodeIgniter 4](https://github.com/dyazincahya/API-KBBI-PHP-CodeIgniter-4)** — Mengambil data dinamis yang bersumber langsung dari portal resmi [KBBI Daring Kemendikdasmen](https://kbbi.kemendikdasmen.go.id/).

---

## Contoh Aplikasi

Penerapan basis data ini dapat dilihat langsung pada aplikasi Android berikut:

- **MyKBBI:** [Unduh di Google Play Store](https://play.google.com/store/apps/details?id=com.kang.cahya.apps.mykbbi)

---

## Sumber Data

Repositori ini merupakan fork yang dikelola melalui
[ManaSiWibi/KBBI-SQL-database](https://github.com/ManaSiWibi/KBBI-SQL-database)
dari [dyazincahya/KBBI-SQL-database](https://github.com/dyazincahya/KBBI-SQL-database),
proyek yang dibuat dan dikembangkan oleh
[Kang Cahya](https://github.com/dyazincahya). Struktur awal dan sebagian data
repositori berasal dari proyek tersebut; perubahan dan dataset tambahan
dicantumkan pada daftar sumber di bawah.

Repositori ini merupakan kurasi dari berbagai sumber data bahasa Indonesia yang tersedia di internet, khususnya GitHub. Namun sebagian data ada yang dibuat menggunakan AI (Artificial Intelligence).

1. **[Ican Bachors (KBBI.sql)](https://github.com/bachors/KBBI.sql)** — Penyedia data repositori dasar.
2. **[aryakdaniswara (kbbi-v6-full-csv)](https://github.com/aryakdaniswara/kbbi-v6-full-csv)** — Penyedia data repositori dasar.
3. **[aryakdaniswara (kbbi-v6-categories)](https://github.com/aryakdaniswara/kbbi-v6-categories)** — Penyedia data repositori dasar.
4. **[aryakdaniswara (kbbi-v6-wordlist)](https://github.com/aryakdaniswara/kbbi-v6-wordlist)** — Penyedia data repositori dasar.
5. **[aryakdaniswara (kbbi-dataset-kbbi-v)](https://github.com/aryakdaniswara/kbbi-dataset-kbbi-v)** — Penyedia data repositori dasar.
6. **[raf555 (KBBI-api)](https://github.com/raf555/kbbi-api)** — Penyedia data repositori dasar.
7. **Baku & Nonbaku** — Dibuat menggunakan model kecerdasan buatan GPT-5.6 Sol.
8. **Sinonim** — Dibuat menggunakan model kecerdasan buatan GPT-5.6 Sol.
9. **Antonim** — Dibuat menggunakan model kecerdasan buatan GPT-5.6 Sol.
10. **[Kamus Alay](https://github.com/nasalsabila/kamus-alay)** — Salsabila, Ali, Yosef, dan Ade; didistribusikan ulang tanpa konteks komentar.
11. **[IndoLeX](https://www.kaggle.com/datasets/binhashem/indolex-indonesian-academic-lexical-dataset)** — Omar Hashem; data frekuensi dan akar kata dari dataset Kaggle versi 2.
12. **[Definisi/kbbi](https://github.com/Definisi/kbbi)** — snapshot KBBI Edisi VI yang diekstrak dari APK resmi versi 6.0.2.
13. **[Kaikki Bahasa Indonesia](https://kaikki.org/idwiktionary/Bahasa%20Indonesia/index.html)** — ekstraksi Wiktionary melalui Wiktextract.
14. **[Kaikki Bahasa Indonesia Peranakan](https://kaikki.org/idwiktionary/Bahasa%20Indonesia%20Peranakan/index.html)** — ekstraksi Wiktionary melalui Wiktextract.
15. **[Lyon28/kamus-besar-bahasa-indonesia](https://huggingface.co/datasets/Lyon28/kamus-besar-bahasa-indonesia)** — snapshot KBBI V dalam CSV.
16. **[victoriasovereigne/tesaurus](https://github.com/victoriasovereigne/tesaurus)** — dump Tesaurus Bahasa Indonesia/Pusat Bahasa 2008.
17. **[riochr17/Daftar-Antonim-Tesaurus-Bahasa-Indonesia](https://github.com/riochr17/Daftar-Antonim-Tesaurus-Bahasa-Indonesia)** — hasil pemrosesan pasangan antonim dari tesaurus.
18. **[WordNet Bahasa](https://wn-msa.sourceforge.net/eng/index.html)** — data lemma-synset Bahasa Indonesia, lisensi MIT.
19. **[MALINDO Morph](https://github.com/matbahasa/MALINDO_Morph)** — kamus morfologi Melayu/Indonesia, lisensi CC BY 4.0 menurut README sumber.
20. **[Leipzig Corpora Collection](https://corpora.uni-leipzig.de/en?corpusId=ind_mixed_2013)** — snapshot `ind_mixed_2013_100K` dari [arsip unduhan resmi](https://downloads.wortschatz-leipzig.de/corpora/ind_mixed_2013_100K.tar.gz), format dan relasi mengikuti [spesifikasi Leipzig](https://wortschatz.informatik.uni-leipzig.de/documents/Format_Download_File-eng.pdf).

Sumber yang diperiksa tetapi tidak disalin sebagai dataset statis:

- **[ivanlanin/kateglo2](https://github.com/ivanlanin/kateglo2)** — repositori aplikasi; data operasional berada di direktori `.data/` yang diabaikan dan tidak menyediakan dump dataset terversi.
- **[satriaajiputra/synonym-antonym-indonesia](https://github.com/satriaajiputra/synonym-antonym-indonesia)** — paket PHP yang mengambil data dari `sinonimkata.com` saat runtime, bukan snapshot data.

---

> [!WARNING]
>
> ### Hak Cipta dan Kepemilikan Data (Copyright and Data Ownership)
>
> Koleksi yang berasal dari KBBI atau Tesaurus Pusat Bahasa mengikuti catatan kepemilikan **Badan Pengembangan dan Pembinaan Bahasa, Republik Indonesia**. Dataset lain memiliki ketentuan sumber masing-masing; lihat README setiap direktori.
>
> Penggunaan koleksi KBBI dan Tesaurus Pusat Bahasa untuk kebutuhan komersial sangat dilarang dan tunduk pada ketentuan hukum pidana berdasarkan **Undang-Undang Republik Indonesia Nomor 28 Tahun 2014 tentang Hak Cipta**.

Kamus Alay mencantumkan lisensi sumber sebagai tidak diketahui. IndoLeX
mencantumkan lisensi **CC BY-NC-SA 4.0**. Kolom definisi KBBI dari IndoLeX tidak
disertakan dalam salinan ini; gunakan [ketentuan lisensi IndoLeX](https://creativecommons.org/licenses/by-nc-sa/4.0/)
dan atribusi sumber sebelum mendistribusikan ulang.

Snapshot KBBI Edisi VI dan snapshot KBBI V juga tidak memiliki lisensi data
terbuka yang konsisten dari sumbernya.
README sumber menyatakan kepemilikan data berada pada Badan Pengembangan dan
Pembinaan Bahasa; penggunaan kembali harus memperoleh izin yang sesuai.

MALINDO Morph menyatakan lisensi **CC BY 4.0**; gunakan atribusi sumber dan
lihat [README dataset](malindo-morph/README.md) untuk provenance serta cakupan
bahasa Melayu/Indonesia.

Snapshot Leipzig berasal dari korpus unduhan yang dinyatakan tersedia dengan
atribusi **CC BY**; kalimatnya diproses otomatis dari materi Internet. Lihat
[FAQ Leipzig](https://www.wortschatz.uni-leipzig.de/en/documentation/faq),
[ketentuan penggunaan](https://wortschatz-leipzig.de/en/usage), dan
[README dataset](leipzig/README.md) untuk batasan provenance dan redistribusi.
