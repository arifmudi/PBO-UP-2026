"""Pengujian unit untuk kelas Petugas menggunakan pytest."""

from src.model.petugas import Petugas


def test_info_petugas() -> None:
    petugas = Petugas("P-01", "Helmy", "Admin Lapangan", True)
    assert petugas.info_petugas() == "[P-01] Helmy - Admin Lapangan (Aktif)"


def test_status_keaktifan() -> None:
    petugas_aktif = Petugas("P-01", "Helmy", "Admin", True)
    petugas_nonaktif = Petugas("P-02", "Faisal", "Gudang", False)

    assert "aktif" in petugas_aktif.status_keaktifan()
    assert "tidak aktif" in petugas_nonaktif.status_keaktifan()


def test_dua_objek_petugas_punya_data_sendiri() -> None:
    p1 = Petugas("P-01", "Helmy", "Admin")
    p2 = Petugas("P-02", "Faisal", "Kasir")

    assert p1.info_petugas() != p2.info_petugas()