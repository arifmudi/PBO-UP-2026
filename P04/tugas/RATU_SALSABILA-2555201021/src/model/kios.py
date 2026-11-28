"""Model domain: kios penjualan hasil pertanian."""

from typing import Final


class Kios:
    """Mewakili produk hasil pertanian yang dijual di kios."""

    PERSEN_MARGIN_MINIMUM: Final[int] = 15
    HARGA_MINIMUM: Final[int] = 1_000
    STOK_MINIMUM: Final[int] = 0
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_terdaftar: int = 0

    def __init__(
        self,
        kode: str,
        nama: str,
        harga_beli: int,
        harga_jual: int,
        stok: int,
    ) -> None:
        """Membuat produk baru dan menghitung jumlah produk terdaftar."""
        if not kode.strip():
            raise ValueError("Kode produk tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama produk tidak boleh kosong.")
        if harga_beli < self.HARGA_MINIMUM:
            raise ValueError("Harga beli tidak valid.")
        if not self.harga_jual_wajar(harga_beli, harga_jual):
            raise ValueError("Harga jual tidak memenuhi margin minimum.")
        if stok < self.STOK_MINIMUM:
            raise ValueError("Stok tidak boleh negatif.")

        self._kode = kode.strip()
        self._nama = nama.strip()
        self._harga_beli = harga_beli
        self._harga_jual = harga_jual
        self._stok = stok

        Kios._jumlah_terdaftar += 1

    @property
    def kode(self) -> str:
        """Mengembalikan kode produk."""
        return self._kode

    @property
    def nama(self) -> str:
        """Mengembalikan nama produk."""
        return self._nama

    @property
    def harga_beli(self) -> int:
        """Mengembalikan harga beli produk."""
        return self._harga_beli

    @property
    def harga_jual(self) -> int:
        """Mengembalikan harga jual produk."""
        return self._harga_jual

    @property
    def stok(self) -> int:
        """Mengembalikan jumlah stok produk."""
        return self._stok

    @staticmethod
    def harga_jual_wajar(harga_beli: int, harga_jual: int) -> bool:
        """Memeriksa apakah harga jual memenuhi margin minimum."""
        if harga_beli < Kios.HARGA_MINIMUM:
            return False

        minimum = (
            harga_beli * (100 + Kios.PERSEN_MARGIN_MINIMUM) + 99
        ) // 100

        return harga_jual >= minimum

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi format rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah produk yang telah didaftarkan."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "Kios":
        """Membuat produk dari teks kode;nama;harga_beli;harga_jual;stok."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 5:
            raise ValueError("Baris harus berisi lima bagian.")

        kode, nama, beli, jual, stok = (
            item.strip() for item in bagian
        )

        if not beli.isdigit() or not jual.isdigit() or not stok.isdigit():
            raise ValueError("Harga dan stok harus berupa bilangan bulat.")

        return cls(kode, nama, int(beli), int(jual), int(stok))

    def keterangan(self) -> str:
        """Mengembalikan informasi produk."""
        return (
            f"[{self._kode}] {self._nama} — "
            f"{self.format_rupiah(self._harga_jual)}"
        )

    def baris_daftar(self) -> str:
        """Menghasilkan informasi produk dengan kolom rata."""
        return (
            f"{self._kode:<10} "
            f"{self._nama:<20} "
            f"{self.format_rupiah(self._harga_jual):>15} "
            f"{self._stok:>8}"
        )