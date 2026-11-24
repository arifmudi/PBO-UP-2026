Refleksi Pertemuan 05: Relasi Antar Kelas dan Diagram Kelas

Pembelajaran

Pada Pertemuan 5, saya mempelajari tentang hubungan antar kelas dalam konsep Pemrograman Berorientasi Objek (PBO), mulai dari penerapannya dalam kode Python hingga penggambarannya menggunakan Diagram Kelas UML. Saya memahami bahwa terdapat tiga jenis relasi utama, yaitu asosiasi, agregasi, dan komposisi. Asosiasi diterapkan pada kelas Sewa dan Penyewa, yaitu hubungan antara dua objek yang tetap dapat berdiri sendiri. Agregasi terlihat pada hubungan BarisSewa dengan AlatTani, di mana data alat tetap tersimpan meskipun transaksi dihapus. Sedangkan komposisi diterapkan pada hubungan Sewa dengan BarisSewa serta Penyewa dengan Alamat, karena objek anak memiliki ketergantungan terhadap objek induknya.

Selain itu, saya juga belajar bahwa data historis, seperti tarif sewa ketika transaksi dilakukan, perlu disimpan agar tidak berubah meskipun harga pada data master mengalami pembaruan. Saya juga memahami penerapan enkapsulasi dengan menggunakan properti berupa tuple agar data di dalam suatu kelas tidak bisa diubah secara langsung dari luar kelas.

Kendala dan Solusi

Dalam proses pengerjaan praktikum P05, saya menemukan beberapa kendala. Pertama, terdapat kesalahan pada urutan parameter NIK di kelas Penyewa dan kelengkapan argumen pada kelas Alamat ketika menjalankan pengujian menggunakan pytest. Solusinya adalah memperbaiki urutan parameter serta memastikan seluruh data yang dibutuhkan sudah dimasukkan.

Kedua, saya mengalami kendala saat pemeriksaan menggunakan Mypy dan Pytest karena beberapa atribut dibuat privat sehingga tidak dapat diakses secara langsung dari luar kelas. Untuk mengatasinya, saya menambahkan properti dan metode pendukung agar data tetap bisa digunakan tanpa mengabaikan konsep enkapsulasi. Terakhir, terdapat kesalahan penulisan indentasi pada kode Python yang menyebabkan pengujian tidak berjalan dengan baik. Saya memperbaikinya dengan menyusun ulang indentasi agar struktur kode menjadi lebih rapi dan dapat dijalankan dengan benar.