
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    Ratu = Penyewa(
        "2555201021",
        "Ratu Salsabila",
        "Kumantan",
        "0831-3275-5771",
    )
    Nayla = Penyewa("1406014403950002", "Nayla Wikhsa", "Uway")

    traktor = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)
    pompa = AlatTani("PA-01", "Pompa Air 3 Inci", 75000)

    print(Ratu.identitas())
    print(Ratu.kontak())
    print(Nayla.kontak())
    print(traktor.keterangan())


if __name__ == "__main__":
    main()
