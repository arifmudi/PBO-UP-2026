# Refleksi Praktikum PBO Pertemuan 3: Enkapsulasi

## Ringkasan Pembelajaran

Di praktikum kali ini, saya belajar cara mengamankan data objek agar tidak bisa diisi sembarangan (seperti tarif minus atau NIK ngasal):

1. **Property (Baca-Saja):** Mengunci atribut agar nilainya tidak bisa diubah dari luar setelah objek dibuat, contohnya `kode` dan `nama` alat.
2. **Setter Bervalidasi:** Menjadi filter pintu masuk saat data diubah. Jika data yang dimasukkan tidak valid (misal tarif <= 0), program langsung melempar `ValueError`.
3. **Konstruktor Wajib Lewat Setter:** Pentingnya memanggil setter di dalam `__init__` (misal `self.tarif_harian = tarif_harian` bukannya `self._tarif_harian`), supaya nilai awal dari konstruktor tetap melewati validasi dan tidak membocorkan data salah.
4. **`@dataclass(frozen=True)`:** Digunakan untuk membuat objek nilai (*value object*) seperti `Alamat` yang sifatnya sekali buat dan tidak boleh diubah isinya.
5. **Mitos Double Underscore (`__`):** Pembuktian bahwa `__` (name mangling) bukan proteksi sungguhan karena nama variabelnya masih bisa diakses lewat nama aslinya (misal `_Dompet__saldo`). Keamanan kode yang sebenarnya ada pada logika setter dan pengujian (*unit test*).

## Kendala yang Dihadapi

* Sempat mengalami error pada pembuatan *unit test* untuk validasi nomor telepon (`pytest.raises`), karena inisialisasi awal dengan data salah ditaruh di luar blok `with pytest.raises(...)`.
* Mengalami kendala sintaks saat mencoba menjalankan perintah Python satu baris (*one-liner*) di terminal PowerShell.

## Rencana Perbaikan & Penerapan

* Lebih teliti saat menulis pengujian penolakan (*rejection tests*) menggunakan `pytest.raises` agar penanganan *exception* tepat pada baris yang meng-raise error.
* Memastikan semua atribut di kelas berikutnya (seperti kelas `Petugas`) dikategorikan dengan benar ke dalam tiga tingkat penjagaan: baca-saja, baca-tulis bervalidasi, atau objek beku.