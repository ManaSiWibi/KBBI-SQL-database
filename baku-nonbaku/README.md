# Baku Non-Baku

Data ini berisi informasi tentang pasangan kata baku dan kata non-baku beserta penjelasannya.

## Format Data

- [JSON](dictionary_baku_nonbaku__JSON.json) — format kanonis repositori.

## Struktur JSON

| Nama Field | Tipe Data | Nullable | Keterangan           |
| ---------- | --------- | -------- | -------------------- |
| id         | INT       | YES      | Primary Key          |
| word       | TEXT      | NO       | Kata baku            |
| wrong      | TEXT      | NO       | Kata non-baku        |
| explain    | TEXT      | NO       | Penjelasan atau arti |
| clue       | TEXT      | YES      | Petunjuk             |

## Contoh Data

| id  | word (baku) | wrong (non baku) | explain (keterangan)                                                                        | clue (petunjuk)                                            |
| --- | ----------- | ---------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 1   | Apotek      | Apotik           | Kata yang baku menurut KBBI adalah APOTEK, sedangkan APOTIK merupakan bentuk tidak bakunya. | **_ /apoték/ n toko tempat meramu dan menjual obat ... _** |

## Sumber dan provenance

Dataset ini dibuat menggunakan model kecerdasan buatan GPT-5.6 Sol, sebagaimana
dicatat di [README repositori](../README.md) dan disimpan di
[`ManaSiWibi/KBBI-SQL-database`](https://github.com/ManaSiWibi/KBBI-SQL-database).
Prompt asli, tanggal pembuatan,
dan catatan review manusia tidak tersimpan; perlakukan data ini sebagai data
generatif nonotoritatif dan verifikasi terhadap Badan Bahasa sebelum digunakan.
