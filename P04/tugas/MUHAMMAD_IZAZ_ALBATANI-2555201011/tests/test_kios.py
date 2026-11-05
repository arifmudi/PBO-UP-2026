"""Pengujian untuk kelas Kios."""

import pytest
from src.model.kios import Kios


def test_membuat_produk() -> None:
    produk = Kios("BR-01", "Beras", 10_000, 11_000)

    assert produk.kode == "BR-01"
    assert produk.nama_produk == "Beras"
    assert produk.harga_modal == 10_000
    assert produk.harga_jual == 11_000


def test_margin_minimum_diterima() -> None:
    produk = Kios("BR-02", "Beras", 10_000, 11_000)

    assert produk.harga_jual == 11_000


def test_harga_jual_di_bawah_margin_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-03", "Beras", 10_000, 10_500)


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("", "Beras", 10_000, 11_000)


def test_nama_produk_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-04", "", 10_000, 11_000)


def test_harga_modal_di_bawah_batas_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-05", "Gula", 500, 1_000)


def test_harga_jual_melebihi_batas_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-06", "Minyak", 1_000, 10_000_001)


def test_dari_baris() -> None:
    produk = Kios.dari_baris("BR-07;Gula;12.000;13.200")

    assert produk.kode == "BR-07"
    assert produk.nama_produk == "Gula"
    assert produk.harga_modal == 12_000
    assert produk.harga_jual == 13_200


def test_format_baris_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("BR-08;Gula;12000")


def test_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("BR-09;Gula;modal;13200")


def test_nilai_jual() -> None:
    produk = Kios("BR-10", "Minyak", 10_000, 12_000)

    assert produk.nilai_jual(3) == 36_000


def test_jumlah_nol_ditolak() -> None:
    produk = Kios("BR-11", "Minyak", 10_000, 12_000)

    with pytest.raises(ValueError):
        produk.nilai_jual(0)


def test_keuntungan() -> None:
    produk = Kios("BR-12", "Beras", 10_000, 12_000)

    assert produk.keuntungan(3) == 6_000


def test_format_rupiah() -> None:
    assert Kios.format_rupiah(150_000) == "Rp150.000"


def test_harga_wajar() -> None:
    assert Kios.harga_wajar(10_000, 11_000) is True
    assert Kios.harga_wajar(10_000, 10_000) is False


def test_counter_menggunakan_delta() -> None:
    awal = Kios.jumlah_produk()

    Kios("BR-13", "Gula", 10_000, 11_000)

    akhir = Kios.jumlah_produk()

    assert akhir - awal == 1
