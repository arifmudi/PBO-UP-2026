# pbo-sipala-CONTOH — Pertemuan 7

Kode acuan Pertemuan 7 — Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai

## Empat cara memperlakukan hal berbeda secara seragam

| Cara | Dipakai ketika | Berkas |
|---|---|---|
| Polimorfisme lewat pewarisan | Objeknya milik kita, punya induk sama | `src/model/daftar_harga.py` |
| Duck typing | Tidak punya induk sama, tapi methodnya ada | (didemonstrasikan pada `bebek_rapuh.py`) |
| Pernyataan `match` | Yang dibedakan bentuk data/perintah | `src/ui/perintah_konsol.py` |
| `functools.singledispatch` | Tipe argumen bukan milik kita | `src/format_nilai.py` |

`DaftarHarga` tidak memuat satu pun `isinstance`, `type()`, maupun nama kelas
turunan. Menambah jenis alat baru tidak menuntut satu baris pun diubah di sana.

## Tiga gerbang

```
python periksa_pbo.py src --profil p07
python -m mypy
python -m pytest
python -m src.main
```

Keluaran yang diharapkan:

```
LOLOS. Tidak ada pelanggaran disiplin berorientasi objek.
Success: no issues found in 25 source files
73 passed
```

## Dua kesalahan yang sengaja ditanam

**① Rantai percabangan berdasarkan jenis** — `python rantai_if.py`:

```
Alat                     cara lama    polimorfik   status
Traktor                  Rp750.000     Rp750.000   cocok
Pompa                    Rp603.000     Rp603.000   cocok
Perontok                 Rp600.000     Rp600.000   cocok
Penggiling Gabah         Rp360.000     Rp410.000   *** SALAH ***
```

Cabang `else` menangkap jenis baru diam-diam dan menghitungnya dengan rumus
dasar. Tidak ada galat, tidak ada peringatan — hanya angka yang salah. Cabang
`else` itu justru ditulis dengan niat baik, dan niat baik itulah yang
menyembunyikan kesalahannya.

**② Duck typing yang rapuh** — `python bebek_rapuh.py`:

```
Traktor                     Rp750.000
Gerobak Dorong                 RUNTUH   GerobakSewaan.biaya_sewa() takes
                                        1 positional argument but 2 were given
```

### Tiga tingkat penjagaan

| Keadaan | Kapan kesalahan ketahuan | Kelemahannya |
|---|---|---|
| `list[object]` | Saat program dijalankan | Bisa berbulan-bulan kemudian |
| `list[AlatTani]` | mypy, sebelum dijalankan | Kaku: gerobak yang benar pun ditolak |
| **Yang kita butuhkan** | Menuntut kontraknya saja | Belum ada — **Pertemuan 9** |

Percobaan tahap kedua:

```
# ubah  daftar: list[object]  →  daftar: list[AlatTani]
python -m mypy bebek_rapuh.py
→ error: List item 1 has incompatible type "GerobakSewaan";
         expected "AlatTani"  [list-item]
```

## Catatan versi

`pyproject.toml` memakai `python_version = "3.14"`. Sesuaikan pada berkas milik
dosen bila laboratorium memakai versi lain — bukan pada berkas milik mahasiswa.
