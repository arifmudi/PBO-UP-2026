# Mengapa PBO diperlukan pada Sistem Manajemen Kost dan Tagihan Bulanan di Bangkinang

## 1. Gambaran Pencatatan Saat Ini
Pengelolaan usaha rumah kost di daerah Bangkinang umumnya masih mengandalkan pencatatan manual menggunakan buku tulis atau pesan di WhatsApp. Pemilik kost mencatat identitas penghuni, nomor kamar, tanggal masuk, serta kesepakatan harga sewa bulanan secara manual.

Setiap awal atau akhir bulan, pemilik kost harus mengecek satu per satu catatan di buku untuk mengetahui siapa saja penghuni yang sudah memasuki jatuh tempo pembayaran. Pembayaran sewa beserta biaya tambahan (seperti listrik atau air) biasanya diterima secara tunai atau transfer bank, lalu pemilik kost memberikan kuitansi kertas atau sekadar mengonfirmasi lewat pesan singkat.

## 2. Persoalan yang Timbul
Metode pengelolaan manual berbasis buku dan catatan pesan ini sering memicu beberapa kendala operasional:

1. **Pengawasan Jatuh Tempo dan Tagihan Tambahan yang Luput**
   Pemilik kost sering kesulitan memantau tanggal jatuh tempo pembayaran tiap penghuni yang berbeda-beda. Hal ini menyebabkan penagihan sering terlambat atau biaya variabel (seperti kelebihan pemakaian listrik) lupa dihitung dan ditagihkan.
2. **Riwayat Pembayaran Rusak atau Tercecer**
   Pencatatan pembayaran yang tercecer di buku atau pesan WhatsApp membuat pemilik kost susah merekap total pendapatan bulanan secara pasti. Selain itu, sering terjadi selisih paham dengan penghuni terkait bukti transfer yang belum terverifikasi dengan rapi.

## 3. Bagian yang Tertolong bila Dimodelkan sebagai Objek (PBO)
Dengan menerapkan konsep Pemrograman Berbasis Objek (PBO), sistem pengelolaan kost dapat dimodelkan secara lebih terstruktur dan efisien:

* **Manajemen Kamar dan Penghuni via Kelas `Kamar` dan `Penghuni`**
  Setiap kamar dimodelkan sebagai objek dari kelas `Kamar` (atribut: `nomor_kamar`, `tipe_kamar`, `harga_sewa`, `status_terisi`). Informasi penyewa disimpan dalam kelas `Penghuni` (atribut: `nama`, `no_hp`, `tanggal_masuk`). Dengan adanya *method* seperti `cek_status_kamar()`, sistem dapat menampilkan kamar mana saja yang masih kosong atau terisi secara akurat.

* **Otomatisasi Kalkulasi Tagihan via Kelas `Tagihan`**
  Aktivitas pembayaran bulanan dimodelkan ke dalam kelas `Tagihan` yang menghubungkan objek `Kamar` dan `Penghuni`. Kelas ini memiliki atribut `biaya_sewa`, `biaya_listrik`, dan `denda_keterlambatan`, serta dilengkapi *method* `hitung_total_tagihan()`. Sistem akan secara otomatis mengkalkulasi total pembayaran yang harus dilunasi penghuni sesuai durasi dan tagihan tambahan tanpa perlu dihitung manual.

Melalui pendekatan berorientasi objek ini, manajemen rumah kost menjadi lebih rapi, pemantauan tagihan bulanan lebih teratur, dan laporan keuangan harian maupun bulanan dapat tersimpan dengan jelas.