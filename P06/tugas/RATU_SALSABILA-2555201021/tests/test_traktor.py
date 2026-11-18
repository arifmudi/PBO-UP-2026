
import pytest

from src.model.traktor import Traktor


def test_traktor_dapat_dibuat() -> None:
    traktor = Traktor("TR001", "Traktor Roda Dua", 50_000, 20)
    assert traktor.kode == "TR001"
    assert traktor.nama == "Traktor Roda Dua"


def test_traktor_menghitung_biaya_operator() -> None:
    traktor = Traktor("TR002", "Traktor", 50_000, 20)
    assert traktor.biaya_sewa(2) == 300_000


def test_traktor_dari_baris_csv() -> None:
    traktor = Traktor.dari_baris_csv(
        "TR003;Traktor CSV;50000;20"
    )
    assert traktor.kode == "TR003"
    assert traktor.nama == "Traktor CSV"
    assert traktor.tarif_harian == 50_000


def test_traktor_csv_dengan_jumlah_kolom_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor.dari_baris_csv("TR004;Traktor;50000")


def test_traktor_csv_dengan_tarif_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor.dari_baris_csv("TR005;Traktor;abc;20")


def test_traktor_csv_dengan_tenaga_kuda_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor.dari_baris_csv("TR006;Traktor;50000;abc")


def test_traktor_tenaga_kuda_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor("TR007", "Traktor", 50_000, 0)


def test_traktor_tenaga_kuda_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor("TR008", "Traktor", 50_000, -5)
