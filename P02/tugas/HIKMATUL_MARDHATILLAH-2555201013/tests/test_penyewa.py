"""Pengujian untuk kelas Penyewa."""
from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("123456", "Budi", "Kuok", "08123456789")
    assert penyewa.identitas() == "Budi (123456) — Desa Kuok"


def test_kontak_dengan_nomor() -> None:
    penyewa = Penyewa("123456", "Budi", "Kuok", "08123456789")
    assert penyewa.kontak() == "Budi dapat dihubungi di 08123456789"


def test_kontak_tanpa_nomor() -> None:
    penyewa = Penyewa("123456", "Siti", "Salo")
    assert penyewa.kontak() == "Siti belum mencantumkan nomor telepon"