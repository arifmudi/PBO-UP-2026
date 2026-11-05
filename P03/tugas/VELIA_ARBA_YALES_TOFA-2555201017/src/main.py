
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.petugas import Petugas


def main() -> None:
    alamat_1 = Alamat(
        "Dusun Suka Maju",
        "Kuok",
        "Kuok",
    )
    alamat_2 = Alamat(
        "Dusun Bangkinang",
        "Bangkinang",
        "Bangkinang",
    )

    penyewa_1 = Penyewa(
        "Budi Santoso",
        "1406012509900001",
        alamat_1,
        "0812-3456-7890",
    )

    penyewa_2 = Penyewa(
        "Siti Aminah",
        "1406012509900002",
        alamat_2,
    )

    alat = AlatTani(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150000,
    )

    petugas = Petugas(
        "Andi Saputra",
        "198705102010011001",
        "Petugas Lapangan",
        "0813-9876-5432",
    )

    print(penyewa_1.identitas())
    print(penyewa_1.kontak())
    print(penyewa_2.identitas())
    print(penyewa_2.kontak())

    print(alat.keterangan())
    print(f"Biaya sewa 3 hari: Rp{alat.biaya_sewa(3):,}")

    print(petugas.identitas())
    print(petugas.kontak())


if __name__ == "__main__":
    main()
