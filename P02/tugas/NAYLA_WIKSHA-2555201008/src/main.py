
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    """Menampilkan informasi penyewa dan alat pertanian."""
    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        "Kuok",
        "0812-3456-7890",
    )
    siti = Penyewa(
        "1406012509900002",
        "Siti Aminah",
        "Bangkinang",
    )

    traktor = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)
    pompa = AlatTani("PM-01", "Pompa Air", 75000)

    print(budi.identitas())
    print(budi.kontak())
    print(siti.kontak())
    print(traktor.keterangan())
    print(f"Biaya sewa traktor selama 3 hari: Rp{traktor.biaya_sewa(3):,}".replace(",", "."))
    print(pompa.keterangan())


if __name__ == "__main__":
    main()
