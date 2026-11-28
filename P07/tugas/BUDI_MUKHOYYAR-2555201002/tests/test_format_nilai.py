
from src.format_nilai import sebagai_teks


def test_format_bilangan_bulat() -> None:
    assert sebagai_teks(150_000) == "Rp150.000"


def test_format_bilangan_bulat_nol() -> None:
    assert sebagai_teks(0) == "Rp0"


def test_format_bilangan_bulat_jutaan() -> None:
    assert sebagai_teks(1_500_000) == "Rp1.500.000"


def test_format_bilangan_pecahan() -> None:
    assert sebagai_teks(0.25) == "25.0%"


def test_format_bilangan_pecahan_persen_penuh() -> None:
    assert sebagai_teks(1.0) == "100.0%"


def test_format_bilangan_pecahan_nol() -> None:
    assert sebagai_teks(0.0) == "0.0%"


def test_format_daftar_angka() -> None:
    assert sebagai_teks([10_000, 20_000]) == "Rp10.000, Rp20.000"


def test_format_daftar_campuran() -> None:
    assert sebagai_teks([10_000, 0.5, "UPJA"]) == (
        "Rp10.000, 50.0%, UPJA"
    )


def test_format_daftar_kosong() -> None:
    assert sebagai_teks([]) == ""


def test_format_teks_biasa() -> None:
    assert sebagai_teks("Belajar PBO") == "Belajar PBO"


def test_format_boolean() -> None:
    assert sebagai_teks(True) == "Rp1"


def test_format_tipe_data_lain() -> None:
    assert sebagai_teks(None) == "None"
