""" Unit test untuk kelas Petugas """
from src.model.petugas import Petugas


def test_penyimpanan_data_dua_objek_petugas_independen() -> None:
    petugas = Petugas("P01", "Mukhtar Lutfi", "Koordinator", "Pagi")

    assert petugas._id_petugas == "P01"
    assert petugas._nama == "Mukhtar Lutfi"
    assert petugas._jabatan == "Koordinator"

    petugas._nama = "Budi S."
    assert petugas._nama == "Budi S."

def test_get_info_petugas() -> None:
    petugas = Petugas("P01", "Mukhtar Lutfi", "Koordinator", "Pagi")
    info = petugas.get_info()

    assert info == "Petugas [P01] - Mukhtar Lutfi (Koordinator, Shift: Pagi)"

def test_hitung_tunjangan_shift_default_dan_kustom() -> None:
    petugas_pagi = Petugas("P01", "Mukhtar Lutfi", shift="Pagi")
    petugas_sore = Petugas("P02", "Dini", shift="Sore")

    assert petugas_pagi.hitung_tunjangan_shift() == 50000.0
    assert petugas_sore.hitung_tunjangan_shift() == 60000.0
    assert petugas_sore.hitung_tunjangan_shift(100000.0) == 120000.0