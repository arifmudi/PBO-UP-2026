
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    alamat_budi = Alamat("Pulau Jambu", "Kuok", "Kuok")

    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat_budi,
        "0812-3456-7890",
    )

    traktor = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)

    print(budi.identitas())
    print(alamat_budi.lengkap())
    print(traktor.keterangan())

    print("--- Percobaan menembus penjagaan ---")

    try:
        traktor.tarif_harian = 0
    except ValueError as e:
        print("Ditolak (tarif nol):", e)

    try:
        traktor.tarif_harian = -5000
    except ValueError as e:
        print("Ditolak (tarif minus):", e)

    print("Tarif tetap utuh:", traktor.keterangan())


if __name__ == "__main__":
    main()
