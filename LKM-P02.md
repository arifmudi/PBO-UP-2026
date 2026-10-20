# LEMBAR KERJA MAHASISWA
## Pertemuan 2 — Kelas Pertama SIPALA: Penyewa dan AlatTani

**Nama:** Ratu Salsabila  
**NIM:** 2555201021  
**Kelas:** A  
**Tanggal:** 20 Oktober 2026  
**Tautan repositori:** https://github.com/ratusalsabilafr/pbo-sipala-2555201021

---

# A. KUIS AWAL

### 1. Sebutkan ketiga gerbang mutu beserta apa yang diperiksa masing-masing.

**Jawaban:**

Ketiga gerbang mutu adalah:

1. **Pemeriksaan disiplin PBO**, yaitu memeriksa apakah kode mengikuti aturan pemrograman berorientasi objek.
2. **Mypy**, yaitu memeriksa kesesuaian tipe data dan anotasi tipe pada kode Python.
3. **Pytest**, yaitu menjalankan pengujian untuk memastikan program bekerja sesuai dengan hasil yang diharapkan.

### 2. Pada Pertemuan 1 sebuah program berjalan benar tetapi tetap ditolak gerbang. Apa sebabnya?

**Jawaban:**

Program yang berjalan dengan benar belum tentu memenuhi aturan PBO. Kode juga harus mempunyai struktur yang sesuai, mengikuti aturan pemrograman berorientasi objek, menggunakan anotasi tipe dengan benar, dan lolos pengujian.

### 3. Kode PBO-001 berbunyi “kode berjalan di tingkat modul”. Apa maksudnya, dan bagaimana memperbaikinya?

**Jawaban:**

Kode berjalan di tingkat modul berarti terdapat perintah yang langsung dijalankan ketika modul dibaca atau diimpor. Cara memperbaikinya adalah memindahkan perintah tersebut ke dalam fungsi atau metode. Untuk menjalankan program utama, gunakan blok `if __name__ == "__main__":`.

### 4. Mengapa folder `src/model` tidak boleh memuat perintah `print`?

**Jawaban:**

Karena folder `src/model` bertugas menyimpan kelas dan logika pengolahan data, bukan menampilkan hasil ke layar. Perintah `print` sebaiknya diletakkan di `src/main.py` agar tugas setiap bagian program terpisah dan kode lebih mudah dirawat.

---

# B. PENGAMATAN PRAKTIKUM

## B.1 Galat akibat `self` yang terlupa (Langkah 5)

**Pesan galat:**

```text
TypeError: AlatTani.biaya_sewa() takes 1 positional argument
but 2 were given
```

**Penjelasan:**

Galat tersebut terjadi karena parameter `self` terlupa ditulis pada definisi metode. Ketika metode dipanggil melalui objek, Python otomatis mengirimkan objek sebagai argumen pertama. Jadi, pemanggilan `alat.biaya_sewa(3)` sebenarnya mengirimkan dua argumen, yaitu objek `alat` dan angka `3`. Perbaikannya adalah menambahkan parameter `self` pada definisi metode.

## B.2 Tarif yang diubah dari luar (Langkah 8)

**1. Berapa nilai tarif sesudah diubah dari luar?**

Jawaban: Tarif berubah menjadi `-5000` atau minus Rp5.000 per hari.

**2. Berapa biaya sewa 3 hari yang dihasilkan?**

Jawaban: Biaya sewa menjadi `-15000` atau minus Rp15.000.

**3. Apakah Python menampilkan peringatan? Mengapa?**

Jawaban: Tidak. Python tetap menjalankan program karena perubahan atribut tersebut tidak otomatis dianggap sebagai kesalahan oleh Python.

**4. Menurut Anda, kapan kesalahan seperti ini akan ketahuan di dunia nyata?**

Jawaban: Kesalahan dapat diketahui ketika perhitungan biaya digunakan dalam transaksi dan menghasilkan tarif yang tidak masuk akal, misalnya saat petani melakukan pembayaran sewa alat.

## B.3 Bukti ketiga gerbang hijau (Langkah 10)

| Gerbang | Keluaran |
|---|---|
| `python periksa_pbo.py src --profil p02` | LOLOS. Tidak ada pelanggaran disiplin berorientasi objek. |
| `python -m mypy` | Success: no issues found in 12 source files |
| `python -m pytest` | 11 passed in 0.57s |

**Catatan:** Keluaran di atas mengikuti hasil pemeriksaan P02 yang sebelumnya kamu dapatkan. Jika hasil di terminal berbeda, gunakan keluaran terbaru dari terminalmu.

---

# C. AKTIVITAS KELOMPOK: MERANCANG KELAS KERAMBA

**Anggota kelompok:** Sesuaikan dengan anggota kelompok praktikum.

## C.1 Kerangka kelas Keramba

```python
"""Model keramba untuk memperkirakan hasil panen ikan."""


class Keramba:
    """Menyimpan data keramba dan menghitung perkiraan panen."""

    def __init__(
        self,
        kode: str,
        ukuran: float,
        jumlah_bibit: int = 0,
    ) -> None:
        self._kode = kode
        self._ukuran = ukuran
        self._jumlah_bibit = jumlah_bibit

    def perkiraan_panen(
        self,
        tingkat_kelulusan_hidup: float,
        berat_per_ekor: float,
    ) -> float:
        """Menghitung perkiraan berat panen dalam kilogram."""
        jumlah_ikan_hidup = (
            self._jumlah_bibit * tingkat_kelulusan_hidup
        )
        return jumlah_ikan_hidup * berat_per_ekor
```

## C.2 Dua pertanyaan perancangan

### 1. Parameter mana yang layak diberi nilai default, dan mengapa justru parameter itu?

**Jawaban:**

Parameter `jumlah_bibit` layak diberi nilai default `0` karena jumlah bibit dapat belum ditentukan ketika objek keramba dibuat. Sementara itu, kode dan ukuran keramba sebaiknya diberikan saat pembuatan objek agar identitas dan ukuran keramba jelas.

### 2. Mengapa tingkat kelulusan hidup sebaiknya menjadi parameter method, bukan atribut keramba?

**Jawaban:**

Karena tingkat kelulusan hidup dapat berubah tergantung kondisi pemeliharaan dan waktu pengamatan. Dengan menjadikannya parameter metode, perkiraan panen dapat dihitung menggunakan tingkat kelulusan hidup yang berbeda tanpa mengubah data tetap pada objek keramba.

---

# D. REFLEKSI PENUTUP

### 1. Pada pertemuan ini objek Anda tidak mengizinkan atributnya dibaca dari luar; yang keluar hanya hasil method. Menurut Anda apa untungnya cara demikian?

**Jawaban:**

Keuntungannya adalah data objek lebih terjaga dan pengguna tidak bergantung langsung pada atribut di dalam kelas. Pengguna cukup memanggil metode yang disediakan sehingga pengolahan data lebih teratur dan perubahan kode lebih mudah dikelola.

### 2. Sebutkan satu hal yang belum Anda pahami, dan tuliskan pertanyaan yang akan Anda ajukan pada Pertemuan 3.

**Jawaban:**

Saya masih ingin memahami cara melindungi atribut agar tidak diubah sembarangan dari luar kelas. Pertanyaan saya untuk Pertemuan 3 adalah: bagaimana penggunaan `@property` dapat membantu mengontrol akses dan perubahan nilai atribut pada Python?

---

**Paraf Asisten/Dosen:** ....................................

**Tanda Tangan Mahasiswa:** ....................................