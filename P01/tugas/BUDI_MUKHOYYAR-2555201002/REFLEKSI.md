 # Mengapa PBO diperlukan pada Sistem Pemesanan Lapangan Futsal di Bangkinang

## 1. Gambaran Pencatatan Saat Ini
Beberapa pengelola lapangan futsal di area Bangkinang saat ini masih menggunakan pencatatan manual berupa papan tulis, buku kalender, dan obrolan WhatsApp untuk mengelola jadwal sewa. Ketika pelanggan hendak memesan jadwal (*booking*), pengelola akan mengecek ketersediaan jam secara manual di papan tulis atau kalender, lalu mencatat nama pemesan, nomor HP, jam sewa, dan status uang muka (*DP*) di buku besar harian.

Setiap kali tim selesai bertanding, pengelola menerima pelunasan sisa pembayaran secara tunai atau transfer, kemudian mencatat total pemasukan di lembaran kasir harian.

## 2. Persoalan yang Timbul
Penggunaan metode pencatatan manual berbasis buku dan papan tulis ini sering memicu dua persoalan utama:

1. **Risiko Jadwal Bentrok (*Double Booking*) dan Kesulitan Pemantauan DP**
   Karena konfirmasi pemesanan sering masuk secara bersamaan melalui WhatsApp dan pendaftaran langsung di tempat, pengelola rentan melakukan kesalahan pencatatan yang mengakibatkan dua tim memesan jam dan lapangan yang sama. Selain itu, pencatatan batas waktu pembayaran DP yang masih manual sering kali membingungkan status reservasi (apakah jadwal sudah pasti atau masih menggantung).
2. **Rekapitulasi Pendapatan Sewa Lambat dan Rawan Tercecer**
   Proses rekap harian memerlukan waktu lama karena pengelola harus mencocokkan catatan DP, pelunasan di tempat, dan bukti transfer satu per satu. Hal ini rentan terhadap *human error* atau catatan hilang/tercecer, sehingga laporan bulanan pemilik tempat futsal kurang akurat.

## 3. Bagian yang Tertolong bila Dimodelkan sebagai Objek (PBO)
Dengan menerapkan konsep Pemrograman Berbasis Objek (PBO), kendala operasional tersebut dapat diatasi melalui pemodelan entitas lapangan futsal menjadi objek-objek terstruktur:

* **Pencegahan Jadwal Bentrok via Kelas `Lapangan` dan `Reservasi`**
  Lapangan dimodelkan sebagai objek dari kelas `Lapangan` dengan atribut seperti `id_lapangan`, `jenis_lantai`, dan `tarif_per_jam`. Aktivitas penyewaan dimodelkan ke dalam kelas `Reservasi` yang memiliki atribut `jam_mulai`, `jam_selesai`, `pemesan`, dan `status_bayar`. Melalui *method* seperti `cek_ketersediaan_jadwal()`, sistem secara otomatis akan menolak pemesanan baru jika slot jam yang diminta sudah terikat (*instantiated*) dengan objek `Reservasi` lain pada lapangan yang sama.

* **Otomatisasi Hitung Biaya & Pembayaran via Kelas `Pembayaran`**
  Setiap transaksi diwakili oleh objek dari kelas `Pembayaran` yang memiliki *method* `hitung_sisa_bayar()` dan `konfirmasi_dp()`. Sistem secara otomatis dapat menghitung total biaya sewa berdasarkan durasi jam dan mengkalkulasi sisa tagihan di lokasi secara tepat tanpa perlu dihitung manual.

Melalui pemodelan berbasis objek ini, pengelolaan jadwal dan transaksi penyewaan lapangan futsal menjadi lebih terorganisir, mencegah bentrok jadwal, serta memudahkan penyusunan laporan keuangan secara real-time.