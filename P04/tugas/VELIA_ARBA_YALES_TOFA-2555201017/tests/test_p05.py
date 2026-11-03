from __future__ import annotations
import sys
import os
import pytest

# Menambahkan direktori tugas ke sys.path secara aman
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.model.alat_tani import AlatTani
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa
from src.model.baris_sewa import BarisSewa
from src.model.sewa import Sewa

def buat_penyewa() -> Penyewa:
    alamat = Alamat("Kuok", "Kuok", "Kampar")
    # Urutan parameter yang benar: Penyewa(nik, nama, alamat)
    return Penyewa("1406012509900001", "Budi Santoso", alamat)

def test_salinan_tidak_ikut_berubah_saat_tarif_alat_naik() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)
    alat.tarif_harian = 175_000
    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 450_000

def test_komposisi_tidak_dapat_dibongkar_dari_luar() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(AlatTani("TR-01", "Traktor", 150_000), 3)
    with pytest.raises(AttributeError):
        sewa.baris.append(None)  # type: ignore[attr-defined]
    assert sewa.jumlah_alat() == 1

def test_penyewa_tetap_hidup_setelah_sewa_dihapus() -> None:
    budi = buat_penyewa()
    sewa = Sewa("SW-001", budi)
    del sewa
    assert budi.nama == "Budi Santoso"