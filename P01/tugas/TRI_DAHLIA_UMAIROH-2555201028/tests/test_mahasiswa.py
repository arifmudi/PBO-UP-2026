from src.mahasiswa import Mahasiswa


def test_mahasiswa_perkenalan() -> None:
    mahasiswa = Mahasiswa("Budi Santoso", "2410123456", "Kuok")

    assert mahasiswa.nama == "Budi Santoso"
    assert mahasiswa.nim == "2410123456"
    assert mahasiswa.desa == "Kuok"
    assert mahasiswa.perkenalan() == (
        "Saya Budi Santoso (2410123456), dari Kuok."
    )