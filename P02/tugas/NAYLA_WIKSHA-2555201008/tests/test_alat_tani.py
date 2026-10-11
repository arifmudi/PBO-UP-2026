
from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_biaya_sewa_satu_hari() -> None:
    alat = AlatTani("PM-01", "Pompa Air", 75000)
    assert alat.biaya_sewa(1) == 75000


def test_keterangan_alat() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)
    assert alat.keterangan() == "[TR-01] Traktor Roda Dua Kubota — Rp150.000/hari"


def test_dua_objek_punya_data_sendiri() -> None:
    traktor = AlatTani("TR-01", "Traktor", 150000)
    pompa = AlatTani("PM-01", "Pompa Air", 75000)

    assert traktor.biaya_sewa(2) == 300000
    assert pompa.biaya_sewa(2) == 150000
