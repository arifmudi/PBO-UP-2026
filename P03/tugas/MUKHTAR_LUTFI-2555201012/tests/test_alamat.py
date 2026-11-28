
"""Pengujian untuk objek nilai Alamat."""

import pytest

from src.model.alamat import Alamat


def test_membuat_alamat_valid() -> None:
    alamat = Alamat("Suka Maju", "Bangun Sari", "Kampar")
    assert alamat.dusun == "Suka Maju"
    assert alamat.desa == "Bangun Sari"
    assert alamat.kecamatan == "Kampar"


def test_alamat_lengkap() -> None:
    alamat = Alamat("Suka Maju", "Bangun Sari", "Kampar")
    assert alamat.lengkap() == (
        "Dusun Suka Maju, Desa Bangun Sari, Kecamatan Kampar"
    )


def test_alamat_singkat() -> None:
    alamat = Alamat("Suka Maju", "Bangun Sari", "Kampar")
    assert alamat.singkat() == "Bangun Sari, Kampar"


def test_desa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Suka Maju", "   ", "Kampar")


def test_kecamatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat("Suka Maju", "Bangun Sari", "")


def test_alamat_tidak_bisa_diubah() -> None:
    alamat = Alamat("Suka Maju", "Bangun Sari", "Kampar")
    with pytest.raises(AttributeError):
        alamat.desa = "Desa Baru"  # type: ignore[misc]
