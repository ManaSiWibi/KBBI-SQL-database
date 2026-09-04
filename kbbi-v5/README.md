# KBBI Edisi V (snapshot Lyon28)

Snapshot CSV KBBI V dari dataset Hugging Face `Lyon28`, dikonversi ke JSON
kanonis. Setiap objek merepresentasikan satu baris makna atau data pendukung;
dataset ini dipertahankan terpisah dari snapshot KBBI Edisi VI.

## Berkas

- [`kbbi_v5__JSON.json`](kbbi_v5__JSON.json) — `146.280` objek.

Root key `kbbi_v5` berisi objek dengan field sumber:
`key`, `nama`, `nomor`, `kata_dasar`, `pelafalan`, `bentuk_tidak_baku`,
`varian`, `kelas`, `submakna`, `info`, `contoh`, `etimologi`, `kata_turunan`,
`gabungan_kata`, `peribahasa`, dan `idiom`.

Sel kosong dikonversi menjadi `null`; `nomor` dipertahankan sebagai bilangan
bulat jika tersedia. Isi teks tidak ditulis ulang.

## Sumber dan reproduksibilitas

- [Dataset Hugging Face](https://huggingface.co/datasets/Lyon28/kamus-besar-bahasa-indonesia)
- [Data CSV snapshot](https://huggingface.co/datasets/Lyon28/kamus-besar-bahasa-indonesia/resolve/main/data.csv)
- Revision dataset: `e1e51706b8252ac1be588ba1eae8585b844f1ba9`
- Pembaruan terakhir revision tersebut: `2025-08-12T12:54:14Z`
- SHA-256 CSV input:
  `63de17a42cf1bd0b4f7ca73d954a4928c07598d26f042b0104ffee90ee0ef056`.
- [README historis uploader pada revision upload](https://huggingface.co/datasets/Lyon28/kamus-besar-bahasa-indonesia/blob/a230fbfe20ad202b11622e7b3f6d84c37d77d5/README.md)
  menyatakan data ini adalah KBBI V yang diekstrak dari situs KBBI dengan
  rujukan [damzaky/kumpulan-kata-bahasa-indonesia-KBBI](https://github.com/damzaky/kumpulan-kata-bahasa-indonesia-KBBI).

## Hak penggunaan

Dataset card saat ini menampilkan `Apache-2.0`, tetapi README historis pada
revision upload menyatakan data dimiliki Badan Pengembangan dan Pembinaan
Bahasa serta melarang penggunaan komersial. Kedua pernyataan ini dicatat agar
metadata lisensi tidak dianggap sebagai izin Apache yang berdiri sendiri.
Salinan ini ditambahkan untuk penggunaan nonkomersial/referensi sesuai ruang
lingkup proyek; atribusi Badan Bahasa dan sumber uploader harus dipertahankan.
