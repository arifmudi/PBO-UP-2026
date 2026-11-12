
import pytest

from src.model.pegawai import Pegawai
from src.model.pegawai_tetap import PegawaiTetap
from src.model.pegawai_harian import PegawaiHarian
from src.model.pegawai_kontrak import PegawaiKontrak


def test_pegawai_dapat_dibuat() -> None:
    pegawai = Pegawai("PG001", "Andi", 3_000_000)
    assert str(pegawai) == "Andi (NIP: PG001)"


def test_pegawai_menghitung_penghasilan() -> None:
    pegawai = Pegawai("PG001", "Andi", 3_000_000)
    assert pegawai.hitung_penghasilan(2) == 6_000_000


def test_pegawai_tetap_mendapat_tunjangan() -> None:
    pegawai = PegawaiTetap("PG002", "Budi", 3_000_000, 500_000)
    assert pegawai.hitung_penghasilan(2) == 7_000_000


def test_pegawai_harian_menghitung_tarif() -> None:
    pegawai = PegawaiHarian("PG003", "Citra", 2_000_000, 150_000)
    assert pegawai.hitung_penghasilan(2) == 6_600_000


def test_pegawai_kontrak_minimum_dua_bulan() -> None:
    pegawai = PegawaiKontrak("PG004", "Dedi", 4_000_000, "KTR-01")
    assert pegawai.hitung_penghasilan(1) == 8_000_000


def test_pegawai_kontrak_tiga_bulan() -> None:
    pegawai = PegawaiKontrak("PG005", "Eka", 4_000_000, "KTR-02")
    assert pegawai.hitung_penghasilan(3) == 12_000_000


def test_repr_pegawai() -> None:
    pegawai = Pegawai("PG006", "Fani", 3_000_000)
    assert "Pegawai(" in repr(pegawai)
    assert "PG006" in repr(pegawai)


def test_dua_pegawai_dengan_nip_sama_dianggap_sama() -> None:
    a = Pegawai("PG007", "Gilang", 3_000_000)
    b = Pegawai("PG007", "Gilang Lain", 4_000_000)
    assert a == b


def test_pegawai_dengan_nip_berbeda_tidak_sama() -> None:
    a = Pegawai("PG008", "Hani", 3_000_000)
    b = Pegawai("PG009", "Hani", 3_000_000)
    assert a != b


def test_pegawai_dapat_dijadikan_kunci_dict() -> None:
    a = Pegawai("PG010", "Indra", 3_000_000)
    catatan = {a: "Aktif"}
    b = Pegawai("PG010", "Indra Lain", 4_000_000)
    assert catatan[b] == "Aktif"


def test_pegawai_dibandingkan_dengan_teks() -> None:
    pegawai = Pegawai("PG011", "Joko", 3_000_000)
    assert pegawai != "PG011"


def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Kiki", 3_000_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("PG012", "", 3_000_000)


def test_gaji_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("PG013", "Lina", 0)


def test_tunjangan_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap("PG014", "Maya", 3_000_000, -100_000)
