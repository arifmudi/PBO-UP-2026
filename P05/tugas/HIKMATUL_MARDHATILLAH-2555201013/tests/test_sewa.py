"""Pengujian untuk kelas BarisSewa dan Sewa."""

import pytest

from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.sewa import Sewa
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def buat_alat() -> AlatTani:
    return AlatTani(
        kode="TR-01",
        nama="Traktor Roda Dua",
        tarif_harian=150_000,
    )


def buat_penyewa() -> Penyewa:
    alamat = Alamat(
        dusun="-",
        desa="Kuok",
        kecamatan="Kuok",
    )
    return Penyewa(
        nik="1406012509900001",
        nama="Budi Santoso",
        alamat=alamat,
    )


def test_baris_sewa_menyimpan_data_alat() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)

    assert baris.kode_alat == "TR-01"
    assert baris.nama_alat == "Traktor Roda Dua"
    assert baris.tarif_harian == 150_000
    assert baris.jumlah_hari == 3


def test_subtotal_baris_sewa() -> None:
    baris = BarisSewa(buat_alat(), 3)

    assert baris.subtotal() == 450_000


def test_jumlah_hari_tidak_boleh_nol() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), 0)


def test_jumlah_hari_tidak_boleh_negatif() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), -1)


def test_sewa_menyimpan_penyewa() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-001", penyewa)

    assert sewa.penyewa is penyewa


def test_baris_sewa_dikembalikan_sebagai_tuple() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 3)

    assert isinstance(sewa.baris, tuple)
    assert len(sewa.baris) == 1


def test_sewa_menghitung_total() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 3)

    assert sewa.total() == 450_000


def test_sewa_menolak_alat_yang_sama() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    alat = buat_alat()
    sewa.tambah_alat(alat, 3)

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat, 2)

def test_tarif_baris_sewa_tidak_berubah() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)

    alat.tarif_harian = 200_000

    assert baris.tarif_harian == 150_000
    assert baris.subtotal() == 450_000

def test_sewa_maksimal_sepuluh_alat() -> None:
    sewa = Sewa("SW-002", buat_penyewa())

    for nomor in range(10):
        alat = AlatTani(
            kode=f"AL-{nomor:02d}",
            nama=f"Alat {nomor}",
            tarif_harian=100_000,
        )
        sewa.tambah_alat(alat, 2)

    assert len(sewa.baris) == 10

    alat_baru = AlatTani(
        kode="AL-10",
        nama="Alat Tambahan",
        tarif_harian=100_000,
    )

    with pytest.raises(ValueError):
        sewa.tambah_alat(alat_baru, 2)

def test_nomor_sewa_tidak_boleh_kosong() -> None:
    with pytest.raises(ValueError):
        Sewa("   ", buat_penyewa())