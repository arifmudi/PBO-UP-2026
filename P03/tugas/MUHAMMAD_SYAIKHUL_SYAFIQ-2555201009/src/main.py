
"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    alamat_budi = Alamat("Pulau Belimbing", "Kuok", "Kuok")
    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        alamat_budi,
        "0812-3456-7890",
    )

    alamat_siti = Alamat("Salo Timur", "Salo", "Salo")
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

    print("--- Data penyewa ---")
    print(budi.identitas())
    print(budi.alamat.lengkap())
    print(budi.kontak())
    print(siti.identitas())
    print(siti.kontak())

    print("\n--- Data alat ---")
    print(traktor.keterangan())

    print("\n--- Percobaan menembus penjagaan ---")
    try:
        traktor.tarif_harian = -5000
    except ValueError as kesalahan:
        print(f"Ditolak (tarif minus): {kesalahan}")

    print(f"Tarif tetap utuh: {traktor.keterangan()}")

    try:
        Penyewa("123", "Nama Uji", alamat_budi)
    except ValueError as kesalahan:
        print(f"Ditolak (NIK tidak valid): {kesalahan}")


if __name__ == "__main__":
    main()
