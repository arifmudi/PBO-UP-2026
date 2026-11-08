
"""Model kios UMKM yang menjual kebutuhan hasil pertanian."""

from typing import Final


class Kios:
    """Mengelola produk yang dijual oleh kios."""

    BATAS_HARGA_MINIMUM: Final[int] = 1_000
    BATAS_HARGA_MAKSIMUM: Final[int] = 10_000_000
    MARGIN_MINIMUM: Final[int] = 10
    PEMISAH_DATA: Final[str] = ";"
    JUMLAH_BAGIAN: Final[int] = 4

    _jumlah_produk: int = 0

    def __init__(
        self,
        kode: str,
        nama_produk: str,
        harga_modal: int,
        harga_jual: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("Kode produk tidak boleh kosong")

        if not nama_produk.strip():
            raise ValueError("Nama produk tidak boleh kosong")

        if not self.harga_wajar(harga_modal, harga_jual):
            raise ValueError("Harga produk tidak memenuhi aturan")

        self._kode = kode.strip()
        self._nama_produk = nama_produk.strip()
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual

        Kios._jumlah_produk += 1

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama_produk(self) -> str:
        return self._nama_produk

    @property
    def harga_modal(self) -> int:
        return self._harga_modal

    @property
    def harga_jual(self) -> int:
        return self._harga_jual

    @harga_jual.setter
    def harga_jual(self, nilai: int) -> None:
        if not self.harga_wajar(self._harga_modal, nilai):
            raise ValueError("Harga jual tidak memenuhi aturan margin")

        self._harga_jual = nilai

    @staticmethod
    def harga_wajar(harga_modal: int, harga_jual: int) -> bool:
        if not (
            Kios.BATAS_HARGA_MINIMUM
            <= harga_modal
            <= Kios.BATAS_HARGA_MAKSIMUM
        ):
            return False

        harga_minimum = (
            harga_modal
            + harga_modal * Kios.MARGIN_MINIMUM // 100
        )

        return (
            harga_minimum
            <= harga_jual
            <= Kios.BATAS_HARGA_MAKSIMUM
        )

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_produk(cls) -> int:
        return cls._jumlah_produk

    @classmethod
    def dari_baris(cls, baris: str) -> Kios:
        bagian = baris.strip().split(cls.PEMISAH_DATA)

        if len(bagian) != cls.JUMLAH_BAGIAN:
            raise ValueError("Data harus terdiri dari 4 bagian")

        kode, nama_produk, modal, jual = bagian

        modal_bersih = modal.strip().replace(".", "")
        jual_bersih = jual.strip().replace(".", "")

        if not modal_bersih.isdigit() or not jual_bersih.isdigit():
            raise ValueError("Harga harus berupa angka")

        return cls(
            kode.strip(),
            nama_produk.strip(),
            int(modal_bersih),
            int(jual_bersih),
        )

    def nilai_jual(self, jumlah: int) -> int:
        if jumlah <= 0:
            raise ValueError("Jumlah produk harus lebih dari nol")

        return self._harga_jual * jumlah

    def keuntungan(self, jumlah: int = 1) -> int:
        if jumlah <= 0:
            raise ValueError("Jumlah produk harus lebih dari nol")

        return (self._harga_jual - self._harga_modal) * jumlah

    def keterangan(self) -> str:
        return (
            f"[{self._kode}] {self._nama_produk:<20} "
            f"{self.format_rupiah(self._harga_jual):>15}"
        )
