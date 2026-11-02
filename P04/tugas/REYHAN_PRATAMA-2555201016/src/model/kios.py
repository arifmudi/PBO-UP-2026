from typing import Final


class Kios:
    """Mewakili produk yang dijual oleh kios UMKM."""

    MARGIN_KEUNTUNGAN_PERSEN: Final[int] = 10
    HARGA_MINIMUM: Final[int] = 1_000
    HARGA_MAKSIMUM: Final[int] = 100_000_000
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_produk: int = 0

    def __init__(self, kode: str, nama: str, harga: int) -> None:
        if not kode.strip():
            raise ValueError("Kode produk tidak boleh kosong")

        if not nama.strip():
            raise ValueError("Nama produk tidak boleh kosong")

        if not self.harga_wajar(harga):
            raise ValueError("Harga produk tidak wajar")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._harga = harga

        Kios._jumlah_produk += 1

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def harga(self) -> int:
        return self._harga

    def harga_jual(self) -> int:
        """Menghitung harga jual berdasarkan margin keuntungan."""
        return self._harga + (
            self._harga * self.MARGIN_KEUNTUNGAN_PERSEN // 100
        )

    @staticmethod
    def harga_wajar(nilai: int) -> bool:
        """Memeriksa apakah harga produk masih dalam batas wajar."""
        return (
            isinstance(nilai, int)
            and not isinstance(nilai, bool)
            and Kios.HARGA_MINIMUM <= nilai <= Kios.HARGA_MAKSIMUM
        )

    @classmethod
    def jumlah_produk(cls) -> int:
        """Mengembalikan jumlah produk yang berhasil didaftarkan."""
        return cls._jumlah_produk

    @classmethod
    def dari_baris(cls, baris: str) -> "Kios":
        """Membuat objek Kios dari baris data yang dipisahkan titik koma."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 3:
            raise ValueError(
                "Baris harus berisi kode, nama, dan harga"
            )

        kode, nama, harga = bagian

        try:
            nilai_harga = int(harga.strip())
        except ValueError as exc:
            raise ValueError("Harga harus berupa angka") from exc

        return cls(kode.strip(), nama.strip(), nilai_harga)

    def informasi(self) -> str:
        """Menampilkan informasi produk dengan format rapi."""
        return (
            f"{self._kode:<10} | "
            f"{self._nama:<20} | "
            f"Rp{self.harga_jual():>12,}".replace(",", ".")
        )