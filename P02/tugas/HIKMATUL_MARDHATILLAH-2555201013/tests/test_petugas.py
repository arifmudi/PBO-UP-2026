"""Pengujian untuk model Petugas."""

from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    """Memastikan identitas petugas dikembalikan dengan benar."""
    petugas = Petugas("PT-01", "Budi", "Admin", "08123456789")

    assert petugas.identitas() == "Budi (PT-01) - Admin"


def test_kontak_petugas_tanpa_nomor() -> None:
    """Memastikan kontak default digunakan jika nomor tidak diberikan."""
    petugas = Petugas("PT-02", "Siti", "Operator")

    assert petugas.kontak() == "Siti belum mencantumkan nomor telepon"


def test_dua_petugas_menyimpan_data_masing_masing() -> None:
    """Memastikan data setiap objek petugas tidak tercampur."""
    petugas1 = Petugas("PT-01", "Budi", "Admin")
    petugas2 = Petugas("PT-02", "Siti", "Operator")

    assert petugas1.identitas() == "Budi (PT-01) - Admin"
    assert petugas2.identitas() == "Siti (PT-02) - Operator"