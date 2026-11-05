"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_penyewa_identitas() -> None:
    penyewa = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        "Kuok",
        "089500000001",
    )

    assert penyewa.identitas() == (
        "Budi Santoso (1406012509900001) - Desa Kuok"
    )


def test_penyewa_kontak_ada_telepon() -> None:
    penyewa = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        "Kuok",
        "089500000001",
    )

    assert penyewa.kontak() == (
        "Budi Santoso - 089500000001"
    )


def test_penyewa_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa(
        "1406012509900002",
        "Nur atna Fitri Hasanah",
        "Kuok",
    )

    assert penyewa.kontak() == (
        "Nur atna Fitri Hasanah belum mencantumkan nomor telepon"
    )