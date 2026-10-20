
"""Pengujian untuk kelas AlatTani."""

from src.model.alat_tani import AlatTani


def test_biaya_sewa_satu_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(1) == 150000


def test_biaya_sewa_beberapa_hari() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.biaya_sewa(3) == 450000


def test_keterangan_memuat_nama_alat() -> None:
    alat = AlatTani("PA-01", "Pompa Air", 75000)
    assert "Pompa Air" in alat.keterangan()
