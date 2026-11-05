
from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("12345", "Budi", "Kuok")
    assert penyewa.identitas() == "Budi (12345) — Desa Kuok"


def test_kontak_dengan_nomor_telepon() -> None:
    penyewa = Penyewa("12345", "Budi", "Kuok", "081234567890")
    assert penyewa.kontak() == "Budi dapat dihubungi di 081234567890"


def test_kontak_tanpa_nomor_telepon() -> None:
    penyewa = Penyewa("12345", "Siti", "Bangkinang")
    assert penyewa.kontak() == "Siti belum mencantumkan nomor telepon"


def test_dua_penyewa_memiliki_data_sendiri() -> None:
    budi = Penyewa("12345", "Budi", "Kuok")
    siti = Penyewa("67890", "Siti", "Bangkinang")

    assert budi.identitas() == "Budi (12345) — Desa Kuok"
    assert siti.identitas() == "Siti (67890) — Desa Bangkinang"
