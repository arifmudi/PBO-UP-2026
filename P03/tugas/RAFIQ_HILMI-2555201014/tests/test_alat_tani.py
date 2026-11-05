
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


def test_keterangan() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)

    assert alat.keterangan() == "[TR-01] Traktor Roda Dua — Rp150.000/hari"


def test_kode_hanya_bisa_dibaca() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    with pytest.raises(AttributeError):
        alat.kode = "TR-02"  # type: ignore[misc]


def test_nama_hanya_bisa_dibaca() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    with pytest.raises(AttributeError):
        alat.nama = "Traktor Baru"  # type: ignore[misc]


def test_tarif_nol_ditolak_saat_dibuat() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_tarif_negatif_ditolak_saat_dibuat() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -1000)


def test_tarif_negatif_ditolak_saat_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    with pytest.raises(ValueError):
        alat.tarif_harian = -5000

    assert alat.tarif_harian == 150000


def test_tarif_nol_ditolak_saat_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    with pytest.raises(ValueError):
        alat.tarif_harian = 0

    assert alat.tarif_harian == 150000


def test_tarif_valid_bisa_diubah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    alat.tarif_harian = 200000

    assert alat.tarif_harian == 200000


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Traktor", 150000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "", 150000)

def test_tarif_di_atas_batas_maksimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 5_000_001)
