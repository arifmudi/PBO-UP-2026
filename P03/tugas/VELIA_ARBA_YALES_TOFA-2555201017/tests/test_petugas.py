
import pytest
from src.model.nomor_pegawai import NomorPegawai
from src.model.petugas import Petugas


def buat_petugas() -> Petugas:
    return Petugas(
        nama="Andi Saputra",
        nip="198705102010011001",
        jabatan="Petugas Lapangan",
        telepon="0813-9876-5432",
    )


def test_petugas_menyimpan_nama() -> None:
    petugas = buat_petugas()
    assert petugas.nama == "Andi Saputra"


def test_petugas_menyimpan_nomor_pegawai() -> None:
    petugas = buat_petugas()
    assert petugas.nomor_pegawai.nilai == "198705102010011001"


def test_petugas_menyimpan_jabatan() -> None:
    petugas = buat_petugas()
    assert petugas.jabatan == "Petugas Lapangan"


def test_petugas_menyimpan_telepon() -> None:
    petugas = buat_petugas()
    assert petugas.telepon == "0813-9876-5432"


def test_nama_petugas_tidak_dapat_diubah() -> None:
    petugas = buat_petugas()
    atribut = "nama"

    with pytest.raises(AttributeError):
        setattr(petugas, atribut, "Nama Baru")


def test_jabatan_petugas_tidak_dapat_diubah() -> None:
    petugas = buat_petugas()
    atribut = "jabatan"

    with pytest.raises(AttributeError):
        setattr(petugas, atribut, "Manajer")


def test_nomor_pegawai_petugas_tidak_dapat_diubah() -> None:
    petugas = buat_petugas()
    atribut = "nomor_pegawai"

    with pytest.raises(AttributeError):
        setattr(petugas, atribut, NomorPegawai("198705102010011002"))


def test_nomor_pegawai_tidak_dapat_diubah() -> None:
    nomor = NomorPegawai("198705102010011001")
    atribut = "nilai"

    with pytest.raises(AttributeError):
        setattr(nomor, atribut, "198705102010011002")


def test_nomor_pegawai_harus_18_digit() -> None:
    with pytest.raises(ValueError):
        NomorPegawai("12345")


def test_nomor_pegawai_harus_berupa_angka() -> None:
    with pytest.raises(ValueError):
        NomorPegawai("19870510201001100A")


def test_telepon_petugas_dapat_diubah() -> None:
    petugas = buat_petugas()
    petugas.telepon = "081234567890"

    assert petugas.telepon == "081234567890"


def test_telepon_petugas_boleh_tidak_dicantumkan() -> None:
    petugas = buat_petugas()
    petugas.telepon = "-"

    assert petugas.telepon == "-"


def test_telepon_petugas_menolak_nomor_tidak_valid() -> None:
    petugas = buat_petugas()

    with pytest.raises(ValueError):
        petugas.telepon = "12345"


def test_telepon_petugas_menolak_tipe_bukan_teks() -> None:
    petugas = buat_petugas()
    atribut = "telepon"

    with pytest.raises(TypeError):
        setattr(petugas, atribut, 81211112222)
