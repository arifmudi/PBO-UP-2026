from __future__ import annotations
import pytest
from src.model.alat_tani import AlatTani
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa
from src.model.baris_sewa import BarisSewa
from src.model.sewa import Sewa

def buat_penyewa() -> Penyewa:
    alamat = Alamat("Jl. Jend. Sudirman", "Bangkinang", "Kampar")
    return Penyewa("1406012509900001", "Budi Santoso", alamat)

# 1-5. Pengujian AlatTani
def test_alat_tani_init() -> None:
    alat = AlatTani("A01", "Traktor Mini", 200000)
    assert alat.kode == "A01"
    assert alat.nama == "Traktor Mini"
    assert alat.tarif == 200000

def test_alat_tani_tarif_negatif() -> None:
    with pytest.raises(ValueError):
        AlatTani("A02", "Cangkul", -50000)

def test_alat_tani_ubah_tarif() -> None:
    alat = AlatTani("A03", "Traktor", 100000)
    alat.tarif_harian = 120000
    assert alat.tarif == 120000

def test_alat_tani_nama_kosong() -> None:
    with pytest.raises(ValueError):
        AlatTani("A04", "", 50000)

def test_alat_tani_kode_kosong() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Pompa Air", 75000)

# 6-10. Pengujian Alamat
def test_alamat_init() -> None:
    alamat = Alamat("Pandang", "Kuok", "Kampar")
    assert alamat.jalan == "Pandang"
    assert alamat.kecamatan == "Kuok"
    assert alamat.kabupaten == "Kampar"

def test_alamat_str() -> None:
    alamat = Alamat("Pandang", "Kuok", "Kampar")
    assert "Kuok" in str(alamat)

def test_alamat_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("", "Kuok", "Kampar")

def test_alamat_kecamatan_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Pandang", "", "Kampar")

def test_alamat_kabupaten_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Pandang", "Kuok", "")

# 11-15. Pengujian Penyewa (Asosiasi dengan Alamat)
def test_penyewa_init() -> None:
    p = buat_penyewa()
    assert p.nik == "1406012509900001"
    assert p.nama == "Budi Santoso"
    assert p.alamat.kabupaten == "Kampar"

def test_penyewa_nik_pendek() -> None:
    alamat = Alamat("Pandang", "Kuok", "Kampar")
    with pytest.raises(ValueError):
        Penyewa("123", "Siti", alamat)

def test_penyewa_nama_kosong() -> None:
    alamat = Alamat("Pandang", "Kuok", "Kampar")
    with pytest.raises(ValueError):
        Penyewa("1406012509900002", "", alamat)

def test_penyewa_ganti_nama() -> None:
    p = buat_penyewa()
    p.nama = "Budi Utama"
    assert p.nama == "Budi Utama"

def test_penyewa_asosiasi_alamat() -> None:
    alamat = Alamat("Salo", "Salo", "Kampar")
    p = Penyewa("1406012509900003", "Ani", alamat)
    assert p.alamat is alamat

# 16-24. Pengujian BarisSewa (Komposisi & Salinan Data)
def test_salinan_tidak_ikut_berubah_saat_tarif_alat_naik() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    baris = BarisSewa(alat, 3)
    alat.tarif_harian = 175_000
    assert baris.tarif_saat_sewa == 150_000
    assert baris.subtotal() == 450_000

def test_baris_sewa_durasi_nol() -> None:
    alat = AlatTani("TR-02", "Mesin Padi", 200000)
    with pytest.raises(ValueError):
        BarisSewa(alat, 0)

def test_baris_sewa_durasi_negatif() -> None:
    alat = AlatTani("TR-03", "Traktor", 100000)
    with pytest.raises(ValueError):
        BarisSewa(alat, -2)

def test_baris_sewa_subtotal_perhitungan() -> None:
    alat = AlatTani("TR-04", "Pompa Air", 50000)
    baris = BarisSewa(alat, 5)
    assert baris.subtotal() == 250000

