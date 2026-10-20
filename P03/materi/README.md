# pbo-sipala-CONTOH — Pertemuan 3

Kode acuan Pertemuan 3 — Pemrograman Berorientasi Objek
Prodi Teknik Informatika, Fakultas Teknik, Universitas Pahlawan Tuanku Tambusai

## Tiga tingkat penjagaan yang diterapkan

| Tingkat | Berkas | Contoh |
|---|---|---|
| Baca-saja | `alat_tani.py`, `penyewa.py` | `kode`, `nama`, `nik` — divalidasi di konstruktor, tanpa setter |
| Baca-tulis terjaga | `alat_tani.py`, `penyewa.py` | `tarif_harian`, `telepon` — setter bervalidasi |
| Beku seluruhnya | `alamat.py` | `Alamat` — `@dataclass(frozen=True)` + `__post_init__` |

## Isi

| Berkas | Keterangan |
|---|---|
| `src/model/alamat.py` | Objek nilai beku. Validasi di `__post_init__`. |
| `src/model/alat_tani.py` | Property baca-saja untuk kode dan nama; setter bervalidasi untuk tarif. |
| `src/model/penyewa.py` | NIK baca-saja (16 digit), telepon bersetter, menyimpan objek `Alamat`. |
| `src/main.py` | Titik masuk; memuat percobaan menembus penjagaan. |
| `tests/` | 15 fungsi uji, 10 di antaranya membuktikan penolakan. |
| `konstruktor_bocor.py` | **Sengaja salah.** Kesalahan yang ditanam nomor 1 (Langkah 4). |

## Tiga gerbang

```
python periksa_pbo.py src --profil p03
python -m mypy
python -m pytest
python -m src.main
```

Keluaran yang diharapkan:

```
LOLOS. Tidak ada pelanggaran disiplin berorientasi objek.
Success: no issues found in 10 source files
15 passed

--- Percobaan menembus penjagaan ---
Ditolak (tarif nol): tarif harus lebih dari nol, diterima 0
Ditolak (tarif minus): tarif harus lebih dari nol, diterima -5000
Tarif tetap utuh: [TR-01] Traktor Roda Dua Kubota — Rp150.000/hari
```

## Dua kesalahan yang sengaja ditanam

**① Konstruktor melewati penjaga** — `python konstruktor_bocor.py`:

```
Tarif   : -5000          ← masuk lewat konstruktor, tanpa keluhan
3 hari  : -15000
Setter menolak: tarif harus lebih dari nol, diterima -9000   ← setter BEKERJA
```

Setter-nya benar. Validasinya benar. Konstruktor tidak memanggilnya, jadi objek
lahir dalam keadaan tidak valid. Bedanya satu karakter: `self._tarif_harian`
versus `self.tarif_harian`.

**② Garis bawah ganda bukan kunci**:

```
python -c "
class Dompet:
    def __init__(self, saldo: int) -> None:
        self.__saldo = saldo
d = Dompet(100000)
d._Dompet__saldo = -1        # BERHASIL
print(list(vars(d)))         # ['_Dompet__saldo']
"
```

Python mengganti nama, bukan mengunci. Yang menjaga kode adalah setter yang
selalu dilewati, pengujian yang membuktikan penolakan, dan tinjauan kode.

## Catatan versi

`pyproject.toml` memakai `python_version = "3.14"`. Sesuaikan pada berkas milik
dosen bila laboratorium memakai versi lain — bukan pada berkas milik mahasiswa.
