<img width="256" height="256" alt="image" src="https://github.com/user-attachments/assets/049f6ac3-da3f-4c01-bc5d-99daa197fc85" />

# KBBI SQL Database

Kamus Besar Bahasa Indonesia (KBBI) SQL Database, total data `115.978` kata.

## Kamus

### Format data

Tersedia untuk format data:

- [MySQL](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__MySQL.sql)
- [SQLite](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__SQLite.sql)
- [PostgreSQL](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__PostgreSQL.sql)

Juga tersedia untuk format data lainnya seperti:

- [CSV](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__CSV.csv)
- [JSON](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__JSON.json)
- [Markdown](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__MARKDOWN.md)
- [PHP Array](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__PHP_ARRAY.php)
- [XML](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__XML.xml)
- [DbUnit](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__DbUnit.xml)
- [HTML](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/dictionary__HTML.html)

### Database

Buat database baru dengan nama `kbbi`, nama database dapat di sesuaikan dengan keinginan Anda jika mau.

### Tabel

Sebelum mengimpor data kata, buatlah tabelnya terlebih dahulu dengan nama `dictionary`, nama tabel dapat di sesuaikan juga jika mau.

#### SQLite

| Nama Field | Tipe Data | Nullable | Keterangan                  |
| ---------- | --------- | -------- | --------------------------- |
| \_id       | INTEGER   | NO       | Primary Key, Auto Increment |
| word       | TEXT      | NO       | Kata                        |
| arti       | TEXT      | NO       | Arti atau penjelasan        |
| type       | INTEGER   | NO       | Tipe atau kategori          |

```sql
CREATE TABLE "dictionary" (
  _id INTEGER PRIMARY KEY AUTOINCREMENT,
  word TEXT NOT NULL,
  arti TEXT NOT NULL,
  type INTEGER NOT NULL
);
```

#### PostgrSQL

| Nama Field | Tipe Data | Nullable | Keterangan                  |
| ---------- | --------- | -------- | --------------------------- |
| \_id       | serial4   | NO       | Primary Key, Auto Increment |
| word       | text      | NO       | Kata                        |
| arti       | text      | NO       | Arti atau penjelasan        |
| type       | int4      | NO       | Tipe atau kategori          |

```sql
CREATE TABLE public."dictionary" (
	"_id" serial4 NOT NULL,
	word text NOT NULL,
	arti text NOT NULL,
	"type" int4 NOT NULL,
	CONSTRAINT dictionary_pkey PRIMARY KEY (_id)
);
```

#### MySQL

| Nama Field | Tipe Data | Nullable | Keterangan                  |
| ---------- | --------- | -------- | --------------------------- |
| \_id       | INT(11)   | NO       | Primary Key, Auto Increment |
| word       | TEXT      | NO       | Kata                        |
| arti       | TEXT      | NO       | Arti atau penjelasan        |
| type       | INT(11)   | NO       | Tipe atau kategori          |

```sql
CREATE TABLE `dictionary` (
  `_id` int(11) NOT NULL AUTO_INCREMENT,
  `word` text NOT NULL,
  `arti` text NOT NULL,
  `type` int(11) NOT NULL,
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=115989 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
```

### Tipe Format Data

Ada 2 tipe format data, yaitu `1` & `2`, kurang lebih perbedaannya seperti ini:
| \_id | word | arti | type |
|---|---|---|---|
| 1 | A | `<b><sup>1</sup>A, a</b> <i>n</i> <b>1</b> huruf pertama abjad Indonesia; <b>2</b> nama huruf <i>a</i>; <b>3</b> penanda pertama dl urutan (mutu, nilai, dsb)` | `1` |
| 2 | A | Nomina (kata benda)\n(1) huruf pertama abjad Indonesia;\n(2) nama huruf a;\n(3) penanda pertama dalam urutan (mutu, nilai, dan sebagainya) | `2` |

Dapat Anda lihat perbedaannya:

- Tipe `1` menggunakan format HTML
- Tipe `2` tidak menggunakan format HTML

## Baku Non Baku

Ini adalah data yang berbeda diluar data kamus. Pada data ini berisi informasi tentang kata baku dan kata non baku. Kurang lebih perbedaannya seperti ini:

| id  | word (baku) | wrong (non baku) | explain (keterangan)                                                                                                                                                                                                                                                                                                                                                      | clue (petunjuk)                                                                                                                                                                                                                             |
| --- | ----------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Apotek      | Apotik           | Kata yang baku menurut KBBI adalah APOTEK, sedangkan APOTIK merupakan bentuk tidak bakunya.<br><br>Arti _Apotek_: apo·tek /apoték/ n toko tempat meramu dan menjual obat berdasarkan resep dokter serta memperdagangkan barang medis; rumah obat;-- hidup sebagian tanah yg ditanami tanaman obat-obatan untuk keperluan sehari-hari;per·a·po·tek·an n hal atau tt apotek | **_ /apoték/ n toko tempat meramu dan menjual obat berdasarkan resep dokter serta memperdagangkan barang medis; rumah obat;-- hidup sebagian tanah yg ditanami tanaman obatobatan untuk keperluan seharihari;pera·potekan n hal atau tt _** |

Pada data ini tersedia kurang lebih `2847` pasangan kata baku dan non baku. Untuk struktur data pada tabelnya seperti ini:

| Nama Field | Tipe Data | Nullable | Keterangan           |
| ---------- | --------- | -------- | -------------------- |
| id         | INT       | YES      | Primary Key          |
| word       | TEXT      | NO       | Kata baku            |
| wrong      | TEXT      | NO       | Kata non-baku        |
| explain    | TEXT      | NO       | Penjelasan atau arti |
| clue       | TEXT      | YES      | Petunjuk             |

### Format data baku & non-baku

Tersedia untuk format data:

- [MySQL](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__MySQL.sql)
- [SQLite](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__SQLite.sql)
- [PostgreSQL](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__PostgreSQL.sql)

Juga tersedia untuk format data lainnya seperti:

- [CSV](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__CSV.csv)
- [JSON](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__JSON.json)
- [Markdown](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__MARKDOWN.md)
- [PHP Array](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__PHP_ARRAY.php)
- [XML](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__XML.xml)
- [DbUnit](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__DbUnit.xml)
- [HTML](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__HTML.html)
- [TEXT](https://github.com/dyazincahya/KBBI-SQL-database/blob/main/baku-nonbaku/dictionary_baku_nonbaku__TEXT.txt)


## API KBBI

Jika data pada database kurang lengkap, Anda dapat mengkombinasikannya dengan [API KBBI PHP Codeigniter4](https://github.com/dyazincahya/API-KBBI-PHP-Codeigniter-4) yang sumber datanya langsung berasal dari [KBBI Daring Kemdikbud](https://kbbi.kemdikbud.go.id/)

## Contoh Aplikasi KBBI

MyKBBI: [https://play.google.com/store/apps/details?id=com.kang.cahya.apps.mykbbi](https://play.google.com/store/apps/details?id=com.kang.cahya.apps.mykbbi)

## Kredit

- [Ican Bachors](https://github.com/bachors/KBBI.sql)
- [Flaticon](https://www.flaticon.com/free-icon/dictionary_7214200?related_id=7214200)

## Penulis

[Kang Cahya](https://kang-cahya.com)
