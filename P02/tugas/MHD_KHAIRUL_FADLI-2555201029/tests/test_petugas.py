from src.model.petugas import Petugas


def test_petugas_identitas() -> None:
    petugas = Petugas("PT-01", "Ahmad", "Ketua")

    assert petugas.identitas() == "Ahmad (PT-01) — Ketua"


def test_petugas_kontak() -> None:
    petugas = Petugas("PT-02", "Budi", "Operator", "0812-1111-2222")

    assert petugas.kontak() == "Budi dapat dihubungi di 0812-1111-2222"


def test_data_petugas_independen() -> None:
    petugas_a = Petugas("PT-03", "Citra", "Admin")
    petugas_b = Petugas("PT-04", "Dedi", "Operator")

    assert petugas_a.identitas() != petugas_b.identitas()
    assert petugas_a.kontak() != petugas_b.kontak()
