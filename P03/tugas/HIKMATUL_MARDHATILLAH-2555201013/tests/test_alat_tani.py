"""Pengujian untuk kelas AlatTani."""

from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.keterangan() == "[TR-01] Traktor Roda Dua — Rp150.000/hari"


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)

def test_biaya_sewa_satu_hari() -> None:
    alat = AlatTani("PA-01", "Pompa", 75000)
    assert alat.biaya_sewa(1) == 75000


import pytest


def test_kode_bersifat_baca_saja() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        setattr(alat, "kode", "TR-02")


def test_nama_bersifat_baca_saja() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        setattr(alat, "nama", "Pompa")


def test_tarif_dapat_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    alat.tarif_harian = 200000
    assert alat.tarif_harian == 200000


def test_tarif_nol_ditolak() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = 0


def test_tarif_negatif_ditolak() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5000


def test_tarif_terlalu_tinggi_ditolak() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = 5000001


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Traktor", 150000)


def test_tarif_nol_saat_dibuat_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)
