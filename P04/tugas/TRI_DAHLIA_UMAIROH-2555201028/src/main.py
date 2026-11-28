from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.petugas import IdentitasPetugas, Petugas


def main() -> None:
    alamat = Alamat("Kampung Baru", "Kuok", "Kuok")
    penyewa = Penyewa("Budi Santoso", "1401010101010001", alamat)
    alat = AlatTani("AT01", "Traktor", 100_000)
    petugas = Petugas("PT01", "Andi", IdentitasPetugas("andi@example.com"))

    print("=== DATA PENYEWA ===")
    print(penyewa.identitas())

    print("\n=== DATA ALAT TANI ===")
    print(f"Alat: {alat.nama} ({alat.kode})")
    print(f"Tarif: {AlatTani.format_rupiah(alat.tarif_harian)}")

    print("\n=== DATA PETUGAS ===")
    print(f"Petugas: {petugas.nama} - {petugas.status}")

    print("\n=== PENGUJIAN STATICMETHOD ===")
    print(f"Tarif Rp100.000 wajar: {AlatTani.tarif_wajar(100_000)}")
    print(f"Format rupiah: {AlatTani.format_rupiah(1_500_000)}")

    print("\n=== PENGUJIAN CLASSMETHOD ===")
    print(f"Jumlah alat terdaftar: {AlatTani.jumlah_terdaftar()}")

    alat_baru = AlatTani.dari_baris_csv("AT02;Combine Harvester;250000")
    print(f"Alat dari CSV: {alat_baru.nama} ({alat_baru.kode})")
    print(f"Jumlah alat terdaftar: {AlatTani.jumlah_terdaftar()}")

    print("\n=== PENGUJIAN VALIDASI TARIF ===")
    try:
        alat.tarif_harian = 0
    except ValueError as error:
        print(f"Perubahan tarif ditolak: {error}")


if __name__ == "__main__":
    main()