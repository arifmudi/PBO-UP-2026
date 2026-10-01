# Mengapa PBO diperlukan pada Sistem Pencatatan Layanan Laundry Kiloan di Bangkinang

## 1. Gambaran Pencatatan Saat Ini
Kebanyakan usaha laundry kiloan di daerah Bangkinang saat ini masih mengandalkan pencatatan manual di nota kertas rangkap dua. Waktu pelanggan mengantar pakaian, kasir menimbang berat baju, mencatat nama pelanggan, nomor HP, jenis paket (misalnya cuci setrika atau cuci kering), serta estimasi tanggal selesai di lembar nota.

Nota lembar pertama biasanya diberikan ke pelanggan sebagai bukti pengambilan, sedangkan lembar kedua disematkan di kantong plastik pakaian. Setelah pakaian selesai dicuci dan disetrika, kasir akan menghubungi pelanggan lewat WhatsApp atau menunggu pelanggan datang mengambil sendiri sambil melunasi pembayaran.

## 2. Persoalan yang Timbul
Alur pencatatan manual menggunakan nota kertas ini sering menimbulkan beberapa masalah operasional:

1. **Risiko Pakaian Tertukar atau Nota Hilang**
   Nota kertas sangat rentan basah, sobek, atau hilang. Kalau nota di kantong pakaian hilang, petugas kasir sering bingung menentukan pakaian mana milik siapa. Selain itu, status pengerjaan (apakah masih dicuci, sedang disetrika, atau sudah siap ambil) tidak terpantau secara jelas.
2. **Rekapitulasi Keuangan dan Penentuan Berat yang Kurang Akurat**
   Proses menghitung total pemasukan harian dengan cara menjumlahkan potongan nota satu per satu makan waktu dan rawan salah hitung. Pemilik usaha juga susah melacak paket layanan mana yang paling laku atau melihat riwayat langganan tiap pelanggan.

## 3. Bagian yang Tertolong bila Dimodelkan sebagai Objek (PBO)
Masalah-masalah di atas bisa dirapikan jika sistemnya dimodelkan ke dalam konsep Pemrograman Berbasis Objek (PBO):

* **Kejelasan Pelanggan dan Paket via Kelas `Pelanggan` dan `Layanan`**
  Data konsumen disimpan dalam kelas `Pelanggan` (atribut: `id_pelanggan`, `nama`, `no_hp`). Pilihan paket dimodelkan ke dalam kelas `Layanan` (atribut: `nama_paket`, `harga_per_kg`). Dengan struktur ini, sistem gampang mengenali identitas pemilik cucian dan menghitung tarif dasar secara konsisten.

* **Pelacakan Status Cucian via Kelas `Pesanan`**
  Setiap transaksi dimodelkan ke dalam kelas `Pesanan` yang menghubungkan objek `Pelanggan` dan `Layanan`. Kelas ini punya atribut seperti `berat_kg`, `status_pengerjaan` (Diproses/Selesai), serta *method* `hitung_total_biaya()` dan `update_status()`. Begitu status cucian diubah jadi "Selesai", sistem bisa langsung memperbarui riwayat pesanan sehingga tidak ada lagi cerita cucian tertukar atau lupa dikerjakan.

Dengan pendekatan PBO ini, proses penerimaan hingga pengambilan cucian jadi lebih teratur, meminimalkan risiko nota hilang, dan membantu pemilik laundry merekap pendapatan harian secara otomatis.