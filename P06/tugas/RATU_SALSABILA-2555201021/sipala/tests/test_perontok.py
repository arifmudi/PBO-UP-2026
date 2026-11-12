
import pytest

from src.model.perontok import Perontok

def test_perontok_dapat_dibuat() -> None:
    perontok = Perontok("PR001", "Perontok Padi", 50_000, 500)
    assert perontok.kode == "PR001"
    assert perontok.nama == "Perontok Padi"

def test_perontok_minimum_sewa_dua_hari() -> None:
    perontok = Perontok("PR002", "Perontok", 50_000, 500)
    assert perontok.biaya_sewa(1) == 100_000

def test_perontok_sewa_tiga_hari() -> None:
    perontok = Perontok("PR003", "Perontok", 50_000, 500)
    assert perontok.biaya_sewa(3) == 150_000

def test_perontok_dari_baris_csv() -> None:
    perontok = Perontok.dari_baris_csv(
        "PR004;Perontok CSV;50000;500"
    )
    assert perontok.kode == "PR004"
    assert perontok.nama == "Perontok CSV"
    assert perontok.tarif_harian == 50_000

def test_perontok_csv_jumlah_kolom_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR005;Perontok;50000")

def test_perontok_csv_tarif_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR006;Perontok;abc;500")

def test_perontok_csv_kapasitas_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok.dari_baris_csv("PR007;Perontok;50000;abc")

def test_perontok_kapasitas_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok("PR008", "Perontok", 50_000, 0)

def test_perontok_kapasitas_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Perontok("PR009", "Perontok", 50_000, -5)

def test_perontok_jumlah_hari_negatif_ditolak() -> None:
    perontok = Perontok("PR010", "Perontok", 50_000, 500)

    with pytest.raises(ValueError):
        perontok.biaya_sewa(-1)