"""Pengujian untuk kelas Penyewa."""

from src.model.penyewa import Penyewa


def test_inisialisasi_dan_default_telepon() -> None:
    p = Penyewa("1406010101950003", "Mukhtar Lutfi", "Bangkinang")
    assert p._nik == "1406010101950003"
    assert p._nama == "Mukhtar Lutfi"
    assert p._desa == "Bangkinang"
    assert p._telepon == "-"


def test_format_identitas_desa_berbeda() -> None:
    p = Penyewa("1406011212880005", "Zulkifli", "Air Tiris", "0852-9876-5432")
    assert p.identitas() == "Zulkifli (1406011212880005) — Desa Air Tiris"


def test_kontak_dengan_nomor_telepon() -> None:
    p = Penyewa("1406011505920004", "Rahmat Hidayat", "Kuok", "0821-7788-9900")
    assert p.kontak() == "Rahmat Hidayat dapat dihubungi di 0821-7788-9900"