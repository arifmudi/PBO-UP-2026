
"""Pengujian untuk kelas Petugas."""

from src.model.petugas import Petugas


def test_identitas_memuat_nama() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "Kumantan")
    assert "Andi" in petugas.identitas()


def test_wilayah_tugas() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "Kumantan")
    assert "Kumantan" in petugas.wilayah_tugas()


def test_data_setiap_petugas_independen() -> None:
    petugas1 = Petugas("PT-01", "Andi", "Admin", "Kumantan")
    petugas2 = Petugas("PT-02", "Budi", "Operator", "Kuok")

    assert "Andi" in petugas1.identitas()
    assert "Budi" in petugas2.identitas()
    assert "Kumantan" in petugas1.wilayah_tugas()
    assert "Kuok" in petugas2.wilayah_tugas()
