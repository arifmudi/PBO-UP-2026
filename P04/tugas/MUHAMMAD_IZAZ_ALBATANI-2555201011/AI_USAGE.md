# AI_USAGE.md

## Penggunaan AI dalam Praktikum P04 dan Tugas 1 Kios

AI digunakan sebagai alat bantu pembelajaran dalam memahami konsep Pemrograman Berorientasi Objek (PBO) menggunakan Python.

### Bagian yang Dibantu AI

1. Membantu memahami penggunaan konstanta kelas dengan `Final`.
2. Memberikan penjelasan tentang penggunaan `@staticmethod` dan `@classmethod`.
3. Membantu menyusun konstruktor alternatif untuk membaca data produk.
4. Membantu memahami validasi harga modal dan harga jual menggunakan margin minimum.
5. Membantu menyusun pengujian menggunakan `pytest`.
6. Membantu memperbaiki kesalahan kode berdasarkan hasil pemeriksaan Ruff dan MyPy.

### Implementasi yang Dikerjakan

Pada praktikum P04, implementasi menggunakan kelas `AlatTani`.

Pada Tugas 1, implementasi menggunakan kelas `Kios` untuk mengelola produk UMKM, seperti beras, gula pasir, dan minyak goreng.

Fitur kelas `Kios` meliputi:
- Konstanta kelas menggunakan `Final`.
- Penghitung jumlah produk.
- Validasi harga modal dan harga jual.
- Margin keuntungan minimum sebesar 10%.
- Konstruktor alternatif menggunakan `@classmethod`.
- Pemeriksaan kewajaran harga menggunakan `@staticmethod`.
- Format tampilan harga menggunakan f-string.

### Verifikasi

Hasil pemeriksaan setelah implementasi:
- Pytest: 40 pengujian berhasil.
- MyPy: tidak ditemukan masalah pada 14 file sumber.
- Ruff: seluruh pemeriksaan berhasil.
- Pemeriksa disiplin PBO profil P04: LOLOS.

### Kesimpulan

AI digunakan sebagai pendamping untuk memahami materi, membantu proses implementasi, dan memperbaiki kesalahan program. Kode tetap diperiksa dan diuji menggunakan perangkat pengujian yang tersedia agar sesuai dengan ketentuan praktikum dan tugas.