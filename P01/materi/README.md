# pbo-sipala-CONTOH

Kode acuan Pertemuan 1 — Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai

## Isi

| Berkas | Keterangan |
|---|---|
| `salah_prosedural.py` | Sengaja salah. Dipakai pada Langkah 8 untuk membuktikan gerbang pertama bekerja. Dihapus setelah Langkah 12. |
| `src/mahasiswa.py` | Hasil penulisan ulang menjadi kelas. |
| `src/main.py` | Titik masuk program; satu-satunya berkas yang boleh mencetak ke layar. |
| `tests/test_mahasiswa.py` | Pengujian pertama. |
| `pyproject.toml` | Konfigurasi baku. Tidak boleh diubah mahasiswa. |
| `periksa_pbo.py` | Pemeriksa disiplin objek. Tidak boleh diubah mahasiswa. |

## Menjalankan

```
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux atau macOS
pip install pytest mypy ruff
```

## Tiga gerbang

```
python periksa_pbo.py salah_prosedural.py --profil dasar   # harus GAGAL: 9 pelanggaran
python periksa_pbo.py src --profil dasar                   # harus LOLOS
python -m mypy
python -m pytest
python -m src.main
```

Keluaran yang diharapkan pada gerbang yang lolos:

```
LOLOS. Tidak ada pelanggaran disiplin berorientasi objek.
Success: no issues found in 5 source files
3 passed
Saya Budi Santoso (2410123456), dari Kuok.
```

## Catatan

Berkas `pyproject.toml` memakai `python_version = "3.14"`. Bila laboratorium
masih memakai Python versi lain, ubah baris tersebut pada berkas milik dosen —
bukan pada berkas milik mahasiswa.
