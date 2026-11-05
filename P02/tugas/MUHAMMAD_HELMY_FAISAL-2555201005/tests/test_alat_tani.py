"""Pengujian untuk kelas AlatTani."""

from src.model.alat_tani import AlatTani


def test_biaya_sewa_tiga_hari() -> None:
    alat = AlatTani("TR-01", "Traktor Roda Dua", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_dua_objek_punya_data_sendiri() -> None:
    a = AlatTani("TR-01", "Traktor", 150000)
    b = AlatTani("PA-01", "Pompa", 75000)
    assert a.biaya_sewa(1) != b.biaya_sewa(1)


def test_biaya_sewa_gratis() -> None:
    alat = AlatTani("CG-01", "Cangkul", 0)
    assert alat.biaya_sewa(7) == 0


def test_keterangan_tarif_ribuan() -> None:
    alat = AlatTani("SB-01", "Mesin Babat Rumput", 5000)
    assert alat.keterangan() == "[SB-01] Mesin Babat Rumput — Rp5.000/hari"