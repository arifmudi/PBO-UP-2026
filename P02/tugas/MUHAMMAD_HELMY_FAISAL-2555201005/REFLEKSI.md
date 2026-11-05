# Refleksi Praktikum P02: Pembuatan Kelas Dasar & Objek

1. **Pentingnya Parameter `self` pada Method**
   - Mengetahui bahwa `self` wajib ditulis sebagai parameter pertama di setiap *method*. Jika lupa, Python akan menghasilkan `TypeError` karena secara otomatis objek selalu mengirimkan dirinya sebagai argumen pertama.

2. **Pemisahan Logika (*Model*) dan Tampilan (*Output*)**
   - Kelas domain pada folder `src/model` hanya bertugas mengolah data dan mengembalikan nilai (`return`), tanpa menggunakan perintah `print`. Urusan mencetak ke layar sepenuhnya ditangani oleh `src/main.py`.

3. **Kemandirian Data Antar Objek**
   - Setiap objek yang dibuat dari cetak biru (*class*) yang sama akan menyimpan datanya secara terpisah. Mengubah nilai atribut pada satu objek tidak akan memengaruhi data pada objek lainnya.

4. **Kelemahan Enkapsulasi Bawaan Python**
   - Awalan garis bawah (seperti `_tarif_h