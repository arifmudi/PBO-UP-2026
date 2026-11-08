"""Tes untuk model AlatTani pada P03."""

import pytest

from src.model.alat_tani import AlatTani


def test_biaya_sewa() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_keterangan_rupiah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.keterangan() == "[TR-01] Traktor — Rp150.000/hari"


def test_biaya_sewa_nol_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(0) == 0


def test_setiap_objek_independen() -> None:
    traktor = AlatTani("TR-01", "Traktor", 150000)
    pompa = AlatTani("PM-01", "Pompa", 75000)
    assert traktor.biaya_sewa(1) == 150000
    assert pompa.biaya_sewa(1) == 75000


def test_properti_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.kode == "TR-01"
    assert alat.nama == "Traktor"
    assert alat.tarif_harian == 150000


def test_tarif_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    alat.tarif_harian = 200000
    assert alat.tarif_harian == 200000


@pytest.mark.parametrize("tarif", [0, -1, -100])
def test_tarif_tidak_valid(tarif: int) -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", tarif)


def test_tarif_melebihi_batas() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5_000_001)


def test_kode_harus_diisi() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Traktor", 150000)


def test_kode_tidak_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-02"  # type: ignore[misc]


def test_nama_tidak_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.nama = "Pompa"  # type: ignore[misc]