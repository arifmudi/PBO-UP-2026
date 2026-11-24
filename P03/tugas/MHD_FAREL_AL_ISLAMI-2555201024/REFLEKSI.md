### REFLEKSI

1. **Refleksi yang didapat setelah mengerjakan P03:**
   * Memahami penerapan enkapsulasi menggunakan atribut non-publik dan properti (*property*)[cite: 11, 13].
   * Mengetahui cara membuat setter bervalidasi agar objek tidak berada pada kondisi tidak sah (seperti tarif minus atau NIK salah)[cite: 11, 14, 16].
   * Menggunakan objek nilai beku dengan `@dataclass(frozen=True)` untuk data yang tidak boleh diubah seperti alamat[cite: 11, 15].

2. **Kendala yang ditemui selama praktikum:**
   * Sempat mengalami error tipe data (`mypy`) saat menyesuaikan atribut `Penyewa` yang awalnya string biasa menjadi objek `Alamat`[cite: 16].
   * Menyesuaikan pengujian penolakan menggunakan `pytest.raises` agar sesuai dengan validasi setter dan properti baca-saja[cite: 18].
```[cite: 10]