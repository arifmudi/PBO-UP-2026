"""Program utama praktikum P06."""

from src.model.alamat import Alamat
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa
from src.model.traktor import Traktor
from src.model.pompa_air import PompaAir
from src.model.perontok import Perontok

def main() -> None:
    """Menampilkan demonstrasi penyewaan tiga jenis alat tani."""
    alamat = Alamat("Suka Maju", "Kumantan", "Bangkinang Kota")
    penyewa = Penyewa(
        "1400000000000001",
        "Ratu Salsabila",
        alamat,
        "081234567890",
    )

    traktor = Traktor(
        "TR-01",
        "Traktor Roda Dua",
        150_000,
        8,
    )
    pompa = PompaAir(
        "PA-01",
        "Pompa Air",
        75_000,
        600,
    )
    perontok = Perontok(
        "PR-01",
        "Mesin Perontok Padi",
        200_000,
        900,
    )

    sewa = Sewa("SW-001", penyewa)
    sewa.tambah_alat(traktor, 1)
    sewa.tambah_alat(pompa, 1)
    sewa.tambah_alat(perontok, 1)

    print("--- NOTA PENYEWAAN ALAT TANI P06 ---")
    print(sewa.nota())

if __name__ == "__main__":
    main()