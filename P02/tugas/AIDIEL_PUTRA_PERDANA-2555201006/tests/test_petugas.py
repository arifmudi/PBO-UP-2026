# """Pengujian untuk kelas Petugas."""

# from src.model.petugas import Petugas


# def test_dua_objek_petugas_menyimpan_data_masing_masing() -> None:
#     petugas_a = Petugas("PT-01", "Budi Santoso", "Operator", 120000)
#     petugas_b = Petugas("PT-02", "Siti Aminah", "Admin", 100000)

#     assert petugas_a.identitas() != petugas_b.identitas()
#     assert petugas_a.honor_petugas(2) != petugas_b.honor_petugas(2)


# def test_honor_petugas_tiga_hari() -> None:
#     petugas = Petugas("PT-01", "Budi Santoso", "Operator", 120000)
#     assert petugas.honor_petugas(3) == 360000


# def test_parameter_berdefault() -> None:
#     petugas = Petugas("PT-03", "Eko")
#     assert petugas.identitas() == "[PT-03] Eko (Operator)"
#     assert petugas.honor_petugas(1) == 100000

""" Pengujian untuk kelas Petugas """

from src.model.petugas import Petugas

def test_tambah_petugas() -> None:
    petugas_1 = Petugas("Aidiel Putra Perdana", "Operator", 150000)
    petugas_2 = Petugas("Joko Mulyono", "Admin", 120000)

    assert petugas_1._nama == "Aidiel Putra Perdana"
    assert petugas_1._jabatan == "Operator"
    assert petugas_1._tarif_per_jam == 150000

    assert petugas_2._nama == "Joko Mulyono"
    assert petugas_2._jabatan == "Admin"
    assert petugas_2._tarif_per_jam == 120000

def test_hitung_pendapatan() -> None:
    petugas_1 = Petugas("Aidiel Putra Perdana", "Operator", 150000)
    petugas_2 = Petugas("Joko Mulyono", "Admin", 120000)

    assert petugas_1.hitung_pendapatan(3) == 450000
    assert petugas_2.hitung_pendapatan(3) == 360000

def test_cetak_identitas() -> None:
    petugas_1 = Petugas("Aidiel Putra Perdana", "Operator", 150000)
    petugas_2 = Petugas("Joko Mulyono", "Admin", 120000)

    assert petugas_1.cetak_identitas() == "Aidiel Putra Perdana (Operator) — Tarif per jam: Rp 150.000"
    assert petugas_2.cetak_identitas() == "Joko Mulyono (Admin) — Tarif per jam: Rp 120.000"

def test_parameter_default() -> None:
    petugas_default = Petugas("Siti Aminah", "Operator")
    assert petugas_default._tarif_per_jam == 100000