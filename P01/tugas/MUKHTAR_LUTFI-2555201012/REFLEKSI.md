# Mengapa PBO Diperlukan pada Sistem Pencatatan Penyewaan Sound System dan Panggung Acara di Kecamatan Salo

## Gambaran Proses Pencatatan Saat Ini
Usaha penyewaan sound system melayani kebutuhan hajatan warga, acara desa, maupun kegiatan instansi lokal. Saat ini, seluruh proses operasional mulai dari pemesanan paket alat, penjadwalan tanggal acara, hingga pembayaran DP dan pelunasan masih dicatat secara manual menggunakan buku agenda harian dan nota kertas.

## Persoalan yang Timbul
Pencatatan manual yang berjalan saat ini menimbulkan beberapa masalah nyata, di antaranya:
1. **Jadwal Bentrok dan Double Booking:** Pengelola sering kesulitan memantau ketersediaan perangkat khusus seperti genset atau unit speaker tertentu saat terjadi tumpukan acara di akhir pekan, sehingga berisiko terjadi pemesanan ganda di tanggal yang sama.
2. **Keterlacakan Unit dan Status Pelunasan:** Kelengkapan kecil seperti kabel rol dan mikrofon nirkabel rawan tertukar atau tertinggal di lokasi acara. Selain itu, pengelola kesulitan mengecek siapa saja penyewa yang belum melunasi sisa tagihan tanpa harus membongkar tumpukan nota lama satu per satu.

## Solusi Pemodelan Berbasis Objek (PBO)
Permasalahan di atas akan sangat terbantu jika sistem informasi penyewaan ini dimodelkan menggunakan Pemrograman Berbasis Objek (PBO). 

Dengan PBO, kita bisa memecah entitas nyata menjadi kelas-kelas khusus seperti `Pelanggan`, `PeralatanAudio`, dan `JadwalSewa`. Setiap atribut (seperti status ketersediaan alat atau sisa tagihan) tersimpan rapi di dalam objeknya masing-masing (*enkapsulasi*). Selain itu, fungsi/perilaku seperti `cek_ketersediaan_jadwal(tanggal)` atau `validasi_kelengkapan_kembali()` dapat melekat langsung pada objek terkait. Hal ini mencegah bentrok jadwal serta mempermudah pengawasan inventaris barang secara otomatis.