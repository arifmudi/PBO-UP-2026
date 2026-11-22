
from src.format_nilai import sebagai_teks


def test_format_bilangan_bulat() -> None:
    assert sebagai_teks(150000) == "Rp150.000"


def test_format_bilangan_pecahan() -> None:
    assert sebagai_teks(0.25) == "25.0%"


def test_format_daftar() -> None:
    assert sebagai_teks([1000, 0.5, "Andi"]) == "Rp1.000, 50.0%, Andi"


def test_format_teks_umum() -> None:
    assert sebagai_teks("Nayla") == "Nayla"


def test_format_bilangan_negatif() -> None:
    assert sebagai_teks(-5000) == "Rp-5.000"


def test_format_daftar_kosong() -> None:
    assert sebagai_teks([]) == ""


def test_format_daftar_bersarang() -> None:
    assert sebagai_teks([[1000, 0.5], "Andi"]) == (
        "Rp1.000, 50.0%, Andi"
    )
