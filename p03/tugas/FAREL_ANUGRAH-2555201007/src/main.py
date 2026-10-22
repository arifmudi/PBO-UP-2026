"""Titik masuk program P03: enkapsulasi dan objek nilai."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    alamat_budi = Alamat(
        dusun="Pongkai",
        desa="Kuok",
        kecamatan="Kuok",
    )
    alamat_siti = Alamat(
        dusun="Salo",
        desa="Salo",
        kecamatan="Salo",
    )

    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat_budi,
        "0812-3456-7890",
    )
    siti = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        alamat_siti,
    )

    traktor = AlatTani(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150000,
    )

    print(budi.identitas())
    print(budi.kontak())
    print(siti.identitas())
    print(siti.kontak())
    print(traktor.keterangan())


if __name__ == "__main__":
    main()