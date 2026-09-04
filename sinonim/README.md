# Sinonim

Data ini berisi informasi tentang padanan kata (sinonim) dalam Bahasa Indonesia. Saat ini tersedia kurang lebih `4.625` data sinonim.

## Format Data

- [JSON](dictionary_sinonim__JSON.json) — format kanonis repositori.

## Struktur JSON

| Nama Field   | Tipe Data | Nullable | Keterangan                                                          |
| ------------ | --------- | -------- | ------------------------------------------------------------------- |
| id           | INTEGER   | NO       | Primary Key                                                         |
| kata_a       | TEXT      | NO       | Kata pertama                                                        |
| kata_b       | TEXT      | NO       | Kata kedua (padanan)                                                |
| jenis        | TEXT      | NO       | Jenis hubungan (misal: sinonim_satu_synset, varian_baku_tidak_baku) |
| penjelasan   | TEXT      | NO       | Penjelasan hubungan kata                                            |
| penggunaan_a | TEXT      | NO       | Contoh penggunaan kata_a                                            |
| penggunaan_b | TEXT      | NO       | Contoh penggunaan kata_b                                            |

## Contoh Data

| id  | kata_a | kata_b | jenis               | penjelasan                                                                            |
| --- | ------ | ------ | ------------------- | ------------------------------------------------------------------------------------- |
| 1   | aba    | ayah   | sinonim_satu_synset | 'aba' dan 'ayah' tervalidasi sebagai sinonim pada sekurang-kurangnya satu makna...    |
| 2   | abadi  | kekal  | sinonim_satu_synset | 'abadi' dan 'kekal' tervalidasi sebagai sinonim pada sekurang-kurangnya satu makna... |

## Sumber dan provenance

Dataset ini dibuat menggunakan model kecerdasan buatan GPT-5.6 Sol, sebagaimana
dicatat di [README repositori](../README.md) dan disimpan di
[`ManaSiWibi/KBBI-SQL-database`](https://github.com/ManaSiWibi/KBBI-SQL-database).
Prompt asli, tanggal pembuatan,
dan catatan review manusia tidak tersimpan; perlakukan data ini sebagai data
generatif nonotoritatif dan verifikasi terhadap sumber kamus sebelum digunakan.
