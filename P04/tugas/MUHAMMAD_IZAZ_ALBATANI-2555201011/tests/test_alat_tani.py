"""Pengujian untuk kelas AlatTani."""

import pytest
from src.model.alat_tani import AlatTani


def test_tarif_wajar_dipanggil_tanpa_objek() -> None:
    assert AlatTani.tarif_wajar(150000) is True
    assert AlatTani.tarif_wajar(6000000) is False


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150000) == "Rp150.000"


def test_pencacah_naik_dua_alat() -> None:
    awal = AlatTani.jumlah_terdaftar()

    AlatTani("TR-90", "Traktor Uji", 100000)
    AlatTani("TR-91", "Traktor Uji", 100000)

    assert AlatTani.jumlah_terdaftar() == awal + 2


def test_konstruktor_dari_baris_csv() -> None:
    alat = AlatTani.dari_baris_csv("PA-01;Pompa Air;75000")

    assert alat.kode == "PA-01"
    assert alat.nama == "Pompa Air"
    assert alat.tarif_harian == 75000


def test_baris_csv_tarif_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air;tujuh puluh lima ribu")


def test_baris_csv_bagian_kurang_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air")


def test_baris_csv_bagian_lebih_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("PA-01;Pompa Air;75000;Tambahan")


def test_biaya_sewa() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_denda_keterlambatan() -> None:
    alat = AlatTani("TR-02", "Traktor", 150000)
    assert alat.denda_keterlambatan(2) == 30000


def test_denda_hari_negatif_ditolak() -> None:
    alat = AlatTani("TR-03", "Traktor", 150000)

    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)
