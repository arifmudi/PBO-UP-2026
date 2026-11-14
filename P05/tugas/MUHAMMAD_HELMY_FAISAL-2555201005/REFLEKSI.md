# Refleksi Pertemuan 05: Relasi Antar Kelas dan Diagram Kelas

## Pembelajaran

Dalam praktikum P05 ini, titik fokus utama adalah cara menghubungkan antar kelas dan mengendalikan daur hidup datanya di Python. Saya mendalami tiga bentuk relasi: asosiasi (Sewa dan Penyewa berdiri mandiri), agregasi (BarisSewa hanya meminjam rujukan dari AlatTani), dan komposisi (Sewa mengontrol penuh daur hidup BarisSewa, begitu pula Penyewa terhadap Alamat). Poin penting yang saya dapatkan adalah teknik membekukan nilai historis seperti tarif sewa saat transaksi dibuat, sehingga perubahan harga di data master tidak akan merusak riwayat nota lama. Di sisi keamanan kode, penggunaan return `tuple` pada properti baris berhasil menutup celah manipulasi daftar dari luar kelas.

## Kendala dan Solusi

Beberapa kendala teknis sempat muncul selama proses penulisan kode dan pengujian. Pertama, pengujian Pytest gagal akibat salah urutan parameter NIK serta kurangnya argumen pada kelas Alamat, yang diselesaikan dengan menyesuaikan input NIK 16 digit dan melengkapi data dusun, desa, serta kecamatan. Kedua, Mypy memberikan peringatan saat skrip uji mengakses atribut privat, sehingga saya menambahkan decorator `@property` serta method pendukung seperti `baris_nota()` dan `jumlah_alat()`. Ketiga, terdapat kesalahan indentasi pada skrip pengujian yang diatasi dengan menyelaraskan kembali blok spasi kode.