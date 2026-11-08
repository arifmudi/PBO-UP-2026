"""Titik masuk program. Satu-satunya berkas yang boleh mencetak."""

from src.model.alat_tani import AlatTani
from src.model.alamat import Alamat
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def main() -> None:
    print(
        f"Sebelum pendataan, alat terdaftar: "
        f"{AlatTani.jumlah_terdaftar()}"
    )

    traktor = AlatTani(
        "TR-01",
        "Traktor Roda Dua Kubota",
        150_000,
    )
    pompa = AlatTani(
        "PA-01",
        "Pompa Air 3 Inci",
        75_000,
    )

    alamat = Alamat(
        dusun="-",
        desa="Kuok",
        kecamatan="Kuok",
    )

    penyewa = Penyewa(
        nik="1406012509900001",
        nama="Budi Santoso",
        alamat=alamat,
    )

    sewa = Sewa(
        nomor="SW-2026-001",
        penyewa=penyewa,
    )

    sewa.tambah_alat(traktor, 3)
    sewa.tambah_alat(pompa, 5)

    AlatTani.dari_baris_csv("TR-02;Traktor Roda Dua;200000")
    AlatTani.dari_baris_csv("PA-02;Pompa Air;100000")

    print(traktor.keterangan())
    print(pompa.keterangan())

    print(
        f"Sesudah pendataan, alat terdaftar: "
        f"{AlatTani.jumlah_terdaftar()}"
    )

    print("--- Memeriksa tarif tanpa membuat objek ---")
    for calon in (5_000, 150_000, 6_000_000):
        status = "wajar" if AlatTani.tarif_wajar(calon) else "ditolak"
        print(f" {AlatTani.format_rupiah(calon):>14} → {status}")

    print("\n" + sewa.nota())


if __name__ == "__main__":
    main()