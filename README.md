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
- **KBBI Edisi VI (snapshot):** `194.692` entri terstruktur
- **Kata Baku & Nonbaku:** `2.847` pasangan kata
- **Sinonim (Padanan Kata):** `4.625` entri data
- **Antonim (Lawan Kata):** `550` entri data
- **Kamus Alay:** `4.459` pemetaan slang ke bentuk normal
- **IndoLeX:** `131.534` bentuk kata dan `26.956` akar kata berfrekuensi
- **Enrichment KBBI Edisi IV dari IndoLeX:** `38.364` kata yang dapat dijoin

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

---

> [!WARNING]
>
> ### Hak Cipta dan Kepemilikan Data (Copyright and Data Ownership)
>
> Seluruh data di dalam kamus ini dimiliki sepenuhnya oleh **Badan Pengembangan dan Pembinaan Bahasa, Kementerian Pendidikan Dasar dan Menengah Republik Indonesia**.
>
> Penggunaan dataset ini untuk kebutuhan komersial sangat dilarang dan tunduk pada ketentuan hukum pidana berdasarkan **Undang-Undang Republik Indonesia Nomor 28 Tahun 2014 tentang Hak Cipta**.

Kamus Alay mencantumkan lisensi sumber sebagai tidak diketahui. IndoLeX
mencantumkan lisensi **CC BY-NC-SA 4.0**. Kolom definisi KBBI dari IndoLeX tidak
disertakan dalam salinan ini; gunakan [ketentuan lisensi IndoLeX](https://creativecommons.org/licenses/by-nc-sa/4.0/)
dan atribusi sumber sebelum mendistribusikan ulang.

Snapshot KBBI Edisi VI juga tidak memiliki lisensi data terbuka dari sumbernya.
README sumber menyatakan kepemilikan data berada pada Badan Pengembangan dan
Pembinaan Bahasa; penggunaan kembali harus memperoleh izin yang sesuai.

---

<p align="center">
  Dikelola oleh <strong><a href="https://kang-cahya.com">Kang Cahya</a></strong>
</p>
