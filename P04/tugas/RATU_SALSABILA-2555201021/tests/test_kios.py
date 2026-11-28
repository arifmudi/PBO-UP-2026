"""Pengujian untuk kelas Kios."""

import pytest

from src.model.kios import Kios


def test_data_produk_dapat_dibaca() -> None:
    produk = Kios("BR-01", "Beras", 10000, 12000, 20)
    assert produk.kode == "BR-01"
    assert produk.nama == "Beras"
    assert produk.harga_beli == 10000
    assert produk.harga_jual == 12000
    assert produk.stok == 20


def test_keterangan_produk() -> None:
    produk = Kios("BR-01", "Beras", 10000, 12000, 20)
    assert "[BR-01] Beras" in produk.keterangan()


def test_harga_jual_wajar() -> None:
    assert Kios.harga_jual_wajar(10000, 12000)


def test_harga_jual_tidak_wajar() -> None:
    assert not Kios.harga_jual_wajar(10000, 11000)


def test_format_rupiah() -> None:
    assert Kios.format_rupiah(15000) == "Rp15.000"


def test_dari_baris_csv() -> None:
    produk = Kios.dari_baris_csv("BR-02;Beras Merah;15000;18000;10")
    assert produk.kode == "BR-02"
    assert produk.nama == "Beras Merah"
    assert produk.stok == 10


def test_baris_daftar_memuat_data_produk() -> None:
    produk = Kios("GL-01", "Gula", 12000, 15000, 8)
    hasil = produk.baris_daftar()
    assert "GL-01" in hasil
    assert "Gula" in hasil
    assert "Rp15.000" in hasil


def test_jumlah_terdaftar_bertambah() -> None:
    jumlah_awal = Kios.jumlah_terdaftar()
    Kios("BR-03", "Beras Pulen", 10000, 12000, 5)
    assert Kios.jumlah_terdaftar() == jumlah_awal + 1


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("", "Beras", 10000, 12000, 20)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-01", "", 10000, 12000, 20)


def test_harga_beli_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-01", "Beras", 500, 12000, 20)


def test_harga_jual_tidak_wajar_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-01", "Beras", 10000, 11000, 20)


def test_stok_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR-01", "Beras", 10000, 12000, -1)


def test_baris_csv_tidak_lengkap_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("BR-01;Beras;10000")


def test_baris_csv_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("BR-01;Beras;abc;12000;20")
