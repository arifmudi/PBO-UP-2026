
"""Program utama penyewaan alat tani."""

from src.format_nilai import sebagai_teks
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor
from src.ui.perintah_konsol import PerintahKonsol


def main() -> None:
    """Menjalankan program daftar harga sewa alat tani."""
    alat: list[AlatTani] = [
        Traktor("TR-01", "Traktor Kubota", 150_000, 45),
        PompaAir("PA-01", "Pompa Air Honda", 80_000, 100),
        Perontok("PR-01", "Perontok Padi", 100_000, 10),
        AlatTani("AT-01", "Alat Pertanian Umum", 150_000),
    ]

    daftar = DaftarHarga(alat)
    perintah = PerintahKonsol(daftar)

    print("=== PROGRAM SEWA ALAT TANI ===")
    print("Contoh format nilai:", sebagai_teks(150000))
    print("Persentase:", sebagai_teks(0.15))
    print("Daftar nilai:", sebagai_teks([150000, 0.15]))

    print("\nKetik 'bantuan' untuk melihat perintah.")
    while True:
        masukan = input("\nPerintah: ").strip()

        if masukan.lower() in ("keluar", "exit"):
            print("Program selesai.")
            break

        print(perintah.jalankan(masukan))


if __name__ == "__main__":
    main()
