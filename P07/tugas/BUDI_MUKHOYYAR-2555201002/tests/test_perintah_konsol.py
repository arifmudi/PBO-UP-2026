
import pytest
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor
from src.ui.perintah_konsol import PerintahKonsol


@pytest.fixture
def konsol() -> PerintahKonsol:
    """Menyediakan konsol dengan tiga jenis alat."""
    alat = [
        Traktor("TR-01", "Traktor", 150_000, 8),
        PompaAir("PA-01", "Pompa Air", 75_000, 100),
        Perontok("PR-01", "Perontok", 50_000, 500),
    ]
    return PerintahKonsol(DaftarHarga(alat))


def test_perintah_kosong(konsol: PerintahKonsol) -> None:
    assert konsol.jalankan("") == (
        "Perintah kosong. Ketik 'bantuan'."
    )


def test_perintah_hanya_spasi(konsol: PerintahKonsol) -> None:
    assert konsol.jalankan("   ") == (
        "Perintah kosong. Ketik 'bantuan'."
    )


def test_perintah_bantuan(konsol: PerintahKonsol) -> None:
    assert "daftar <hari>" in konsol.jalankan("bantuan")


def test_perintah_tanda_tanya(konsol: PerintahKonsol) -> None:
    assert konsol.jalankan("?") == PerintahKonsol.BANTUAN


def test_perintah_daftar(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("daftar 1")
    assert "Traktor: Rp250.000" in hasil


def test_perintah_harga(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("harga PA-01 2")
    assert hasil == "Pompa Air: Rp192.000"


def test_perintah_harga_kode_tidak_ditemukan(
    konsol: PerintahKonsol,
) -> None:
    hasil = konsol.jalankan("harga XX-99 1")
    assert hasil == "Alat dengan kode 'XX-99' tidak ditemukan."


def test_perintah_termurah(konsol: PerintahKonsol) -> None:
    hasil = konsol.jalankan("termurah 3")
    assert hasil == "Termurah untuk 3 hari: Perontok"


def test_perintah_tidak_dikenal(konsol: PerintahKonsol) -> None:
    assert konsol.jalankan("hapus") == (
        "Perintah 'hapus' tidak dikenal."
    )


def test_perintah_cetak_tidak_dikenal(
    konsol: PerintahKonsol,
) -> None:
    assert konsol.jalankan("cetak") == (
        "Perintah 'cetak' tidak dikenal."
    )


def test_perintah_salah_tidak_dikenal(
    konsol: PerintahKonsol,
) -> None:
    assert konsol.jalankan("mulai") == (
        "Perintah 'mulai' tidak dikenal."
    )


def test_perintah_daftar_tanpa_jumlah_hari(
    konsol: PerintahKonsol,
) -> None:
    assert konsol.jalankan("daftar") == (
        "Perintah 'daftar' tidak dikenal."
    )


def test_perintah_daftar_hari_bukan_angka(
    konsol: PerintahKonsol,
) -> None:
    assert konsol.jalankan("daftar besok") == (
        "Perintah 'daftar' tidak dikenal."
    )


def test_perintah_harga_format_salah(
    konsol: PerintahKonsol,
) -> None:
    assert konsol.jalankan("harga PA-01") == (
        "Perintah 'harga' tidak dikenal."
    )


def test_perintah_termurah_hari_bukan_angka(
    konsol: PerintahKonsol,
) -> None:
    assert konsol.jalankan("termurah besok") == (
        "Perintah 'termurah' tidak dikenal."
    )
