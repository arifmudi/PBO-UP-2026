# Refleksi Praktikum P03 - Enkapsulasi & Objek Nilai Beku

Praktikum kali ini fokus utamanya adalah menutup celah keamanan data yang sempat lolos di Pertemuan 2.

## 1. Pembelajaran Utama & Perubahan Kode
- **Mencegah Data Rusak Sejak Awal:** Membuat `property` baca-saja (`kode` dan `nama`) memastikan identitas objek tidak bisa diubah sembarangan dari luar.
- **Validasi Lewat Setter:** Mengarahkan penugasan nilai di konstruktor langsung ke `setter` ternyata sangat krusial. Jika tidak lewat `setter`, nilai tak valid (seperti tarif bernilai minus atau nol) bisa lolos saat objek baru dibuat.
- **Penggunaan Objek Beku (`frozen=True`):** Mengubah data seperti `Alamat` menjadi *value object* yang *frozen* terbukti lebih aman daripada sekadar menyimpan teks mentah di dalam `Penyewa`.
- **Pengujian Penolakan:** Fokus pengujian tidak lagi cuma memastikan fungsi berjalan saat diberi masukan benar, tetapi membuktikan bahwa program *pasti menolak* saat diberi nilai yang salah menggunakan `pytest.raises`.

## 2. Masalah yang Ditemui & Solusi
- **Pengujian Gagal pada Nilai Batas:** Sempat mengalami *failing test* pada `test_biaya_sewa_gratis` karena *setter* menolak tarif 0 (`nilai <= 0`). Solusinya adalah menyesuaikan pengujian untuk membuktikan penolakan tarif nol sesuai aturan validasi di model.
- **Format Input Telepon:** Penolakan terjadi pada string nomor telepon yang mengandung karakter `+` karena pembersihan hanya menghapus spasi dan `-`. Solusinya adalah menggunakan format angka murni pada data pengujian.

## 3. Kesimpulan
Ketik kode memang jadi sedikit lebih panjang karena harus menulis `property` dan `setter` secara eksplisit, tapi timbal baliknya program jadi jauh lebih kokoh dan tidak diam-diam menyimpan data minus atau error di nota transaksi.