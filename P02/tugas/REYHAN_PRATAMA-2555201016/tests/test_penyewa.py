from src.model.penyewa import Penyewa


def test_identitas_penyewa() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok", "0812")
    assert penyewa.identitas() == "Budi (123) — Desa Kuok"


def test_kontak_dengan_telepon() -> None:
    penyewa = Penyewa("123", "Budi", "Kuok", "0812")
    assert penyewa.kontak() == "Budi dapat dihubungi di 0812"


def test_kontak_tanpa_telepon() -> None:
    penyewa = Penyewa("456", "Siti", "Salo")
    assert penyewa.kontak() == "Siti belum mencantumkan nomor telepon"


def test_dua_penyewa_punya_data_sendiri() -> None:
    a = Penyewa("123", "Budi", "Kuok")
    b = Penyewa("456", "Siti", "Salo")
    assert a.identitas() != b.identitas()