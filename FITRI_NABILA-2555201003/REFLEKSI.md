# Mengapa PBO diperlukan pada Sistem Pencatatan Stok dan Penjualan Toko Kelontong di Bangkinang

## 1. Gambaran Pencatatan Saat Ini
Sebagian besar toko kelontong skala kecil di wilayah Bangkinang saat ini masih menggunakan sistem pencatatan manual berbasis buku agenda dan kalkulator. Ketika pasokan barang baru tiba dari distributor, pemilik toko mencatat nama barang, jumlah stok, dan harga beli secara manual pada buku persediaan. 

Saat transaksi penjualan berlangsung, kasir atau pemilik toko menghitung total belanjaan pembeli menggunakan kalkulator, kemudian menyimpan uang pembayaran ke laci kasir. Rekapitulasi pendapatan baru dilakukan di akhir hari dengan mencatat total uang yang masuk tanpa merinci barang apa saja yang telah terjual.

## 2. Persoalan yang Timbul
Penggunaan metode pencatatan manual ini menimbulkan dua persoalan utama dalam operasional toko:

1. **Stok Barang Tidak Terpantau secara Real-Time**
   Karena barang yang terjual tidak langsung mengurangi data stok di buku persediaan, pemilik toko sulit mengetahui sisa stok fisik secara akurat. Hal ini sering menyebabkan barang yang diminati mendadak habis (*out of stock*), atau adanya barang yang rusak/kadaluarsa karena menumpuk terlalu lama di gudang.
2. **Proses Rekapitulasi Keuangan Lambat dan Rentan Salah Hitung**
   Proses perhitungan ulang seluruh transaksi harian menggunakan kalkulator membutuhkan waktu lama dan rentan terhadap *human error*. Selain itu, pemilik toko sulit menentukan laba bersih harian karena rincian Harga Pokok Penjualan (HPP) per produk tidak tercatat secara otomatis.

## 3. Bagian yang Tertolong bila Dimodelkan sebagai Objek (PBO)
Dengan menerapkan pendekatan Pemrograman Berbasis Objek (PBO), kendala operasional tersebut dapat diatasi melalui pemodelan entitas toko menjadi beberapa objek yang terstruktur:

* **Manajemen Stok dan Notifikasi via Kelas `Barang`**
  Setiap produk dimodelkan sebagai objek dari kelas `Barang` yang memiliki atribut `kode_barang`, `nama_barang`, `stok`, `harga_beli`, dan `harga_jual`. Kelas ini dilengkapi dengan *method* seperti `kurangi_stok()` dan `cek_stok_minimum()`. Sistem dapat memberikan peringatan otomatis apabila atribut `stok` suatu barang telah mencapai batas minimal agar proses pemesanan ulang dapat segera dilakukan.

* **Otomatisasi Penjualan via Kelas `Transaksi`**
  Setiap aktivitas pembayaran dimodelkan ke dalam objek `Transaksi` yang menampung kumpulan objek `ItemBelanja`. Saat transaksi diproses, sistem secara otomatis memanggil *method* `kurangi_stok()` pada objek `Barang` yang dibeli, menghitung total bayar secara presisi, dan menyimpan riwayat transaksi digital.

Melalui pemodelan berbasis objek ini, pengelolaan data barang dan transaksi toko kelontong menjadi lebih terorganisir, meminimalkan risiko kesalahan perhitungan manual, serta memudahkan penyusunan laporan keuangan secara akurat.