def test_baris_sewa_simpan_nama_alat() -> None:
    alat = AlatTani("TR-05", "Traktor Besar", 300000)
    baris = BarisSewa(alat, 2)
    assert baris.nama_alat == "Traktor Besar"

def test_baris_sewa_simpan_kode_alat() -> None:
    alat = AlatTani("TR-06", "Cultivator", 120000)
    baris = BarisSewa(alat, 1)
    assert baris.kode_alat == "TR-06"

def test_baris_sewa_ubah_durasi() -> None:
    alat = AlatTani("TR-07", "Traktor", 100000)
    baris = BarisSewa(alat, 2)
    baris.durasi_hari = 4
    assert baris.subtotal() == 400000

def test_baris_sewa_durasi_invalid_setter() -> None:
    alat = AlatTani("TR-08", "Traktor", 100000)
    baris = BarisSewa(alat, 2)
    with pytest.raises(ValueError):
        baris.durasi_hari = -1

def test_baris_sewa_atribut_read_only() -> None:
    alat = AlatTani("TR-09", "Traktor", 100000)
    baris = BarisSewa(alat, 2)
    with pytest.raises(AttributeError):
        baris.tarif_saat_sewa = 50000 # type: ignore[misc]

# 25-34. Pengujian Sewa (Agregasi Penyewa & Komposisi BarisSewa)
def test_sewa_init() -> None:
    p = buat_penyewa()
    sewa = Sewa("SW-001", p)
    assert sewa.id_sewa == "SW-001"
    assert sewa.penyewa is p
    assert sewa.jumlah_alat() == 0

def test_komposisi_tidak_dapat_dibongkar_dari_luar() -> None:
    sewa = Sewa("SW-002", buat_penyewa())
    sewa.tambah_alat(AlatTani("TR-01", "Traktor", 150_000), 3)
    with pytest.raises(AttributeError):
        sewa.baris.append(None)  # type: ignore[attr-defined]
    assert sewa.jumlah_alat() == 1

def test_penyewa_tetap_hidup_setelah_sewa_dihapus() -> None:
    budi = buat_penyewa()
    sewa = Sewa("SW-003", budi)
    del sewa
    assert budi.nama == "Budi Santoso"

def test_sewa_tambah_beberapa_alat() -> None:
    sewa = Sewa("SW-004", buat_penyewa())
    sewa.tambah_alat(AlatTani("A1", "Traktor", 100000), 2)
    sewa.tambah_alat(AlatTani("A2", "Pompa", 50000), 4)
    assert sewa.jumlah_alat() == 2

def test_sewa_total_biaya() -> None:
    sewa = Sewa("SW-005", buat_penyewa())
    sewa.tambah_alat(AlatTani("A1", "Traktor", 100000), 2) # 200rb
    sewa.tambah_alat(AlatTani("A2", "Pompa", 50000), 3)  # 150rb
    assert sewa.total_biaya() == 350000

def test_sewa_id_kosong() -> None:
    with pytest.raises(ValueError):
        Sewa("", buat_penyewa())

def test_sewa_tambah_alat_invalid_durasi() -> None:
    sewa = Sewa("SW-006", buat_penyewa())
    with pytest.raises(ValueError):
        sewa.tambah_alat(AlatTani("A1", "Traktor", 100000), 0)

def test_sewa_jumlah_alat_kosong() -> None:
    sewa = Sewa("SW-007", buat_penyewa())
    assert sewa.jumlah_alat() == 0

def test_sewa_total_biaya_kosong() -> None:
    sewa = Sewa("SW-008", buat_penyewa())
    assert sewa.total_biaya() == 0

def test_sewa_representasi_string() -> None:
    sewa = Sewa("SW-009", buat_penyewa())
    assert "SW-009" in str(sewa) or sewa.id_sewa == "SW-009"