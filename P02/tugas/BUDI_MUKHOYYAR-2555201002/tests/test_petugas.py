from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    petugas = Petugas(
        "PTG001",
        "Budi",
        "Pengurus UPJA",
    )

    assert petugas.identitas() == "Budi (PTG001) - Pengurus UPJA"


def test_kontak_petugas() -> None:
    petugas = Petugas(
        "PTG001",
        "Budi",
        "Pengurus UPJA",
        "08123456789",
    )

    assert petugas.kontak() == "Budi dapat dihubungi di 08123456789"


def test_kontak_petugas_tanpa_nomor() -> None:
    petugas = Petugas(
        "PTG002",
        "Siti",
        "Administrasi",
    )

    assert petugas.kontak() == "Siti belum mencantumkan nomor telepon"


def test_dua_petugas_punya_data_sendiri() -> None:
    petugas_a = Petugas(
        "PTG001",
        "Budi",
        "Pengurus UPJA",
    )

    petugas_b = Petugas(
        "PTG002",
        "Siti",
        "Administrasi",
    )

    assert petugas_a.identitas() != petugas_b.identitas()