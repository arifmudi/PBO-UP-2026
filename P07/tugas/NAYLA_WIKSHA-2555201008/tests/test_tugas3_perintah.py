
import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak
from src.model.pegawai_tetap import PegawaiTetap
from src.model.penyusun_laporan import PenyusunLaporan
from src.ui.laporan.perintah_laporan import PerintahLaporan


@pytest.fixture
def perintah() -> PerintahLaporan:
    pegawai = [
        Pegawai("001", "Andi", "Staf", 3_000_000),
        PegawaiHarian("002", "Budi", "Petugas", 100_000, 20),
        PegawaiKontrak("003", "Citra", "Admin", 3_000_000),
        PegawaiTetap("004", "Dedi", "Kepala", 3_000_000, 500_000),
    ]
    laporan = PenyusunLaporan(pegawai)
    return PerintahLaporan(laporan)


def test_perintah_kosong(perintah: PerintahLaporan) -> None:
    assert "Perintah kosong" in perintah.jalankan("")


def test_perintah_hanya_spasi(perintah: PerintahLaporan) -> None:
    assert "Perintah kosong" in perintah.jalankan("   ")


def test_perintah_bantuan(perintah: PerintahLaporan) -> None:
    assert "Perintah laporan tersedia" in perintah.jalankan("bantuan")


def test_perintah_tanda_tanya(perintah: PerintahLaporan) -> None:
    assert "Perintah laporan tersedia" in perintah.jalankan("?")


def test_perintah_bantuan_lengkap(perintah: PerintahLaporan) -> None:
    assert "Perintah laporan tersedia" in perintah.jalankan(
        "bantuan lengkap"
    )


def test_perintah_rekap(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("rekap")

    assert "Andi" in hasil
    assert "Budi" in hasil
    assert "Citra" in hasil
    assert "Dedi" in hasil


def test_perintah_tertinggi(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("tertinggi")

    assert "Dedi" in hasil
    assert "3.500.000" in hasil


def test_perintah_terendah(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("terendah")

    assert "Budi" in hasil
    assert "2.000.000" in hasil


def test_perintah_total(perintah: PerintahLaporan) -> None:
    hasil = perintah.jalankan("total")

    assert "11.200.000" in hasil


def test_perintah_tidak_dikenal(perintah: PerintahLaporan) -> None:
    assert "tidak dikenal" in perintah.jalankan("hapus")


def test_perintah_tidak_dikenal_dengan_argumen(
    perintah: PerintahLaporan,
) -> None:
    assert "tidak dikenal" in perintah.jalankan("cetak semua")


def test_perintah_rekap_dengan_argumen_ditolak(
    perintah: PerintahLaporan,
) -> None:
    assert "tidak dikenal" in perintah.jalankan("rekap semua")


def test_perintah_total_dengan_argumen_ditolak(
    perintah: PerintahLaporan,
) -> None:
    assert "tidak dikenal" in perintah.jalankan("total semua")


def test_perintah_tertinggi_dengan_argumen_ditolak(
    perintah: PerintahLaporan,
) -> None:
    assert "tidak dikenal" in perintah.jalankan("tertinggi semua")


def test_perintah_bantuan_dengan_mode_salah(
    perintah: PerintahLaporan,
) -> None:
    assert "tidak dikenal" in perintah.jalankan("bantuan singkat")


def test_perintah_tidak_mengubah_data_pegawai(
    perintah: PerintahLaporan,
) -> None:
    perintah.jalankan("rekap")

    assert "11.200.000" in perintah.jalankan("total")
