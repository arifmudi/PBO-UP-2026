# Refleksi Praktikum P03: Enkapsulasi & Objek Nilai Beku

1. **Penerapan Property Baca-Saja**
   - Menggunakan `@property` tanpa setter untuk data yang tidak boleh berubah setelah objek dibuat (seperti NIK dan ID/nama).

2. **Setter Bervalidasi sebagai Penjaga Pintu**
   - Seluruh perubahan data yang sensitif (seperti tarif) wajib melewati setter bervalidasi agar objek tidak pernah berada dalam keadaan tidak valid (misal bernilai negatif).
   - Konstruktor wajib menugaskan nilai melalui setter (`self.tarif = tarif`), bukan langsung ke variabel privat (`self._tarif`).

3. **Objek Nilai Beku dengan `@dataclass(frozen=True)`**
   - Menggunakan objek nilai yang tidak dapat diubah (seperti `Alamat` atau `PeriodeTugas`) untuk merepresentasikan data nilai, sehingga aman dikembalikan oleh property tanpa risiko dirusak dari luar.

4. **Pengujian Penolakan dengan `pytest.raises`**
   - Pengujian tidak hanya memastikan masukan benar diterima, tetapi juga membuktikan bahwa masukan salah/invalid secara tegas ditolak oleh program.