# KBBI Edisi IV (Kamus Utama)

Direktori ini menyimpan data utama Kamus Besar Bahasa Indonesia (KBBI) Edisi IV
yang memuat total `115.978` kosakata.

## Format Data

- [JSON](dictionary__JSON.json) — format kanonis repositori.

---

## Struktur JSON

Root key `dictionary` berisi array objek dengan rincian field sebagai berikut:

| Nama Field         | Tipe Data      | Kunci (Key) | Nullable | Keterangan                                           |
| :----------------- | :------------- | :---------- | :------- | :--------------------------------------------------- |
| `_id`              | INTEGER        | PRIMARY KEY | NO       | Identifikasi unik entri data (Auto Increment)        |
| `word`             | TEXT / VARCHAR | -           | NO       | Kata atau kosakata                                   |
| `arti`             | TEXT           | -           | YES      | Penjelasan, arti kata, atau definisi                 |
| `type`             | INTEGER        | -           | YES      | Kategori format data (1: HTML markup, 2: Plain Text) |

---
