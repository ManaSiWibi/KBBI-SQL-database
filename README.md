<img width="256" height="256" alt="image" src="https://github.com/user-attachments/assets/049f6ac3-da3f-4c01-bc5d-99daa197fc85" />

# KBBI SQL Database

Kamus Besar Bahasa Indonesia (KBBI) SQL Database, total data `115.978` kata, `2.847` data kata baku-nonbaku, dan `4.625` data sinonim.

## Kamus

Informasi lengkap mengenai database Kamus Besar Bahasa Indonesia.

### Format data

Tersedia untuk format data:

- [MySQL](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__MySQL.sql)
- [SQLite](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__SQLite.sql)
- [PostgreSQL](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__PostgreSQL.sql)

Juga tersedia untuk format data lainnya seperti CSV, JSON, Markdown, PHP Array, XML, DbUnit, dan HTML.

### Struktur Tabel

Secara umum, tabel `dictionary` memiliki struktur sebagai berikut:

| Nama Field | Tipe Data | Keterangan                                  |
| ---------- | --------- | ------------------------------------------- |
| \_id       | INTEGER   | Primary Key, Auto Increment                 |
| word       | TEXT      | Kata                                        |
| arti       | TEXT      | Arti atau penjelasan                        |
| type       | INTEGER   | Tipe atau kategori (1: HTML, 2: Plain Text) |

Detail mengenai pembuatan tabel untuk masing-masing database dapat dilihat pada file SQL terkait.

---

## Baku Non-Baku

Data ini berisi informasi tentang pasangan kata baku dan kata non-baku. Terdapat kurang lebih `2847` pasangan kata.

Detail informasi dan format data dapat dilihat di: [README Baku Non-Baku](baku-nonbaku/README.md)

---

## Sinonim

Data ini berisi informasi tentang padanan kata (sinonim) dalam Bahasa Indonesia. Terdapat kurang lebih `4.625` data sinonim.

Detail informasi dan format data dapat dilihat di: [README Sinonim](sinonim/README.md)

---

## API KBBI

Jika data pada database kurang lengkap, Anda dapat mengkombinasikannya dengan [API KBBI PHP Codeigniter4](https://github.com/dyazincahya/API-KBBI-PHP-Codeigniter-4) yang sumber datanya langsung berasal dari [KBBI Daring Kemdikbud](https://kbbi.kemdikbud.go.id/)

## Contoh Aplikasi KBBI

MyKBBI: [https://play.google.com/store/apps/details?id=com.kang.cahya.apps.mykbbi](https://play.google.com/store/apps/details?id=com.kang.cahya.apps.mykbbi)

## Kredit

- [Ican Bachors](https://github.com/bachors/KBBI.sql)
- [Flaticon](https://www.flaticon.com/free-icon/dictionary_7214200?related_id=7214200)

## Penulis

[Kang Cahya](https://kang-cahya.com)
