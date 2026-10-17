"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_identitas() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok")
    assert penyewa.identitas() == "Budi (123) — Desa Kuok"


def test_kontak_dengan_telepon() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok", "08123456789")
    assert penyewa.kontak() == "Budi dapat dihubungi di 08123456789"


def test_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok")
    assert penyewa.kontak() == "Budi belum mencantumkan nomor telepon"


def test_dua_objek_punya_data_sendiri() -> None:
    budi = Penyewa("123", "Budi", "Kuok")
    siti = Penyewa("456", "Siti", "Salo")
    assert budi.identitas() != siti.identitas()