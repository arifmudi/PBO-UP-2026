from src.model.penyewa import Penyewa


def test_identitas() -> None:
    penyewa = Penyewa("123456", "Budi", "Suka Maju")
    assert penyewa.identitas() == "Budi (123456) — Desa Suka Maju"


def test_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("123456", "Budi", "Suka Maju")
    assert penyewa.kontak() == "Budi belum mencantumkan nomor telepon"


def test_kontak_dengan_telepon() -> None:
    penyewa = Penyewa(
        "123456",
        "Budi",
        "Suka Maju",
        "08123456789",
    )
    assert penyewa.kontak() == "Budi dapat dihubungi di 08123456789"