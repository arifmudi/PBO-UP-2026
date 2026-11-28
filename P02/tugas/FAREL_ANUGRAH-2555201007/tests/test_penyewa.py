from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok")
    assert penyewa.identitas() == "Budi (123) — Desa Kuok"


def test_kontak_penyewa() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok", "08123456789")
    assert penyewa.kontak() == "Budi dapat dihubungi di 08123456789"


def test_telepon_default() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok")
    assert penyewa.kontak() == "Budi belum mencantumkan nomor telepon"
