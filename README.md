# PBO-UP-2026 — Kelas A

Praktikum Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai — 2026/2027

## Jadwal dan tenggat

Setiap tugas berjalan **1 minggu** sejak LKM dibagikan.

| Tugas | Mulai | Tenggat (Pull Request sudah dibuat) |
|---|---|---|
| P01 — Lingkungan kerja dan tiga gerbang | Kamis, 24 September 2026 | Rabu, 30 September 2026, pukul 23.59 WIB (sudah lewat) |
| P02 — Kelas `Penyewa` dan `AlatTani` | Kamis, 1 Oktober 2026 | Rabu, 7 Oktober 2026, pukul 23.59 WIB (sudah lewat) |
| P03 — Enkapsulasi: property, setter, objek nilai `Alamat` | Kamis, 15 Oktober 2026 | **Rabu, 21 Oktober 2026, pukul 23.59 WIB** |

Tugas terstruktur P03 ada di `P03/materi/Panduan-Praktikum-P03.pdf` bagian 7: perbaiki kelas `Petugas`
dari tugas P02 (property baca-saja, setter bervalidasi, objek nilai beku rancanganmu sendiri, minimal
enam uji dengan empat `pytest.raises`). Gerbang memakai profil `p03`; tanda versi `p03-tugas`.

Keterlambatan dihitung dari **waktu Pull Request dibuat** (dicatat GitHub) dan dikurangi
**5 poin per hari**. Commit di fork saja belum dihitung mengumpulkan — buat PR-nya sebelum tenggat.

## Struktur repo

```text
P01/
├── materi/                     dari dosen — JANGAN diubah
│   ├── Panduan-Praktikum-P01.pdf  langkah praktikum dan TUGAS (lihat bagian 6)
│   ├── LKM-P01.pdf             Lembar Kerja Mahasiswa (dicetak/diisi saat praktikum)
│   ├── README.md               langkah praktikum dan tiga gerbang
│   ├── periksa_pbo.py
│   ├── pyproject.toml
│   ├── AI_USAGE.md             contoh pengisian
│   └── salah_prosedural.py
└── tugas/
    └── NAMA_LENGKAP-NIM/       satu folder per mahasiswa
        ├── src/
        ├── tests/
        ├── periksa_pbo.py      salinan dari materi, tidak diubah
        ├── pyproject.toml      salinan dari materi, tidak diubah
        ├── REFLEKSI.md
        ├── LKM-P01.pdf         LKM yang sudah diisi (diunggah dosen)
        └── AI_USAGE.md         WAJIB, termasuk bila tidak memakai AI
P02/
└── ...
P03/
├── materi/                     Panduan, LKM, README, periksa_pbo.py, pyproject.toml, konstruktor_bocor.py
└── tugas/NAMA_LENGKAP-NIM/     src/, tests/, periksa_pbo.py, pyproject.toml, AI_USAGE.md, REFLEKSI.md
```

## Cara mengumpulkan tugas

1. **Fork** repo ini (sekali saja). Sebelum mulai pertemuan baru, klik **Sync fork**
   di halaman fork-mu agar materi terbaru ikut masuk.
2. Buat foldermu di `P0x/tugas/NAMA_LENGKAP-NIM/`.
   - Huruf kapital, kata dipisah garis bawah, tanpa titik.
   - Contoh benar: `P02/tugas/BUDI_SANTOSO-2555201000/`
   - Contoh salah: `budi santoso`, `BUDISANTOSO-2555201000`, `MHD._BUDI-2555201000`
3. Salin `periksa_pbo.py` dan `pyproject.toml` dari `P0x/materi/` ke foldermu **tanpa diubah**.
4. Kerjakan, lalu jalankan tiga gerbang dari dalam foldermu sampai semuanya lolos
   (perintahnya ada di `P0x/materi/README.md`).
5. Isi `REFLEKSI.md` dan `AI_USAGE.md`. Memakai AI tidak otomatis mengurangi nilai;
   **tidak jujur** tentang pemakaiannya yang mengurangi nilai.
6. Commit, push ke fork-mu, lalu buat **Pull Request** ke repo ini dengan judul
   `P0x - NAMA LENGKAP (NIM)`.

### Aturan Pull Request

- Satu PR = satu pertemuan = satu folder milikmu sendiri.
- Jangan mengubah berkas di luar foldermu (materi, folder teman, README ini).
- Setelah PR dibuat, pemeriksaan otomatis berjalan. Lihat hasilnya di bagian bawah PR:
  ✅ berarti lolos, ❌ berarti ada yang harus diperbaiki. Perbaiki di fork-mu lalu push lagi;
  PR yang sama otomatis diperbarui, tidak perlu membuat PR baru.
- PR **tidak di-merge** lewat tombol. Dosen memasukkan tugasmu ke repo ini lalu menutup PR
  dengan komentar "diterima". PR yang ditutup dengan komentar itu artinya tugasmu sudah masuk
  dan dinilai.
