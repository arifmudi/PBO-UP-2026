import pytest
from src.model.pegawai import Pegawai
from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak
from src.model.pegawai_tetap import PegawaiTetap
from src.model.penyusun_laporan import PenyusunLaporan


def buat_pegawai() -> list[Pegawai]:
    return [
        Pegawai("001", "Andi", "Staf", 3_000_000),
        PegawaiHarian("002", "Budi", "Petugas", 100_000, 20),
        PegawaiKontrak("003", "Citra", "Admin", 3_000_000),
        PegawaiTetap("004", "Dedi", "Kepala", 3_000_000, 500_000),
    ]


def test_laporan_menyimpan_jumlah_pegawai() -> None:
    laporan = PenyusunLaporan(buat_pegawai())

    assert laporan.jumlah_pegawai == 4


def test_laporan_menghasilkan_rekap_penghasilan() -> None:
    laporan = PenyusunLaporan(buat_pegawai())

    assert laporan.rekap_penghasilan() == [
        ("Andi", 3_000_000),
        ("Budi", 2_000_000),
        ("Citra", 2_700_000),
        ("Dedi", 3_500_000),
    ]


def test_laporan_menentukan_penghasilan_tertinggi() -> None:
    laporan = PenyusunLaporan(buat_pegawai())

    assert laporan.tertinggi().nama == "Dedi"


def test_laporan_menentukan_penghasilan_terendah() -> None:
    laporan = PenyusunLaporan(buat_pegawai())

    assert laporan.terendah().nama == "Budi"


def test_laporan_menghitung_total_penghasilan() -> None:
    laporan = PenyusunLaporan(buat_pegawai())

    assert laporan.total_penghasilan() == 11_200_000


def test_laporan_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        PenyusunLaporan([])


def test_laporan_menyalin_daftar_pegawai() -> None:
    pegawai = buat_pegawai()
    laporan = PenyusunLaporan(pegawai)

    pegawai.clear()

    assert laporan.jumlah_pegawai == 4


def test_jenis_pegawai_baru_tidak_memerlukan_perubahan_laporan() -> None:
    class PegawaiMagang(Pegawai):
        """Jenis pegawai baru khusus untuk pengujian."""

        def hitung_penghasilan(self) -> int:
            return self.gaji_pokok + 250_000

    magang = PegawaiMagang(
        "005", "Eka", "Magang", 1_000_000
    )

    laporan = PenyusunLaporan([magang])

    assert laporan.rekap_penghasilan() == [
        ("Eka", 1_250_000)
    ]
    assert laporan.total_penghasilan() == 1_250_000
    assert laporan.tertinggi() is magang
    assert laporan.terendah() is magang
