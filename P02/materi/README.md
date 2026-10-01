# pbo-sipala-CONTOH — Pertemuan 2

Kode acuan Pertemuan 2 — Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai

## Isi

| Berkas | Keterangan |
|---|---|
| `src/model/penyewa.py` | Kelas `Penyewa` — empat atribut, dua method, satu parameter berdefault. |
| `src/model/alat_tani.py` | Kelas `AlatTani` — tiga atribut, dua method, format rupiah bergaya Indonesia. |
| `src/main.py` | Titik masuk; satu-satunya berkas yang mencetak ke layar. |
| `tests/test_penyewa.py` | Tiga fungsi uji. |
| `tests/test_alat_tani.py` | Empat fungsi uji, termasuk uji kemandirian objek. |
| `lupa_self.py` | **Sengaja salah.** Kesalahan yang ditanam nomor 1 (Langkah 5). Dihapus setelah Langkah 10. |

## Tiga gerbang

```
python periksa_pbo.py src --profil p02
python -m mypy
python -m pytest
python -m src.main
```

Keluaran yang diharapkan:

```
LOLOS. Tidak ada pelanggaran disiplin berorientasi objek.
Success: no issues found in 8 source files
7 passed

Budi Santoso (1406012509900001) — Desa Kuok
Budi Santoso dapat dihubungi di 0812-3456-7890
Siti Aminah belum mencantumkan nomor telepon
[TR-01] Traktor Roda Dua Kubota — Rp150.000/hari
Sewa traktor 3 hari: Rp450.000
Sewa pompa 5 hari  : Rp375.000
```

## Dua kesalahan yang sengaja ditanam

**① Melupakan `self`** — jalankan `python lupa_self.py`:

```
TypeError: AlatTani.biaya_sewa() takes 1 positional argument but 2 were given
```

**② Mengubah atribut dari luar** — Python mengizinkannya tanpa keluhan:

```
python -c "
from src.model.alat_tani import AlatTani
alat = AlatTani('TR-01', 'Traktor', 150000)
alat._tarif_harian = -5000
print(alat.keterangan())      # Rp-5.000/hari
print(alat.biaya_sewa(3))     # -15000
"
```

Kesalahan kedua inilah yang menjadi alasan keberadaan Pertemuan 3.

## Catatan versi

`pyproject.toml` memakai `python_version = "3.14"`. Sesuaikan pada berkas milik
dosen bila laboratorium memakai versi lain — bukan pada berkas milik mahasiswa.
