"""Pengujian untuk kelas Penyewa."""
from src.model.penyewa import Penyewa


def test_penyewa_menyimpan_data() -> None:
    penyewa = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        "Kuok",
        "0812-3456-7890",
    )

    assert penyewa._nik == "1406012509900001"
    assert penyewa._nama == "Budi Santoso"
    assert penyewa._desa == "Kuok"
    assert penyewa._telepon == "0812-3456-7890"


def test_penyewa_identitas() -> None:
    penyewa = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        "Kuok",
        "0812-3456-7890",
    )

    assert penyewa.identitas() == (
        "Budi Santoso (1406012509900001) — Desa Kuok"
    )


def test_penyewa_kontak() -> None:
    penyewa = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        "Kuok",
        "0812-3456-7890",
    )

    assert penyewa.kontak() == (
        "Budi Santoso dapat dihubungi di 0812-3456-7890"
    )


def test_penyewa_tanpa_telepon() -> None:
    penyewa = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        "Salo",
    )

    assert penyewa.kontak() == (
        "Siti Aminah belum mencantumkan nomor telepon"
    )
