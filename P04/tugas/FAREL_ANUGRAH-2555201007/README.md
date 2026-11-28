Push-Location ..\..\..\P04\tugas\FAREL_ANUGRAH-2555201007

@'
# P04 — Milik Kelas dan Milik Objek

**Nama:** Farel Anugrah  
**NIM:** 2555201007  
**Mata Kuliah:** Pemrograman Berorientasi Objek

## Deskripsi

Praktikum P04 membahas konstanta tingkat kelas, atribut milik kelas, serta penggunaan `@classmethod` dan `@staticmethod` pada Python.

## Implementasi

Pada kelas `AlatTani`, implementasi meliputi:

- Konstanta tarif minimum dan maksimum.
- Konstanta persentase denda harian.
- Validasi tarif menggunakan `staticmethod`.
- Format mata uang rupiah menggunakan `staticmethod`.
- Penghitungan jumlah objek menggunakan `classmethod`.
- Pembuatan objek dari baris CSV menggunakan `classmethod`.
- Perhitungan denda keterlambatan.

## Pemeriksaan

- Pemeriksa disiplin PBO profil P04: LOLOS.
- Mypy: tidak ditemukan masalah pada 12 berkas sumber.
- Pytest: 44 tes berhasil.

## Menjalankan Program

```powershell
python -m src.main