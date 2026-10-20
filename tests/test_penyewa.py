
"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_identitas_memuat_nama() -> None:
    penyewa = Penyewa("123", "Ratu Salsabila", "Kumantan")
    assert "Ratu Salsabila" in penyewa.identitas()


def test_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("123", "Nayla Wikhsa", "Uway")
    assert "belum mencantumkan nomor telepon" in penyewa.kontak()


def test_kontak_dengan_telepon() -> None:
    penyewa = Penyewa("123", "Ratu Salsabila", "Kumantan", "081234567890")
    assert "081234567890" in penyewa.kontak()
