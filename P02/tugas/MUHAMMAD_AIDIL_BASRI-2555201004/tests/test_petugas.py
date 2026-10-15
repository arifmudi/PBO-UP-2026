"""Pengujian untuk kelas Petugas."""

from src.model.petugas import Petugas


def test_identitas() -> None:
    petugas = Petugas("PT-01", "Andi", "Ketua")
    assert petugas.identitas() == "Andi (PT-01) — Ketua"


def test_kontak_dengan_telepon() -> None:
    petugas = Petugas("PT-01", "Andi", "Ketua", "08123456789")
    assert petugas.kontak() == "Andi dapat dihubungi di 08123456789"


def test_dua_objek_punya_data_sendiri() -> None:
    andi = Petugas("PT-01", "Andi", "Ketua")
    budi = Petugas("PT-02", "Budi", "Sekretaris")

    assert andi.identitas() != budi.identitas()