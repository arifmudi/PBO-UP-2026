"""Pengujian alternatif untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_identitas_desa_panjang() -> None:
    petani = Penyewa("1406012509901111", "Joko Widodo", "Tanjung Belit Selatan")
    assert petani.identitas() == "Joko Widodo (1406012509901111) — Desa Tanjung Belit Selatan"


def test_kontak_default_parameter() -> None:
    petani = Penyewa("1406012509902222", "Maimunah", "Salo")
    assert petani.kontak() == "Maimunah belum mencantumkan nomor telepon"


def test_kontak_format_kode_negara() -> None:
    petani = Penyewa("1406012509903333", "Rudi", "Bangkinang", "+62 811-2222-3333")
    assert petani.kontak() == "Rudi dapat dihubungi di +62 811-2222-3333"