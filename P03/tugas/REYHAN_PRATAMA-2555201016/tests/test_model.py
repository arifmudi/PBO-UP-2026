
import pytest
from src.model.alamat import Alamat


def test_alamat_valid() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    assert alamat.kota == "Bangkinang"


def test_alamat_jalan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat(
            jalan="",
            kota="Bangkinang",
            provinsi="Riau",
            kode_pos="28411",
        )


def test_alamat_beku_tidak_bisa_diubah() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    with pytest.raises(AttributeError):
        alamat.kota = "Pekanbaru"  # type: ignore[misc]
