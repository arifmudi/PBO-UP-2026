# Mengapa PBO diperlukan pada Sistem Pencatatan Obat dan Penjualan Apotek di Bangkinang

## 1. Gambaran Pencatatan Saat Ini
Beberapa apotek kecil di daerah Bangkinang saat ini masih menggunakan pencatatan manual berbasis buku agenda dan nota kertas untuk mengelola operasional sehari-hari. Ketika stok obat baru datang dari distributor, petugas kasir atau apoteker mencatat nama obat, jumlah unit, dan tanggal kadaluarsa (*expiry date*) secara manual di dalam buku besar stok. 

Sementara itu, untuk transaksi penjualan harian, kasir menuliskan nama obat dan harganya pada nota kertas rangkap dua. Lembar pertama diberikan kepada pembeli sebagai bukti pembayaran, sedangkan lembar kedua disimpan dalam laci kasir untuk bahan rekapitulasi keuangan harian.

## 2. Persoalan yang Timbul
Dari alur pencatatan manual di atas, terdapat dua persoalan utama yang sering memicu kendala operasional:

1. **Kesulitan Pemantauan Obat Kadaluarsa dan Stok Menipis**
   Karena tanggal kadaluarsa dan sisa stok hanya tertulis di buku besar, petugas kesulitan memantau obat mana yang sudah mendekati masa *expired* atau mana yang stoknya tinggal sedikit. Hal ini berisiko menyebabkan obat kadaluarsa masih tersimpan di rak penjualan, atau terjadi kekosongan stok obat penting tanpa disadari.
2. **Proses Rekapitulasi Kasir Lambat dan Rentan Salah Hitung**
   Setiap akhir jam operasional, petugas harus menghitung seluruh nota kertas satu per satu menggunakan kalkulator. Proses ini memakan waktu lama dan rentan terhadap *human error* (salah penjumlahkan nota atau nota hilang/selip), sehingga laporan pendapatan harian sering kali tidak sinkron dengan fisik uang kasir.

## 3. Bagian yang Tertolong bila Dimodelkan sebagai Objek (PBO)
Penerapan konsep Pemrograman Berbasis Objek (PBO) dapat membantu menyederhanakan masalah ini dengan memodelkan komponen-komponen apotek menjadi objek digital yang saling berinteraksi:

* **Manajemen Stok dan Peringatan Otomatis via Kelas `Obat`**
  Setiap produk obat dimodelkan sebagai entitas/objek dari kelas `Obat` yang memiliki atribut `kode_obat`, `nama_obat`, `stok`, `harga`, dan `tanggal_kadaluarsa`. Dengan adanya *method* seperti `cek_kadaluarsa()` dan `kurangi_stok()`, sistem secara otomatis dapat memberikan notifikasi atau warna khusus jika suatu obat mendekati tanggal *expired* atau jika stoknya berada di bawah batas minimum.

* **Otomatisasi Transaksi via Kelas `Transaksi` dan `DetailPenjualan`**
  Proses pembungkusan transaksi dapat dibuatkan objek `Transaksi` yang menampung daftar objek `DetailPenjualan`. Setiap kali terjadi penjualan, sistem akan otomatis menghitung total harga, mengurangi atribut `stok` pada objek `Obat` yang bersangkutan, serta merekam riwayat transaksi ke dalam basis data.

Dengan pemodelan berbasis objek ini, pengolahan data apotek menjadi lebih terstruktur, mengurangi ketergantungan pada pencatatan fisik yang rentan rusak, serta mempercepat proses pembuatan laporan keuangan dan inventaris.