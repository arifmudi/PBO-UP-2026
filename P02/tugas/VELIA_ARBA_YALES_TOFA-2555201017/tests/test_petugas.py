from src.model.petugas import Petugas


def test_petugas_menyimpan_data() -> None:
    petugas = Petugas(
        "Andi Saputra",
        "NIP001",
        "Administrator",
        "0812-1111-2222",
    )

    assert petugas.identitas() == "Andi Saputra (NIP001) - Administrator"
    assert petugas.kontak() == "Andi Saputra dapat dihubungi di 0812-1111-2222"


def test_petugas_tanpa_telepon() -> None:
    petugas = Petugas("Siti Aminah", "NIP002", "Admin")

    assert petugas.kontak() == "Siti Aminah belum mencantumkan nomor telepon"


def test_dua_petugas_punya_data_sendiri() -> None:
    petugas1 = Petugas("Andi Saputra", "NIP001", "Administrator")
    petugas2 = Petugas("Budi Santoso", "NIP002", "Operator")

    assert petugas1.identitas() == "Andi Saputra (NIP001) - Administrator"
    assert petugas2.identitas() == "Budi Santoso (NIP002) - Operator"
