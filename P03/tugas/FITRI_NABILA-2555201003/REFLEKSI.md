## Refleksi Praktikum P03

Setelah mengikuti praktikum P03, saya jadi lebih memahami pentingnya menjaga data di dalam sebuah program. Dari praktikum ini, saya belajar bahwa data yang dimasukkan tidak boleh dibiarkan begitu saja, karena kalau nilainya salah, program bisa menghasilkan sesuatu yang tidak sesuai. Misalnya, gaji atau tarif yang bernilai negatif tentu tidak masuk akal.

Saya juga belajar menggunakan `@property` dan setter untuk mengatur data agar tidak bisa diubah sembarangan. Data yang tidak seharusnya berubah bisa dibuat hanya bisa dibaca, sedangkan data yang masih boleh berubah harus diperiksa terlebih dahulu. Selain itu, saya belajar membuat objek yang nilainya tidak bisa diubah menggunakan `@dataclass(frozen=True)`.

Hal lain yang saya pahami adalah pengujian program bukan hanya untuk memastikan kode berjalan dengan benar, tetapi juga untuk memastikan program bisa menolak data yang salah. Dengan menggunakan `pytest.raises`, saya bisa menguji apakah program memberikan penolakan ketika menerima nilai yang tidak sesuai.

Dari praktikum ini, saya menyadari bahwa membuat program bukan hanya tentang membuat kode yang bisa berjalan, tetapi juga memastikan data di dalamnya tetap aman dan sesuai aturan. Ke depannya, saya ingin lebih teliti dalam membuat validasi dan pengujian supaya program yang saya buat tidak mudah mengalami kesalahan.