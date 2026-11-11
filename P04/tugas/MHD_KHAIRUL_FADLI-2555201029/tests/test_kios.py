
"""Pengujian untuk model Kios."""

import pytest
from src.model.kios import Kios


def test_membuat_produk_dengan_data_valid() -> None:
    """Produk dapat dibuat dengan data yang benar."""
    produk = Kios("P001", "Beras", 10_000, 11_000, 20)

    assert produk.kode == "P001"
    assert produk.nama == "Beras"
    assert produk.harga_modal == 10_000
    assert produk.harga_jual == 11_000
    assert produk.stok == 20


def test_pencacah_produk_bertambah_satu() -> None:
    """Pencacah bertambah satu setiap produk berhasil dibuat."""
    jumlah_awal = Kios.jumlah_produk_terdaftar()

    Kios("P002", "Gula", 12_000, 13_200, 15)

    jumlah_akhir = Kios.jumlah_produk_terdaftar()

    assert jumlah_akhir - jumlah_awal == 1


def test_harga_wajar_menerima_margin_minimum() -> None:
    """Harga jual dengan margin minimum diterima."""
    assert Kios.harga_wajar(10_000, 11_000) is True


def test_harga_wajar_menolak_margin_di_bawah_minimum() -> None:
    """Harga jual dengan margin kurang dari minimum ditolak."""
    assert Kios.harga_wajar(10_000, 10_999) is False


def test_membuat_produk_dari_baris_teks() -> None:
    """Produk dapat dibuat menggunakan konstruktor alternatif."""
    produk = Kios.dari_baris("P003;Minyak Goreng;15000;16500;10")

    assert produk.kode == "P003"
    assert produk.nama == "Minyak Goreng"
    assert produk.harga_modal == 15_000
    assert produk.harga_jual == 16_500
    assert produk.stok == 10


def test_format_laporan_produk() -> None:
    """Laporan produk menampilkan informasi dengan format rapi."""
    produk = Kios("P004", "Beras", 10_000, 11_000, 20)
    laporan = produk.format_laporan()

    assert "P004" in laporan
    assert "Beras" in laporan
    assert "Rp" in laporan
    assert "11.000" in laporan
    assert "20 unit" in laporan


def test_menolak_kode_produk_kosong() -> None:
    """Kode produk tidak boleh kosong."""
    with pytest.raises(ValueError, match="Kode produk"):
        Kios("", "Beras", 10_000, 11_000, 20)


def test_menolak_nama_produk_kosong() -> None:
    """Nama produk tidak boleh kosong."""
    with pytest.raises(ValueError, match="Nama produk"):
        Kios("P005", "", 10_000, 11_000, 20)


def test_menolak_harga_modal_nol() -> None:
    """Harga modal harus lebih dari nol."""
    with pytest.raises(ValueError, match="Harga modal"):
        Kios("P006", "Beras", 0, 11_000, 20)


def test_menolak_harga_jual_di_bawah_margin() -> None:
    """Harga jual tidak boleh kurang dari margin minimum."""
    with pytest.raises(ValueError, match="margin minimum"):
        Kios("P007", "Beras", 10_000, 10_999, 20)


def test_menolak_stok_negatif() -> None:
    """Stok produk tidak boleh bernilai negatif."""
    with pytest.raises(ValueError, match="Stok"):
        Kios("P008", "Beras", 10_000, 11_000, -1)


def test_menolak_baris_dengan_jumlah_kolom_salah() -> None:
    """Baris teks harus memiliki lima bagian."""
    with pytest.raises(ValueError, match="Baris harus berisi"):
        Kios.dari_baris("P009;Beras;10000;11000")


def test_menolak_harga_modal_bukan_angka() -> None:
    """Harga modal dari baris teks harus berupa angka."""
    with pytest.raises(ValueError, match="Harga modal harus berupa angka"):
        Kios.dari_baris("P010;Beras;sepuluh ribu;11000;20")


def test_menolak_harga_jual_bukan_angka() -> None:
    """Harga jual dari baris teks harus berupa angka."""
    with pytest.raises(ValueError, match="Harga jual harus berupa angka"):
        Kios.dari_baris("P011;Beras;10000;sebelas ribu;20")


def test_menolak_stok_bukan_angka() -> None:
    """Stok dari baris teks harus berupa angka."""
    with pytest.raises(ValueError, match="Stok harus berupa angka"):
        Kios.dari_baris("P012;Beras;10000;11000;banyak")
