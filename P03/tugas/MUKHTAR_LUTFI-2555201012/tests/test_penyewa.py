
"""Pengujian untuk kelas Penyewa."""

import pytest

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def buat_alamat() -> Alamat:
    return Alamat("Suka Maju", "Bangkinang", "Kampar")


def test_inisialisasi_dan_default_telepon() -> None:
    p = Penyewa("1406010101950003", "Mukhtar Lutfi", buat_alamat())
    assert p.nik == "1406010101950003"
    assert p.alamat.desa == "Bangkinang"
    assert p.telepon == "-"


def test_format_identitas_desa_berbeda() -> None:
    p = Penyewa(
        "1406011212880005",
        "Zulkifli",
        Alamat("Dusun Satu", "Air Tiris", "Kampar"),
        "0852-9876-5432",
    )
    assert p.identitas() == "Zulkifli (1406011212880005) — Desa Air Tiris"


def test_kontak_dengan_nomor_telepon() -> None:
    p = Penyewa(
        "1406011505920004",
        "Rahmat Hidayat",
        Alamat("Dusun Dua", "Kuok", "Kampar"),
        "0821-7788-9900",
    )
    assert p.kontak() == (
        "Rahmat Hidayat dapat dihubungi di 0821-7788-9900"
    )


def test_nik_harus_16_angka() -> None:
    with pytest.raises(ValueError):
        Penyewa("12345", "Budi", buat_alamat())


def test_nik_tidak_boleh_mengandung_huruf() -> None:
    with pytest.raises(ValueError):
        Penyewa("140601010195000A", "Budi", buat_alamat())


def test_nik_read_only() -> None:
    p = Penyewa("1406010101950003", "Budi", buat_alamat())
    with pytest.raises(AttributeError):
        p.nik = "1234567890123456"  # type: ignore[misc]


def test_alamat_harus_berupa_objek_alamat() -> None:
    with pytest.raises(ValueError):
        Penyewa(
            "1406010101950003",
            "Budi",
            "Bangkinang",  # type: ignore[arg-type]
        )


def test_telepon_menerima_nomor_valid() -> None:
    p = Penyewa("1406010101950003", "Budi", buat_alamat())
    p.telepon = "0812-3456-7890"
    assert p.telepon == "0812-3456-7890"


def test_telepon_menerima_tanda_strip() -> None:
    p = Penyewa("1406010101950003", "Budi", buat_alamat())
    p.telepon = "-"
    assert p.telepon == "-"


def test_telepon_menolak_nomor_terlalu_pendek() -> None:
    p = Penyewa("1406010101950003", "Budi", buat_alamat())
    with pytest.raises(ValueError):
        p.telepon = "12345"


def test_telepon_menolak_huruf() -> None:
    p = Penyewa("1406010101950003", "Budi", buat_alamat())
    with pytest.raises(ValueError):
        p.telepon = "0812ABC45678"


def test_alamat_read_only() -> None:
    p = Penyewa("1406010101950003", "Budi", buat_alamat())
    with pytest.raises(AttributeError):
        p.alamat = buat_alamat()  # type: ignore[misc]
