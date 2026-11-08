"""Pengujian untuk kelas AlatTani dan Alamat."""
import dataclasses
import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert "TR-01" in alat.keterangan()
    assert "Traktor" in alat.keterangan()


def test_biaya_sewa_nol_hari() -> None:
    alat = AlatTani("PA-01", "Pompa Air", 75000)
    assert alat.biaya_sewa(0) == 0


def test_tarif_minus_ditolak_sejak_konstruktor() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_tarif_minus_ditolak_lewat_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5000
    assert alat.tarif_harian == 150000  # Nilai lama tetap utuh[cite: 18]


def test_kode_tidak_punya_setter() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-99"  # type: ignore


def test_alamat_tidak_dapat_diubah() -> None:
    a = Alamat("Pulau Jambu", "Kuok", "Kuok")
    with pytest.raises(dataclasses.FrozenInstanceError):
        a.desa = "Salo"  # type: ignore