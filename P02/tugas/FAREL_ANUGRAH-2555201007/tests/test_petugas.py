from src.model.petugas import Petugas


def test_petugas_memiliki_identitas() -> None:
    petugas = Petugas("P001", "Andi", "Admin")
    assert petugas.identitas() == "Andi (P001) - Admin"


def test_petugas_memiliki_kontak() -> None:
    petugas = Petugas("P002", "Budi", "Operator", "081234567890")
    assert petugas.kontak() == "Budi dapat dihubungi di 081234567890"


def test_dua_objek_petugas_menyimpan_data_independen() -> None:
    petugas1 = Petugas("P001", "Andi", "Admin")
    petugas2 = Petugas("P002", "Budi", "Operator")

    assert petugas1.identitas() == "Andi (P001) - Admin"
    assert petugas2.identitas() == "Budi (P002) - Operator"
    assert petugas1.identitas() != petugas2.identitas()


def test_telepon_default() -> None:
    petugas = Petugas("P003", "Citra", "Kasir")
    assert petugas.kontak() == "Citra belum mencantumkan nomor telepon"
