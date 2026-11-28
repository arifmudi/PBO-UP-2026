
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor
from src.ui.perintah_konsol import PerintahKonsol


def main() -> None:
    """Menjalankan program daftar harga sewa alat pertanian."""

    alat = [
        Traktor("TR-01", "Traktor Roda Dua Kubota", 150_000, 8),
        PompaAir("PA-01", "Pompa Air 3 Inci", 75_000, 100),
        Perontok("PR-01", "Mesin Perontok Padi", 50_000, 500),
    ]

    daftar = DaftarHarga(alat)
    konsol = PerintahKonsol(daftar)

    print("=== SISTEM DAFTAR HARGA SEWA ALAT PERTANIAN ===")
    print("Ketik 'bantuan' untuk melihat daftar perintah.")
    print("Ketik 'keluar' untuk mengakhiri program.")

    while True:
        perintah = input("\nPerintah: ").strip()

        if perintah.lower() == "keluar":
            print("Program selesai.")
            break

        print(konsol.jalankan(perintah))


if __name__ == "__main__":
    main()
