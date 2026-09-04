# MALINDO Morph

Snapshot kamus morfologi bahasa Melayu dan bahasa Indonesia dari rilis 2024.
Dataset ini dipertahankan terpisah dari kamus definisi karena berisi analisis
bentuk kata, bukan definisi atau kelas kata.

## Berkas

- [`malindo_morph__JSON.json`](malindo_morph__JSON.json) — `255.941` baris.

Root key `malindo_morph` berisi objek dengan field:

| Field | Keterangan |
| --- | --- |
| `id` | ID sumber; awalan `cc`, `ec`, atau `ex` menunjukkan status pemeriksaan |
| `root` | Bentuk akar |
| `derived_form` | Bentuk jadian |
| `prefix` | Prefiks atau proklitik |
| `suffix` | Sufiks atau enklitik |
| `confix` | Konfiks |
| `reduplication` | Jenis reduplikasi, atau `0` |
| `source` | Sumber lema/bentuk |
| `stem` | Bentuk dasar |
| `lemma` | Lema |

Status pada `id` mengikuti sumber: `cc` adalah *core, checked*, `ec` adalah
*expanded, checked*, dan `ex` adalah *expanded, not checked*. Sumber `Kamus`
menggabungkan Kamus Dewan edisi keempat dan KBBI edisi kelima; koleksi ini
karena itu mencakup bahasa Melayu dan bahasa Indonesia, bukan KBBI Indonesia
murni. Snapshot sumber memiliki 103 ID yang berulang (104 baris tambahan);
semua baris dipertahankan dan `id` tidak boleh digunakan sebagai kunci unik.

## Sumber dan reproduksibilitas

- [MALINDO_Morph](https://github.com/matbahasa/MALINDO_Morph)
- [README sumber dan format](https://github.com/matbahasa/MALINDO_Morph/blob/master/readme.md)
- [Berkas `malindo_dic_2024.tsv`](https://github.com/matbahasa/MALINDO_Morph/blob/master/malindo_dic_2024.tsv)
- Commit snapshot: `e3ab07c435343d39d6ab3cb87cd9ba57c27f49d3`
- SHA-256 input TSV: `3c3379e889d3cc74446de709935fca5e0de80154f1a5e8e5b37d9b47180e4c73`
- [Makalah MALINDO Morph](http://lrec-conf.org/workshops/lrec2018/W29/pdf/8_W29.pdf)

JSON ini adalah normalisasi satu-satunya berkas rilis 2024; kode analyzer,
pickle, PDF panduan, dan versi lama tidak disalin.

## Lisensi

README sumber menyatakan MALINDO Morph dilisensikan dengan
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
Atribusi sumber dan keterangan perubahan harus dipertahankan saat data ini
digunakan atau didistribusikan.
