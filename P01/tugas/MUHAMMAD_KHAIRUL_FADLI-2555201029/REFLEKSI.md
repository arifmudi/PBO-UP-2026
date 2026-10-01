# Mengapa PBO diperlukan pada Sistem Pencatatan dan Layanan Pencucian Motor di Bangkinang

## 1. Gambaran Pencatatan Saat Ini
Sebagian besar usaha pencucian motor skala kecil di wilayah Bangkinang saat ini menerapkan sistem operasional yang sangat sederhana tanpa adanya pencatatan transaksi sama sekali. Pelanggan cukup datang menyerahkan motor, menunggu proses pencucian selesai, lalu langsung membayar uang tunai kepada petugas kasir atau pekerja cuci tanpa menerima nota maupun bukti pembayaran. 

Pencatatan pendapatan biasanya hanya dilakukan secara kasar di akhir hari dengan menghitung total fisik uang tunai yang ada di dalam laci kasir tanpa merekam berapa jumlah motor yang telah dicuci hari itu.

## 2. Persoalan yang Timbul
Meskipun alur ini terkesan praktis dan cepat, metode tanpa pencatatan ini menimbulkan dua masalah utama bagi pemilik usaha:

1. **Risiko Kebocoran Pendapatan dan Ketidaksesuaian Data**
   Karena tidak ada catatan motor masuk dan jenis paket cuci yang dipilih (misalnya cuci biasa vs cuci salju/pengilap), pemilik tempat cuci sulit memantau apakah pendapatan fisik tunai yang terkumpul sudah sesuai dengan jumlah motor yang sebenarnya dilayani oleh pekerja.
2. **Kesulitan Membagi Hasil Kerja dan Rekapitulasi Keuangan**
   Pengelola kesulitan menghitung bagi hasil atau komisi harian untuk para pekerja cuci karena tidak ada riwayat detail mengenai siapa mencuci motor yang mana. Selain itu, pemilik usaha tidak bisa menganalisis tren hari/jam tersibuk serta rekap harian sering kali tidak akurat.

## 3. Bagian yang Tertolong bila Dimodelkan sebagai Objek (PBO)
Dengan menerapkan pendekatan Pemrograman Berbasis Objek (PBO), operasional pencucian motor kecil ini dapat dirapikan melalui pemodelan digital yang tetap cepat digunakan:

* **Pencatatan Ringkas via Kelas `Kendaraan` dan `PaketCuci`**
  Setiap motor yang masuk dimodelkan sebagai objek dari kelas `Kendaraan` (atribut: `plat_nomor`, `jenis_motor`) dan memilih objek dari kelas `PaketCuci` (atribut: `nama_paket`, `harga`). Saat motor selesai dicuci dan dibayar, sistem tinggal menghubungkan kedua objek ini secara cepat tanpa membuang waktu.

* **Otomatisasi Hitung Komisi & Rekap via Kelas `Transaksi`**
  Aktivitas pembayaran dimodelkan ke dalam objek `Transaksi` yang mencatat objek `Kendaraan`, `Pekerja`, dan total pembayaran. Kelas ini memiliki *method* seperti `hitung_komisi_pekerja()` dan `rekam_pendapatan()`. Setiap kali transaksi dicatat, sistem otomatis menghitung bagian upah pekerja dan merekap total pendapatan secara real-time.

Melalui pemodelan berorientasi objek ini, usaha pencucian motor tetap dapat melayani pembayaran langsung dengan cepat, sekaligus mencegah kebocoran uang dan memudahkan pembagian komisi pekerja secara transparan.