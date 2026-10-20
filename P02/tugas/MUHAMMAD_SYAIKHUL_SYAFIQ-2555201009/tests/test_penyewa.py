"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok")
    assert penyewa.identitas() == "Budi (123) — Desa Kuok"


def test_kontak_dengan_nomor() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok", "081234567890")
    assert penyewa.kontak() == "Budi dapat dihubungi di 081234567890"


def test_kontak_tanpa_nomor() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok")
    assert penyewa.kontak() == "Budi belum mencantumkan nomor telepon"