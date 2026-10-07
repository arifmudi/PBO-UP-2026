"""Pengujian untuk kelas Petugas."""
from src.model.petugas import Petugas


def test_petugas_menyimpan_data() -> None:
    petugas = Petugas(
        "PT-01",
        "Rudi Hartono",
        "Admin",
        "0812-1111-2222",
    )

    assert petugas._id_petugas == "PT-01"
    assert petugas._nama == "Rudi Hartono"
    assert petugas._jabatan == "Admin"
    assert petugas._telepon == "0812-1111-2222"


def test_petugas_identitas() -> None:
    petugas = Petugas(
        "PT-01",
        "Rudi Hartono",
        "Admin",
        "0812-1111-2222",
    )

    assert petugas.identitas() == "Rudi Hartono (PT-01) — Admin"


def test_dua_petugas_punya_data_sendiri() -> None:
    a = Petugas("PT-01", "Rudi Hartono", "Admin")
    b = Petugas("PT-02", "Sari Aminah", "Kasir")

    assert a.identitas() != b.identitas()