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
