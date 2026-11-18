
"""Pengujian untuk kelas BarisSewa."""

import pytest

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.traktor import Traktor


def test_baris_sewa_dapat_dibuat() -> None:
    alat = AlatTani("AT01", "Alat Tani", 100_000)
    baris = BarisSewa(alat, 2)

    assert baris.alat is alat
    assert baris.jumlah_hari == 2
    assert baris.kode_alat == "AT01"
    assert baris.nama_alat == "Alat Tani"
    assert baris.tarif_saat_sewa == 100_000


def test_subtotal_menghitung_tarif_dasar() -> None:
    alat = AlatTani("AT02", "Alat Tani", 100_000)
    baris = BarisSewa(alat, 2)

    assert baris.subtotal() == 200_000


def test_subtotal_memakai_biaya_subclass() -> None:
    traktor = Traktor("TR01", "Traktor", 150_000, 8)
    baris = BarisSewa(traktor, 1)

    assert baris.subtotal() == 250_000


def test_baris_nota_menampilkan_subtotal() -> None:
    traktor = Traktor("TR02", "Traktor", 150_000, 8)
    baris = BarisSewa(traktor, 1)

    assert "Rp150.000" in baris.baris_nota()
    assert "Rp250.000" in baris.baris_nota()


def test_jumlah_hari_nol_ditolak() -> None:
    alat = AlatTani("AT03", "Alat Tani", 100_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, 0)


def test_jumlah_hari_negatif_ditolak() -> None:
    alat = AlatTani("AT04", "Alat Tani", 100_000)

    with pytest.raises(ValueError):
        BarisSewa(alat, -1)
