"""Pengujian untuk kelas Mahasiswa."""

from src.mahasiswa import Mahasiswa


def test_perkenalan_memuat_nama() -> None:
    saya = Mahasiswa("Ratu Salsabila", "2555201021", "Kumantan")
    assert "Ratu Salsabila" in saya.perkenalan()


def test_atribut_dibaca_lewat_property() -> None:
    saya = Mahasiswa("Ratu Salsabila", "2555201021", "Kumantan")
    assert saya.nama == "Ratu Salsabila"
    assert saya.asal_desa == "Kumantan"