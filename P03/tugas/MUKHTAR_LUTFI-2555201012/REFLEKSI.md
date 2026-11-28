# Refleksi Praktikum P02 - PBO (SIPALA)

## 1. Poin Penting yang Dipelajari
- **Beri Perintah, Jangan Bertanya:** Kelas domain (`Penyewa` dan `AlatTani`) dibuat fokus pada perilaku tanpa langsung melakukan `print()`. Metode hanya mengembalikan teks/nilai (`identitas()`, `kontak()`, `biaya_sewa()`), sedangkan urusan cetak ke layar diserahkan ke `src/main.py`.
- **Fungsi `self`:** Berperan sebagai penanda objek itu sendiri. Tanpa `self`, metode tidak punya akses ke atribut dalam kelas.
- **Kemandirian Objek:** Objek yang dibuat dari kelas yang sama (seperti `budi` dan `siti`) menyimpan datanya masing-masing di memori dan tidak saling menimpa.
- **Type Hinting & Default Parameter:** Penggunaan anotasi tipe (seperti `-> None` pada `__init__`) menjaga kerapian kode, sedangkan nilai bawaan (seperti `telepon: str = "-"`) membantu menangani data opsional.

## 2. Temuan dari Eksperimen Galat

### Melupakan `self` (`TypeError`)
Pesan galat `TypeError: takes 1 positional argument but 2 were given` muncul karena saat metode dipanggil, Python secara otomatis menyisipkan objek itu sendiri sebagai argumen pertama. Tanpa `self` di definisi fungsi, Python menganggap ada kelebihan argumen.

### Mengubah Atribut dari Luar
Saat `alat._tarif_harian` diubah langsung jadi `-5000`, program tetap berjalan dan menghasilkan nilai minus tanpa error. Ini membuktikan bahwa tanda garis bawah (`_`) di Python hanya berupa kesepakatan (*convention*), bukan pembatasan akses fisik. Hal ini berbahaya jika data diubah sembarangan dari luar kelas.

## 3. Langkah yang Dilakukan
- Menyusun direktori `src/model/` dengan benar dan menerapkan penamaan kelas *PascalCase* serta file *snake_case*.
- Memastikan semua tes di `pytest`, `mypy`, dan `periksa_pbo.py --profil p02` lolos hijau.
- Menerapkan pola yang sama untuk tugas kelas `Petugas` beserta pengujian unitnya.