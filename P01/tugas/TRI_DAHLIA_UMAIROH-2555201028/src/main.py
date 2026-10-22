from src.model.alamat import Alamat
from src.model.penyewa import Penyewa


def main() -> None:
    alamat = Alamat(
        dusun="Dusun I",
        desa="Kuok",
        kecamatan="Kuok",
    )

    penyewa = Penyewa(
        nama="Budi Santoso",
        nik="1234567890123456",
        alamat=alamat,
    )

    print(penyewa.identitas())


if __name__ == "__main__":
    main()