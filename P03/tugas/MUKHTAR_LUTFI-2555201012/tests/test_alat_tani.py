"""Pengujian untuk kelas AlatTani."""

from src.model.alat_tani import AlatTani

def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000
def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)

def test_inisialisasi_atribut() -> None:
    alat = AlatTani("CT-05", "Cultivator", 200000)
    assert alat._kode == "CT-05"
    assert alat._nama == "Cultivator"
    assert alat._tarif_harian == 200000

def test_keterangan_format_tarif_berbeda() -> None:
    alat = AlatTani("TR-03", "Traktor Roda Empat", 1250000)
    assert alat.keterangan() == "[TR-03] Traktor Roda Empat — Rp1.250.000/hari"

import pytest


def test_tarif_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_tarif_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -1000)


def test_tarif_melebihi_batas_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5_000_001)


def test_tarif_bukan_bilangan_bulat_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 150000.5)  # type: ignore[arg-type]


def test_kode_tidak_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-02"  # type: ignore[misc]


def test_nama_tidak_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.nama = "Pompa"  # type: ignore[misc]
