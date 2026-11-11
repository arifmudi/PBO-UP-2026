
"""Program utama praktikum P04."""

from src.model.alat_tani import AlatTani


def main() -> None:
    """Menampilkan demonstrasi fitur kelas AlatTani."""
    print(f"Sebelum mendaftarkan alat: {AlatTani.jumlah_terdaftar()}")

    alat_1 = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150_000)
    alat_2 = AlatTani("PA-01", "Pompa Air 3 Inci", 75_000)

    alat_3 = AlatTani.dari_baris_csv("AL-01;Alat Semprot;50000")
    alat_4 = AlatTani.dari_baris_csv("KM-01;Mesin Panen;250000")

    print(alat_1.keterangan())
    print(alat_2.keterangan())
    print(f"Setelah mendaftarkan alat: {AlatTani.jumlah_terdaftar()}")

    print("\n--- Pemeriksaan tarif tanpa membuat objek ---")
    calon_tarif = [5_000, 150_000, 6_000_000]

    for tarif in calon_tarif:
        format_tarif = AlatTani.format_rupiah(tarif)
        if AlatTani.tarif_wajar(tarif):
            status = "wajar"
        else:
            status = "ditolak"

        print(f"{format_tarif:>14} -> {status}")

    print("\n--- Denda keterlambatan ---")
    print(
        f"Denda 2 hari untuk {alat_1.nama}: "
        f"{AlatTani.format_rupiah(alat_1.denda_keterlambatan(2))}"
    )


if __name__ == "__main__":
    main()
