# REFLEKSI P04
## Milik Kelas dan Milik Objek

**Nama:** Farel Anugrah  
**NIM:** 2555201007  
**Mata Kuliah:** Pemrograman Berorientasi Objek  
**Pertemuan:** 4

### 1. Hal yang Saya Pelajari

Pada praktikum pertemuan 4, saya mempelajari perbedaan antara atribut milik kelas dan atribut milik objek, serta penggunaan `@classmethod` dan `@staticmethod` dalam Python.

Saya memahami bahwa atribut milik kelas dapat digunakan bersama oleh seluruh objek dalam kelas yang sama, sedangkan atribut milik objek menyimpan data masing-masing objek. Saya juga mempelajari bahwa `@classmethod` digunakan untuk mengakses atau mengelola data tingkat kelas, sedangkan `@staticmethod` digunakan untuk menjalankan fungsi yang tidak membutuhkan akses langsung ke objek maupun kelas.

### 2. Kesulitan yang Dihadapi

Kesulitan yang saya hadapi adalah memahami kesalahan penggunaan atribut milik objek untuk menghitung jumlah seluruh objek. Kesalahan tersebut menyebabkan nilai pencacah tidak bertambah pada tingkat kelas.

Selain itu, saya juga mempelajari masalah penggunaan list sebagai nilai bawaan yang dapat menyebabkan beberapa objek menggunakan daftar yang sama. Dari masalah tersebut, saya memahami pentingnya membedakan data yang seharusnya dimiliki bersama dan data yang harus dimiliki masing-masing objek.

### 3. Penerapan pada Program SIPALA

Pada program SIPALA, saya menerapkan konsep milik kelas dan milik objek pada kelas `AlatTani`.

Saya menambahkan konstanta tarif minimum, tarif maksimum, dan persentase denda harian. Saya juga menerapkan `@staticmethod` untuk memeriksa kewajaran tarif dan memformat nilai rupiah. Selanjutnya, saya menggunakan `@classmethod` untuk menghitung jumlah alat yang terdaftar dan membuat objek dari baris CSV.

### 4. Kesimpulan

Melalui praktikum ini, saya memahami bahwa pemilihan atribut dan method harus disesuaikan dengan tanggung jawabnya. Penggunaan atribut milik kelas dan milik objek yang tepat dapat mencegah kesalahan pengelolaan data serta membuat program lebih terstruktur dan mudah dikembangkan.

### 5. Target Pembelajaran Berikutnya

Pada pertemuan berikutnya, saya ingin lebih memahami penggunaan `@classmethod` dan `@staticmethod`, serta mempelajari bagaimana konsep pewarisan (*inheritance*) dapat diterapkan untuk mengembangkan program SIPALA.
