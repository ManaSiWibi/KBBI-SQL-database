# Tesaurus Pusat Bahasa

Snapshot tesaurus Bahasa Indonesia yang dipertahankan terpisah dari tabel
sinonim dan antonim kurasi repositori.

## Berkas

- [`tesaurus_pusat_bahasa__JSON.json`](tesaurus_pusat_bahasa__JSON.json) —
  `20.139` entri.

Root key `tesaurus_pusat_bahasa` berisi objek:

| Field | Keterangan |
| --- | --- |
| `word` | Kata kepala |
| `tag` | Kelas kata sumber |
| `sinonim` | Array sinonim |
| `antonim` | Array antonim |

Data sumber memuat sekitar `130.132` relasi sinonim berarah dan `1.947`
relasi antonim berarah. Nilai asli dipertahankan; relasi tidak diasumsikan
simetris dan tidak dicampur dengan data kurasi lain.

## Sumber dan hak penggunaan

- [Repositori sumber](https://github.com/victoriasovereigne/tesaurus)
- [Commit snapshot](https://github.com/victoriasovereigne/tesaurus/tree/9df5ae4f63a18190a9576bca5badbd75351c2f44)
  (`9df5ae4f63a18190a9576bca5badbd75351c2f44`).
- README sumber menyatakan data diambil dari *Tesaurus Bahasa Indonesia*
  karya Departemen Pendidikan Nasional/Pusat Bahasa tahun 2008 dan menautkan
  [salinan PDF sumber](https://theindonesianwriters.files.wordpress.com/2011/04/kamus-tesaurus_bahasa-indonesia.pdf).
- SHA-256 `dict.json` input:
  `071000e8b25b815770758afdc303e4922f5fba20222ba66ef11bf1181620f0fe`.

Repositori sumber tidak menyertakan file lisensi data. Koleksi ini digunakan
untuk referensi nonkomersial dengan atribusi sumber; status redistribusi tetap
harus diperlakukan sebagai hak yang belum diklarifikasi.

