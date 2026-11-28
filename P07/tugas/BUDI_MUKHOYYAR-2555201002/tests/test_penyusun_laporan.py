from src.model.pegawai.pegawai import Pegawai
from src.model.pegawai.pegawai_honorer import PegawaiHonorer
from src.model.pegawai.pegawai_kontrak import PegawaiKontrak
from src.model.pegawai.pegawai_tetap import PegawaiTetap
from src.model.pegawai.penyusun_laporan import PenyusunLaporan


def test_rekap_dan_total_penghasilan() -> None:
    daftar = [
        PegawaiTetap("001", "Andi", 3000000, 500000),
        PegawaiHonorer("002", "Siti", 25000, 80),
        PegawaiKontrak("003", "Rina", 3000000, 200000),
    ]

    laporan = PenyusunLaporan(daftar)

    assert laporan.rekap_penghasilan() == [
        ("Andi", 3500000),
        ("Siti", 2000000),
        ("Rina", 3500000),
    ]
    assert laporan.total_penghasilan() == 9000000


def test_pegawai_berpenghasilan_tertinggi_dan_terendah() -> None:
    daftar = [
        PegawaiTetap("001", "Andi", 3000000, 500000),
        PegawaiHonorer("002", "Siti", 25000, 80),
        PegawaiKontrak("003", "Rina", 3000000, 200000),
    ]

    laporan = PenyusunLaporan(daftar)

    assert laporan.pegawai_tertinggi() == ("Andi", 3500000)
    assert laporan.pegawai_terendah() == ("Siti", 2000000)


def test_penyusun_laporan_menerima_jenis_pegawai_baru() -> None:
    class PegawaiMagang(Pegawai):
        def hitung_penghasilan(self, penyesuaian: int = 0) -> int:
            return 1500000 + penyesuaian

    daftar = [
        PegawaiTetap("001", "Andi", 3000000, 500000),
        PegawaiMagang("004", "Doni", 0),
    ]

    laporan = PenyusunLaporan(daftar)

    assert laporan.rekap_penghasilan() == [
        ("Andi", 3500000),
        ("Doni", 1500000),
    ]
    assert laporan.total_penghasilan() == 5000000