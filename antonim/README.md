# Antonim

Data ini berisi informasi tentang lawan kata (antonim) dalam Bahasa Indonesia. Saat ini tersedia kurang lebih `550` data antonim.

## Format Data

- [JSON](dictionary_antonim__JSON.json) — format kanonis repositori.

## Struktur JSON

| Nama Field        | Tipe Data | Nullable | Keterangan                                       |
| ----------------- | --------- | -------- | ------------------------------------------------ |
| id                | INTEGER   | NO       | Primary Key                                      |
| kata_a            | TEXT      | NO       | Kata pertama                                     |
| kata_b            | TEXT      | NO       | Kata kedua (lawan kata)                          |
| jenis_oposisi     | TEXT      | NO       | Jenis hubungan (misal: gradabel, komplementer)   |
| bidang            | TEXT      | NO       | Bidang atau konteks penggunaan                   |
| tingkat_keyakinan | TEXT      | NO       | Tingkat keyakinan data (tinggi, menengah, rendah)|
| penjelasan        | TEXT      | NO       | Penjelasan hubungan antonim                      |
| penggunaan_a      | TEXT      | NO       | Contoh penggunaan kata_a                         |
| penggunaan_b      | TEXT      | NO       | Contoh penggunaan kata_b                         |
| catatan           | TEXT      | YES      | Catatan tambahan                                 |

## Contoh Data

| id  | kata_a | kata_b | jenis_oposisi         | penjelasan                                                                        |
| --- | ------ | ------ | --------------------- | --------------------------------------------------------------------------------- |
| 1   | baik   | buruk  | gradabel/kontekstual  | Pasangan 'baik' dan 'buruk' memiliki hubungan pertentangan makna dalam konteks... |
| 2   | besar  | kecil  | gradabel/kontekstual  | Pasangan 'besar' dan 'kecil' memiliki hubungan pertentangan makna dalam konteks...|
