import pytest

from src.model.kios import Kios


def test_kios_valid() -> None:
    kios = Kios("BR01", "Beras", 10_000)

    assert kios.kode == "BR01"
    assert kios.nama == "Beras"
    assert kios.harga == 10_000


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("", "Beras", 10_000)


def test_kode_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("   ", "Beras", 10_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR01", "", 10_000)


def test_nama_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR01", "   ", 10_000)


def test_harga_di_bawah_minimum_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR01", "Beras", 500)


def test_harga_di_atas_maksimum_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR01", "Beras", 100_000_001)


def test_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("BR01", "Beras", 10_000.5)  # type: ignore[arg-type]


def test_harga_jual_dengan_margin() -> None:
    kios = Kios("BR01", "Beras", 10_000)

    assert kios.harga_jual() == 11_000


def test_harga_wajar() -> None:
    assert Kios.harga_wajar(10_000) is True
    assert Kios.harga_wajar(500) is False


def test_harga_wajar_menolak_boolean() -> None:
    assert Kios.harga_wajar(True) is False


def test_dari_baris() -> None:
    kios = Kios.dari_baris("BR02;Gula;15000")

    assert kios.kode == "BR02"
    assert kios.nama == "Gula"
    assert kios.harga == 15_000


def test_dari_baris_format_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("BR03;Minyak")


def test_dari_baris_harga_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("BR03;Minyak;mahal")


def test_dari_baris_harga_tidak_wajar_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris("BR03;Minyak;500")


def test_informasi_produk() -> None:
    kios = Kios("BR04", "Beras", 10_000)

    hasil = kios.informasi()

    assert "BR04" in hasil
    assert "Beras" in hasil
    assert "Rp" in hasil


def test_jumlah_produk_bertambah() -> None:
    jumlah_awal = Kios.jumlah_produk()

    Kios("BR05", "Gula", 15_000)

    jumlah_akhir = Kios.jumlah_produk()

    assert jumlah_akhir - jumlah_awal == 1