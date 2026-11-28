from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    petugas = Petugas("PT-01", "Ratu Salsabila", "Pengurus UPJA", "Kumantan")
    assert petugas.identitas() == "Ratu Salsabila (PT-01) — Pengurus UPJA"


def test_wilayah_tugas() -> None:
    petugas = Petugas("PT-01", "Ratu Salsabila", "Pengurus UPJA", "Kumantan")
    assert petugas.wilayah_tugas() == "Ratu Salsabila bertugas di Desa Kumantan"


def test_kontak_tanpa_nomor_telepon() -> None:
    petugas = Petugas("PT-01", "Ratu Salsabila", "Pengurus UPJA", "Kumantan")
    assert petugas.kontak() == "Ratu Salsabila belum mencantumkan nomor telepon"


def test_kontak_dengan_nomor_telepon() -> None:
    petugas = Petugas("PT-01", "Ratu Salsabila", "Pengurus UPJA", "Kumantan", "081234567890")
    assert petugas.kontak() == "Ratu Salsabila dapat dihubungi di 081234567890"