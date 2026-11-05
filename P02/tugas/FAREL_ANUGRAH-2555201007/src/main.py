"""Titik masuk program P02."""

from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.petugas import Petugas


def main() -> None:
    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        "Kuok",
        "0812-3456-7890",
    )
    siti = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        "Salo",
    )
    traktor = AlatTani(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150000,
    )
    andi = Petugas(
        "P001",
        "Andi",
        "Admin UPJA",
        "081234567890",
    )

    print(budi.identitas())
    print(budi.kontak())
    print(siti.kontak())
    print(traktor.keterangan())
    print(andi.identitas())
    print(andi.kontak())


if __name__ == "__main__":
    main()
