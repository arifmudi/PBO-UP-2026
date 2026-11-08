import pytest

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat(
        dusun="Pulau Belimbing",
        desa="Kuok",
        kecamatan="Kuok",
    )
    return Penyewa(
        nik="1406012509900001",
        nama="Budi Santoso",
        alamat=alamat,
    )


def buat_alat(kode: str = "TR-01") -> AlatTani:
    return AlatTani(
        kode=kode,
        nama=f"Alat {kode}",
        tarif_harian=150000,
    )


def test_sewa_menyimpan_penyewa() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-001", penyewa)

    assert sewa.penyewa is penyewa


def test_baris_sewa_tidak_dapat_diubah_dari_luar() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)

    assert isinstance(sewa.baris, tuple)
    assert len(sewa.baris) == 1


def test_tambah_alat_menghitung_total() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 3)

    assert sewa.total() == 450000


def test_alat_yang_sama_tidak_boleh_ditambahkan_dua_kali() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    alat = buat_alat()

    sewa.tambah_alat(alat, 2)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat, 3)


def test_maksimal_sepuluh_alat() -> None:
    sewa = Sewa("SW-001", buat_penyewa())

    for nomor in range(10):
        sewa.tambah_alat(buat_alat(f"TR-{nomor:02d}"), 1)

    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat("TR-10"), 1)


def test_nota_menggunakan_snapshot_tarif() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    alat = buat_alat()

    sewa.tambah_alat(alat, 2)
    alat.tarif_harian = 200000

    assert "Rp150.000" in sewa.nota()
    assert "Rp300.000" in sewa.nota()


def test_nomor_sewa_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        Sewa("   ", buat_penyewa())