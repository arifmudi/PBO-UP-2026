"""Pengujian untuk kelas Petugas."""

import pytest

from src.model.petugas import IdentitasPetugas, Petugas


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


def test_property_baca_saja() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "Kumantan")

    with pytest.raises(AttributeError):
        petugas.nama = "Budi"  # type: ignore[misc]

    with pytest.raises(AttributeError):
        petugas.id_petugas = "PT-02"  # type: ignore[misc]


def test_setter_desa_tugas() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "Kumantan")
    petugas.desa_tugas = "Kuok"

    assert petugas.desa_tugas == "Kuok"

    with pytest.raises(ValueError):
        petugas.desa_tugas = ""


def test_setter_telepon() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "Kumantan")
    petugas.telepon = "08123456789"

    assert petugas.telepon == "08123456789"

    with pytest.raises(ValueError):
        petugas.telepon = ""


def test_validasi_data_petugas() -> None:
    with pytest.raises(ValueError):
        Petugas("", "Andi", "Admin", "Kumantan")

    with pytest.raises(ValueError):
        Petugas("PT-01", "", "Admin", "Kumantan")

    with pytest.raises(ValueError):
        Petugas("PT-01", "Andi", "Admin", "")


def test_objek_nilai_identitas_beku() -> None:
    identitas = IdentitasPetugas("PT-01", "Andi", "Admin")

    with pytest.raises(AttributeError):
        identitas.nama = "Budi"  # type: ignore[misc]