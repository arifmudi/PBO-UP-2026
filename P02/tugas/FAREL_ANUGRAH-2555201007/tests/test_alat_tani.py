from src.model.alat_tani import AlatTani


def test_biaya_sewa() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_keterangan_rupiah() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.keterangan() == "[TR-01] Traktor — Rp150.000/hari"


def test_biaya_sewa_nol_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(0) == 0


def test_setiap_objek_independen() -> None:
    traktor = AlatTani("TR-01", "Traktor", 150000)
    pompa = AlatTani("PM-01", "Pompa", 75000)
    assert traktor.biaya_sewa(1) == 150000
    assert pompa.biaya_sewa(1) == 75000
