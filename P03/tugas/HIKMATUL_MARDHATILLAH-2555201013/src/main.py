"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.alamat import Alamat


def main() -> None:
    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        Alamat("Pulau Jambu", "Kuok", "Kuok"),
        "0812-3456-7890",
    )

    siti = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        Alamat("Dusun I", "Salo", "Salo"),
    )

    traktor = AlatTani(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150000,
    )

    pompa = AlatTani(
        "PA-01",
        "Pompa Air 3 Inci",
        75000,
    )

    print(budi.identitas())
    print(budi.alamat.lengkap())
    print(budi.kontak())
    print(siti.kontak())
    print(traktor.keterangan())
    print("--- Percobaan menembus penjagaan ---")

    for tarif in (0, -5000):
        try:
            AlatTani("TR-02", "Traktor Uji", tarif)
        except ValueError as e:
            label = "nol" if tarif == 0 else "minus"
            print(f"Ditolak (tarif {label}): {e}")

    print(f"Tarif tetap utuh: {traktor.keterangan()}")


if __name__ == "__main__":
    main()