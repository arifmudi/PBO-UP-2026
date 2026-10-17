""" Pengujian untuk kelas Petugas """

from src.model.petugas import Petugas

def test_tambah_petugas() -> None:
    petugas = Petugas("Fitri Nabila", "085375362713", "Admin", 100000)
    assert petugas._nama_petugas == "Fitri Nabila"
    assert petugas._no_telepon == "085375362713"
    assert petugas._jabatan == "Admin"
    assert petugas._gaji_harian == 100000

def test_hitung_gaji_petugas() -> None:
    petugas = Petugas("Fitri Nabila", "085375362713", "Admin", 100000)
    assert petugas.gaji_petugas(5) == 500000

def test_tampilkan_identitas_petugas() -> None:
    petugas = Petugas("Fitri Nabila", "085375362713", "Admin", 100000)
    assert petugas.tampilkan_identitas() == "Fitri Nabila (Admin) nomor telepon: 085375362713, gaji harian: Rp100.000"

def test_hubungi_petugas() -> None:
    petugas = Petugas("Fitri Nabila", "085375362713", "Admin", 100000)
    assert petugas.hubungi_petugas() == "Fitri Nabila - 085375362713"