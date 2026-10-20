
"""Pengujian untuk kelas Petugas."""

from src.model.petugas import Petugas


def test_identitas_petugas() -> None:
    petugas = Petugas("PT-01", "Andi", "Admin", "andi")
    assert petugas.identitas() == "Andi (PT-01) - Admin"


def test_kontak_dengan_nomor_telepon() -> None:
    petugas = Petugas(
        "PT-02", "Budi", "Operator", "budi", "081234567890"
    )
    assert petugas.kontak() == "Budi dapat dihubungi di 081234567890"


def test_dua_objek_menyimpan_data_masing_masing() -> None:
    petugas_a = Petugas("PT-01", "Andi", "Admin", "andi")
    petugas_b = Petugas(
        "PT-02", "Budi", "Operator", "budi", "081234567890"
    )

    assert petugas_a.identitas() == "Andi (PT-01) - Admin"
    assert petugas_b.identitas() == "Budi (PT-02) - Operator"
    assert petugas_a.kontak() == "Andi belum mencantumkan nomor telepon"
    assert petugas_b.kontak() == "Budi dapat dihubungi di 081234567890"
