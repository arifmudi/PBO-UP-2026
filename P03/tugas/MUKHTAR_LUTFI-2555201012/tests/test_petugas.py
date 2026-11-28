
"""Pengujian untuk kelas Petugas dan PeriodeTugas."""

import pytest

from src.model.petugas import Petugas, PeriodeTugas


def test_membuat_petugas_dan_info() -> None:
    petugas = Petugas("P01", "Mukhtar Lutfi", "Koordinator", "Pagi")
    assert petugas.get_info() == (
        "Petugas [P01] - Mukhtar Lutfi "
        "(Koordinator, Shift: Pagi)"
    )


def test_nama_bisa_diubah_dengan_valid() -> None:
    petugas = Petugas("P01", "Mukhtar Lutfi")
    petugas.nama = "Budi"
    assert petugas.nama == "Budi"


def test_id_petugas_tidak_bisa_diubah() -> None:
    petugas = Petugas("P01", "Mukhtar Lutfi")
    with pytest.raises(AttributeError):
        petugas.id_petugas = "P02"  # type: ignore[misc]


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("P01", "   ")


def test_nama_tidak_bisa_diubah_menjadi_kosong() -> None:
    petugas = Petugas("P01", "Mukhtar Lutfi")
    with pytest.raises(ValueError):
        petugas.nama = ""


def test_shift_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("P01", "Mukhtar Lutfi", shift="Siang")


def test_periode_tugas_tidak_bisa_diubah() -> None:
    periode = PeriodeTugas("Pagi")
    with pytest.raises(AttributeError):
        periode.shift = "Malam"  # type: ignore[misc]


def test_tunjangan_shift_sore() -> None:
    petugas = Petugas("P02", "Dini", shift="Sore")
    assert petugas.hitung_tunjangan_shift() == 60000.0


def test_tarif_tunjangan_nol_ditolak() -> None:
    petugas = Petugas("P01", "Mukhtar Lutfi")
    with pytest.raises(ValueError):
        petugas.hitung_tunjangan_shift(0)
