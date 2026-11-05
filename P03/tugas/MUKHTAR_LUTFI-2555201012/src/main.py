
"""Program utama untuk demonstrasi penyewaan alat pertanian."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    """Menjalankan contoh penyewaan alat pertanian."""
    traktor = AlatTani("ALT001", "Traktor", 250_000)

    budi = Penyewa(
        "1406012509900001",
        "Budi Santoso",
        Alamat("Suka Maju", "Kuok", "Kampar"),
        "0812-3456-7890",
    )

    siti = Penyewa(
        "1406014403950002",
        "Siti Aminah",
        Alamat("Dusun Satu", "Salo", "Kampar"),
    )

    print("=== SISTEM PENYEWAAN ALAT PERTANIAN ===")
    print(traktor.keterangan())
    print(budi.identitas())
    print(budi.kontak())
    print(siti.identitas())
    print(siti.kontak())
    print(f"Biaya sewa 2 hari: Rp{traktor.biaya_sewa(2):,}".replace(",", "."))


if __name__ == "__main__":
    main()
