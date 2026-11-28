import pytest

from src.model.alat_tani import AlatTani


# ==================================================
# PENGUJIAN DASAR ALAT TANI
# ==================================================

def test_alat_tani_valid() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    assert alat.kode == "AT01"
    assert alat.nama == "Traktor"
    assert alat.tarif_harian == 100000


def test_kode_read_only() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    with pytest.raises(AttributeError):
        alat.kode = "AT02"  # type: ignore[misc]


def test_nama_read_only() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    with pytest.raises(AttributeError):
        alat.nama = "Mesin"  # type: ignore[misc]


# ==================================================
# PENGUJIAN TARIF HARIAN
# ==================================================

def test_tarif_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("AT01", "Traktor", 0)


def test_tarif_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("AT01", "Traktor", -1000)


def test_tarif_terlalu_besar_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("AT01", "Traktor", 5_000_001)


def test_tarif_bisa_diubah_valid() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    alat.tarif_harian = 200000
    assert alat.tarif_harian == 200000


def test_tarif_baru_nol_ditolak() -> None:
    alat = AlatTani("AT01", "Traktor", 100000)
    with pytest.raises(ValueError):
        alat.tarif_harian = 0


# ==================================================
# PENGUJIAN STATICMETHOD
# ==================================================

def test_tarif_wajar_valid() -> None:
    assert AlatTani.tarif_wajar(100000) is True


def test_tarif_wajar_batas_minimum() -> None:
    assert AlatTani.tarif_wajar(AlatTani.TARIF_MINIMUM) is True


def test_tarif_wajar_batas_maksimum() -> None:
    assert AlatTani.tarif_wajar(AlatTani.TARIF_MAKSIMUM) is True


def test_tarif_wajar_di_bawah_minimum() -> None:
    assert AlatTani.tarif_wajar(9999) is False


def test_tarif_wajar_di_atas_maksimum() -> None:
    assert AlatTani.tarif_wajar(5_000_001) is False


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(100000) == "Rp100.000"


def test_format_rupiah_jutaan() -> None:
    assert AlatTani.format_rupiah(1500000) == "Rp1.500.000"


# ==================================================
# PENGUJIAN CLASSMETHOD
# ==================================================

def test_jumlah_terdaftar() -> None:
    awal = AlatTani.jumlah_terdaftar()
    AlatTani("AT02", "Traktor", 100000)
    assert AlatTani.jumlah_terdaftar() == awal + 1


def test_dari_baris_csv_valid() -> None:
    alat = AlatTani.dari_baris_csv("AT03;Traktor;100000")
    assert alat.kode == "AT03"
    assert alat.nama == "Traktor"
    assert alat.tarif_harian == 100000


def test_dari_baris_csv_bagian_tidak_valid() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("AT03;Traktor")


def test_dari_baris_csv_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("AT03;Traktor;mahal")


# ==================================================
# PENGUJIAN DENDA KETERLAMBATAN
# ==================================================

def test_denda_keterlambatan() -> None:
    alat = AlatTani("AT04", "Traktor", 100000)
    assert alat.denda_keterlambatan(2) == 20000


def test_denda_nol_hari() -> None:
    alat = AlatTani("AT05", "Traktor", 100000)
    assert alat.denda_keterlambatan(0) == 0


def test_denda_hari_negatif_ditolak() -> None:
    alat = AlatTani("AT06", "Traktor", 100000)
    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)