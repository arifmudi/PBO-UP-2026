"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_penyewa_identitas() -> None:
    penyewa = Penyewa("1406012509900001", "Budi Santoso", "Kuok", "0812-3456-7890")
    assert penyewa.identitas() == "Budi Santoso (1406012509900001) — Desa Kuok"


def test_penyewa_kontak_ada_telepon() -> None:
    penyewa = Penyewa("1406012509900001", "Budi Santoso", "Kuok", "0812-3456-7890")
    assert penyewa.kontak() == "Budi Santoso dapat dihubungi di 0812-3456-7890"


def test_penyewa_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("1406012509900002", "Siti Aminah", "Salo")
    assert penyewa.kontak() == "Siti Aminah belum mencantumkan nomor telepon"