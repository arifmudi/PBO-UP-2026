
import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.petugas import Petugas


def buat_alamat() -> Alamat:
    return Alamat("Suka Maju", "Kuok", "Kuok")


def buat_penyewa() -> Penyewa:
    return Penyewa(
        "Budi Santoso",
        "1406012509900001",
        buat_alamat(),
        "0812-3456-7890",
    )


def test_alamat_lengkap() -> None:
    alamat = buat_alamat()
    assert alamat.lengkap() == "Dusun Suka Maju, Desa Kuok, Kecamatan Kuok"


def test_alamat_singkat() -> None:
    alamat = buat_alamat()
    assert alamat.singkat() == "Kuok, Kuok"


def test_alamat_menolak_desa_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Suka Maju", "   ", "Kuok")


def test_alamat_menolak_kecamatan_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Suka Maju", "Kuok", "   ")


def test_alamat_tidak_dapat_diubah() -> None:
    alamat = buat_alamat()
    with pytest.raises(AttributeError):
        alamat.desa = "Bangkinang"  # type: ignore[misc]


def test_penyewa_menyimpan_data() -> None:
    penyewa = buat_penyewa()
    assert penyewa.identitas() == (
        "Budi Santoso (1406012509900001) - Kuok, Kuok"
    )


def test_penyewa_kontak_dengan_telepon() -> None:
    penyewa = buat_penyewa()
    assert penyewa.kontak() == (
        "Budi Santoso dapat dihubungi di 0812-3456-7890"
    )


def test_penyewa_tanpa_telepon() -> None:
    penyewa = Penyewa("Siti Aminah", "1406012509900002", buat_alamat())
    assert penyewa.kontak() == (
        "Siti Aminah belum mencantumkan nomor telepon"
    )


def test_dua_penyewa_punya_data_sendiri() -> None:
    penyewa_1 = buat_penyewa()
    penyewa_2 = Penyewa("Siti", "1406012509900002", buat_alamat())
    assert penyewa_1.identitas() != penyewa_2.identitas()


def test_nik_menolak_digit_kurang() -> None:
    with pytest.raises(ValueError):
        Penyewa("Budi", "12345", buat_alamat())


def test_nik_menolak_huruf() -> None:
    with pytest.raises(ValueError):
        Penyewa("Budi", "140601250990000A", buat_alamat())


def test_nik_tidak_dapat_diubah_langsung() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(AttributeError):
        penyewa.nik = "1406012509900002"  # type: ignore[misc]


def test_telepon_menolak_nomor_terlalu_pendek() -> None:
    with pytest.raises(ValueError):
        Penyewa("Budi", "1406012509900001", buat_alamat(), "12345")


def test_telepon_menolak_huruf() -> None:
    with pytest.raises(ValueError):
        Penyewa(
            "Budi",
            "1406012509900001",
            buat_alamat(),
            "0812ABC56789",
        )


def test_telepon_menolak_tipe_bukan_teks() -> None:
    with pytest.raises(TypeError):
        Penyewa(
            "Budi",
            "1406012509900001",
            buat_alamat(),
            1234567890,  # type: ignore[arg-type]
        )


def test_telepon_dapat_diubah_dengan_validasi() -> None:
    penyewa = buat_penyewa()
    penyewa.telepon = "081234567890"
    assert penyewa.telepon == "081234567890"


def test_alat_tani_menghitung_biaya() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_alat_tani_menghasilkan_keterangan() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.keterangan() == "[TR-01] Traktor - Rp150,000/hari"


def test_tarif_alat_menolak_nol() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_tarif_alat_menolak_tipe_bukan_integer() -> None:
    with pytest.raises(TypeError):
        AlatTani("TR-01", "Traktor", 150000.5)  # type: ignore[arg-type]


def test_tarif_alat_dapat_diubah_dengan_validasi() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    alat.tarif_harian = 200000
    assert alat.biaya_sewa(2) == 400000


def test_kode_alat_hanya_dapat_dibaca() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.kode = "TR-02"  # type: ignore[misc]


def test_nama_alat_hanya_dapat_dibaca() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    with pytest.raises(AttributeError):
        alat.nama = "Bajak"  # type: ignore[misc]


def test_petugas_menghasilkan_identitas() -> None:
    petugas = Petugas(
        "Andi Saputra",
        "198705102010011001",
        "Petugas Lapangan",
    )
    assert petugas.identitas() == (
        "Andi Saputra (198705102010011001) - Petugas Lapangan"
    )


def test_petugas_kontak() -> None:
    petugas = Petugas(
        "Andi Saputra",
        "198705102010011001",
        "Petugas Lapangan",
        "0813-9876-5432",
    )
    assert petugas.kontak() == (
        "Andi Saputra dapat dihubungi di 0813-9876-5432"
    )
