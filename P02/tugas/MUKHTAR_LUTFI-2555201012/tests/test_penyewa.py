"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("1406012509900001", "Budi Santoso", "Kuok", "0812-3456-7890")
    assert penyewa.identitas() == "Budi Santoso (1406012509900001) — Desa Kuok"


def test_kontak_dengan_telepon() -> None:
    penyewa = Penyewa("1406012509900001", "Budi Santoso", "Kuok", "0812-3456-7890")
    assert penyewa.kontak() == "Budi Santoso dapat dihubungi di 0812-3456-7890"


def test_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("1406014403950002", "Siti Aminah", "Salo")
    assert penyewa.kontak() == "Siti Aminah belum mencantumkan nomor telepon"


def test_dua_penyewa_data_mandiri() -> None:
    budi = Penyewa("1406012509900001", "Budi Santoso", "Kuok", "0812-3456-7890")
    siti = Penyewa("1406014403950002", "Siti Aminah", "Salo")
    assert budi.kontak() != siti.kontak()