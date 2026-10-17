from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    petugas = Petugas("P001", "Andi", "Admin", "081234567890")
    assert petugas.identitas() == "Andi (P001) - Admin"


def test_kontak_petugas() -> None:
    petugas = Petugas("P002", "Budi", "Operator")
    assert petugas.kontak() == "Budi belum mencantumkan nomor telepon"


def test_dua_petugas_punya_data_sendiri() -> None:
    petugas_a = Petugas("P001", "Andi", "Admin")
    petugas_b = Petugas("P002", "Budi", "Operator")
    assert petugas_a.identitas() != petugas_b.identitas()