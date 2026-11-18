
"""Pengujian untuk kelas PompaAir."""

import pytest

from src.model.pompa_air import PompaAir


def test_pompa_air_dapat_dibuat() -> None:
    pompa = PompaAir("PA001", "Pompa Air", 50_000, 600)

    assert pompa.kode == "PA001"
    assert pompa.nama == "Pompa Air"
    assert pompa.tarif_harian == 50_000


def test_pompa_air_menghitung_konsumsi_solar() -> None:
    pompa = PompaAir("PA002", "Pompa Air", 50_000, 600)

    assert pompa.konsumsi_solar_harian() == 18


def test_pompa_air_menghitung_biaya_berdasarkan_debit() -> None:
    pompa = PompaAir("PA003", "Pompa Air", 50_000, 600)

    assert pompa.biaya_sewa(2) == 352_000


def test_pompa_air_dari_baris_csv() -> None:
    pompa = PompaAir.dari_baris_csv(
        "PA004;Pompa CSV;50000;600"
    )

    assert pompa.kode == "PA004"
    assert pompa.nama == "Pompa CSV"
    assert pompa.tarif_harian == 50_000
    assert pompa.konsumsi_solar_harian() == 18


def test_pompa_air_csv_jumlah_kolom_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA005;Pompa;50000")


def test_pompa_air_csv_tarif_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA006;Pompa;abc;600")


def test_pompa_air_csv_debit_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir.dari_baris_csv("PA007;Pompa;50000;abc")


def test_pompa_air_debit_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA008", "Pompa", 50_000, 0)


def test_pompa_air_debit_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA009", "Pompa", 50_000, -5)
