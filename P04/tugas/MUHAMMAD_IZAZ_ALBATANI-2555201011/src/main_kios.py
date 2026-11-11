"""Program utama demonstrasi kelas Kios."""

from src.model.kios import Kios


def main() -> None:
    print("=== PRAKTIKUM P04: KIOS UMKM ===")

    produk_kios = [
        Kios("BR-01", "Beras", 10_000, 11_000),
        Kios("GL-01", "Gula Pasir", 14_000, 15_400),
        Kios("MY-01", "Minyak Goreng", 16_000, 17_600),
    ]

    print("\nDaftar Produk:")
    print(f"{'Kode':<10}{'Nama Produk':<22}{'Harga Jual':>15}")

    for produk in produk_kios:
        print(produk.keterangan())

    print("\nInformasi Kelas:")
    print(f"Margin minimum : {Kios.MARGIN_MINIMUM}%")
    print(f"Jumlah produk  : {Kios.jumlah_produk()}")

    print("\nPerhitungan:")
    print(
        "Nilai jual 5 kg beras :",
        Kios.format_rupiah(produk_kios[0].nilai_jual(5)),
    )
    print(
        "Keuntungan 5 kg beras :",
        Kios.format_rupiah(produk_kios[0].keuntungan(5)),
    )

    print("\nPemeriksaan Harga:")
    print("Modal Rp10.000, jual Rp11.000:",
          "WAJAR" if Kios.harga_wajar(10_000, 11_000) else "TIDAK WAJAR")
    print("Modal Rp10.000, jual Rp10.500:",
          "WAJAR" if Kios.harga_wajar(10_000, 10_500) else "TIDAK WAJAR")


if __name__ == "__main__":
    main()
