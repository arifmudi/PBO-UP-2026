
"""Pengujian untuk kelas AlatTani."""

import pytest

from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)
    assert alat.keterangan() == "[TR-01] Traktor Roda Dua Kubota — Rp150.000/hari"


def test_biaya_sewa_satu_hari() -> None:
    alat = AlatTani("PA-01", "Pompa Air 3 Inci", 75000)
    assert alat.biaya_sewa(1) == 75000


def test_kode_baca_saja() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.kode == "TR-01"
    with pytest.raises(AttributeError):
        alat.kode = "TR-02"  # type: ignore[misc]


def test_nama_baca_saja() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.nama == "Traktor"
    with pytest.raises(AttributeError):
        alat.nama = "Pompa"  # type: ignore[misc]


def test_tarif_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_tarif_minus_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -5000)


def test_tarif_di_atas_batas_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5_000_001)


def test_setter_tarif_tidak_mengubah_nilai_jika_ditolak() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(ValueError):
        alat.tarif_harian = -5000
    assert alat.tarif_harian == 150000


def test_setter_tarif_menerima_nilai_valid() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    alat.tarif_harian = 200000
    assert alat.tarif_harian == 200000
