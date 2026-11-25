# pbo-sipala-CONTOH — Pertemuan 9

Kode acuan Pertemuan 9 — Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai

## Dua cara menuntut kontrak, dipakai bersama

| | `abc.ABC` — nominal | `typing.Protocol` — struktural |
|---|---|---|
| Yang dituntut | Keturunan, ditulis dengan sengaja | Bentuk saja |
| Kapan diperiksa | Saat objek dibuat | Saat mypy dijalankan |
| Keuntungan | Kelalaian mustahil lolos | Menerima kelas dari mana pun |
| Kelemahan | Kaku | Bisa terpenuhi secara kebetulan |
| Di SIPALA | `AlatTani` | `Sewaan` |

## Penataan ulang yang tidak mengubah hasil

Rumus biaya sewa yang sebelumnya tertulis di **tiga tempat** kini hanya ada di
induk dan tidak ditimpa satu pun turunan:

```python
# di AlatTani — tidak ditimpa
def biaya_sewa(self, jumlah_hari: int) -> int:
    hari = self.hari_ditagih(jumlah_hari)
    return self._tarif_harian * hari + self.biaya_tambahan(hari)
```

Turunan hanya mengisi lubangnya:

| Turunan | Mengisi | Isinya |
|---|---|---|
| `Traktor` | `biaya_tambahan()` | ongkos operator × hari |
| `PompaAir` | `biaya_tambahan()` | solar sesuai debit × hari |
| `Perontok` | `biaya_tambahan()` = 0 dan `hari_ditagih()` | kekhasannya pada hari |

Angkanya **sama persis** dengan Pertemuan 7:

```
Traktor   1 hari: Rp250.000   3 hari: Rp750.000
PompaAir  1 hari: Rp201.000   3 hari: Rp603.000
Perontok  1 hari: Rp400.000   3 hari: Rp600.000
```

## Tiga gerbang

```
python periksa_pbo.py src --profil p09
python -m mypy
python -m pytest
python -m src.main
```

Keluaran yang diharapkan:

```
LOLOS. Tidak ada pelanggaran disiplin berorientasi objek.
Success: no issues found in 26 source files
49 passed
```

## Dua kesalahan yang sengaja ditanam

**① Lupa mengisi method wajib** — `python lupa_abstrak.py`:

```
DITOLAK saat objek dibuat:
    Can't instantiate abstract class Penggiling without an implementation
    for abstract method 'syarat_pemakaian'
```

Bandingkan dengan Pertemuan 7: di sana kesalahan serupa baru runtuh ketika
methodnya benar-benar dipanggil. Di sini ditolak saat objek dibuat, dan
pesannya menyebut persis method mana.

**② Kontrak terpenuhi secara kebetulan** — `python kontrak_kebetulan.py`:

```
Karyawan memenuhi kontrak Sewaan? True

   kode         ada? True
   nama         ada? True
   biaya_sewa   ada? True
   keterangan   ada? True
```

`Karyawan` sama sekali bukan barang sewaan — `biaya_sewa()` miliknya
mengembalikan **upah**. Tetapi bentuknya cocok, jadi Protocol menerimanya.
mypy pun tidak berkeberatan. Inilah harga dari kelenturan kontrak struktural.

## Catatan versi

`pyproject.toml` memakai `python_version = "3.14"`. Sesuaikan pada berkas milik
dosen bila laboratorium memakai versi lain — bukan pada berkas milik mahasiswa.
