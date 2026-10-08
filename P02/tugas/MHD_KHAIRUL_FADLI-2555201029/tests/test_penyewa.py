"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("123456", "Budi", "Kuok")
    assert penyewa.identitas() == "Budi (123456) — Desa Kuok"


def test_kontak_dengan_telepon() -> None:
    penyewa = Penyewa("123456", "Budi", "Kuok", "081234567890")
    assert penyewa.kontak() == "Budi dapat dihubungi di 081234567890"


def test_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("123456", "Budi", "Kuok")
    assert penyewa.kontak() == "Budi belum mencantumkan nomor telepon"