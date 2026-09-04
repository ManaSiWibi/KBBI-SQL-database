# Antonim Tesaurus Bahasa Indonesia

Daftar pasangan antonim hasil pemrosesan teks Tesaurus Bahasa Indonesia.
Dataset ini dipisahkan dari tabel antonim kurasi repositori karena metode
sumber menghasilkan pasangan berarah dan dapat mengandung noise.

## Berkas

- [`antonim_tesaurus__JSON.json`](antonim_tesaurus__JSON.json) — `30.171`
  pasangan berarah unik.

Root key `antonim_tesaurus` berisi:

| Field | Keterangan |
| --- | --- |
| `id` | ID lokal setelah deduplikasi |
| `kata_a` | Kata pertama |
| `kata_b` | Kata kedua |

Sumber memiliki `34.138` baris. Salinan ini membuang baris kosong dan
mendeduplikasi pasangan berarah setelah pemisahan whitespace; pasangan terbalik
tetap dipertahankan sebagai data berbeda.

## Sumber dan hak penggunaan

- [Repositori sumber](https://github.com/riochr17/Daftar-Antonim-Tesaurus-Bahasa-Indonesia)
- [Commit snapshot](https://github.com/riochr17/Daftar-Antonim-Tesaurus-Bahasa-Indonesia/tree/8c26d5b9e6651c755a0bc07e962185f71d67d6a6)
  (`8c26d5b9e6651c755a0bc07e962185f71d67d6a6`).
- README sumber mengkreditkan [Tesaurus Bahasa Indonesia](http://www.buku-e.lipi.go.id/utama.cgi?lihatarsip&dend001&1257716945).
- SHA-256 input `hasil-pasangan-antonim-id.txt`:
  `b956285c08e2aaf4d77b4367248f78e513c145a26cfbda4f444516c2f9aefebc`.

README sumber tidak memberikan lisensi terbuka yang jelas. Koleksi ini
dipertahankan untuk penggunaan nonkomersial/referensi dengan atribusi sumber.

