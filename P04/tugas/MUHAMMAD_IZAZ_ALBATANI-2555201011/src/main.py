"""Program utama praktikum P04."""

from src.model.alat_tani import AlatTani


def main() -> None:
    """Menampilkan fitur milik kelas dan milik objek."""
    print("=== PRAKTIKUM P04: ALAT TANI ===")

    awal = AlatTani.jumlah_terdaftar()

    alat1 = AlatTani(
        "PA-01",
        "Pompa Air 3 Inci",
        75_000,
    )

    alat2 = AlatTani.dari_baris_csv(
        "TR-01;Traktor Roda Empat;250000"
    )

    print("\nDaftar Alat:")
    print(f"{alat1.keterangan():>45}")
    print(f"{alat2.keterangan():>45}")

    print("\nInformasi Kelas:")
    print(
        f"Tarif minimum : "
        f"{AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)}"
    )
    print(
        f"Tarif maksimum: "
        f"{AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)}"
    )
    print(
        f"Jumlah alat   : "
        f"{AlatTani.jumlah_terdaftar() - awal}"
    )

    print("\nPerhitungan:")
    print(
        f"Biaya sewa 3 hari : "
        f"{AlatTani.format_rupiah(alat1.biaya_sewa(3))}"
    )
    print(
        f"Denda terlambat 2 hari: "
        f"{AlatTani.format_rupiah(alat1.denda_keterlambatan(2))}"
    )

    print("\nPemeriksaan Tarif:")

    for tarif in (5_000, 150_000, 6_000_000):
        status = (
            "WAJAR"
            if AlatTani.tarif_wajar(tarif)
            else "TIDAK WAJAR"
        )

        print(
            f"{AlatTani.format_rupiah(tarif):>14} : {status}"
        )


if __name__ == "__main__":
    main()
