from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.petugas import Petugas


def test_penyewa_menyimpan_data() -> None:
    penyewa = Penyewa(
        "Budi Santoso",
        "1406012509900001",
        "Desa Kuok",
        "0812-3456-7890",
    )

    assert penyewa.identitas() == "Budi Santoso (1406012509900001) - Desa Kuok"


def test_penyewa_kontak_dengan_telepon() -> None:
    penyewa = Penyewa(
        "Budi Santoso",
        "1406012509900001",
        "Desa Kuok",
        "0812-3456-7890",
    )

    assert penyewa.kontak() == "Budi Santoso dapat dihubungi di 0812-3456-7890"


def test_penyewa_tanpa_telepon() -> None:
    penyewa = Penyewa(
        "Siti Aminah",
        "1406012509900002",
        "Desa Bangkinang",
    )

    assert penyewa.kontak() == "Siti Aminah belum mencantumkan nomor telepon"


def test_dua_objek_punya_data_sendiri() -> None:
    penyewa_1 = Penyewa("Budi", "001", "Kuok")
    penyewa_2 = Penyewa("Siti", "002", "Bangkinang")

    assert penyewa_1.identitas() != penyewa_2.identitas()


def test_alat_tani_menghitung_biaya() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    assert alat.biaya_sewa(3) == 450000


def test_alat_tani_menghasilkan_keterangan() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)

    assert alat.keterangan() == "[TR-01] Traktor - Rp150,000/hari"


def test_petugas_menghasilkan_identitas() -> None:
    petugas = Petugas(
        "Andi Saputra",
        "198705102010011001",
        "Petugas Lapangan",
    )

    assert petugas.identitas() == (
        "Andi Saputra (198705102010011001) - Petugas Lapangan"
    )


def test_petugas_kontak() -> None:
    petugas = Petugas(
        "Andi Saputra",
        "198705102010011001",
        "Petugas Lapangan",
        "0813-9876-5432",
    )

    assert petugas.kontak() == "Andi Saputra dapat dihubungi di 0813-9876-5432"