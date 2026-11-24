
"""Model domain: alat yang disewakan UPJA."""

from typing import Final


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        """Membuat alat tani dan menghitung jumlah alat terdaftar."""
        if not kode.strip():
            raise ValueError("Kode alat tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama alat tidak boleh kosong.")

        self._kode = kode
        self._nama = nama
        self.tarif_harian = tarif_harian
        AlatTani._jumlah_terdaftar += 1

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if not AlatTani.tarif_wajar(nilai):
            minimum = AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)
            maksimum = AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)
            raise ValueError(
                f"Tarif harian harus antara {minimum} dan {maksimum}."
            )
        self._tarif_harian = nilai

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "AlatTani":
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 3:
            raise ValueError(
                "Baris CSV harus berisi kode, nama, dan tarif."
            )

        kode, nama, tarif = (item.strip() for item in bagian)

        if not tarif.isdigit():
            raise ValueError("Tarif harus berupa bilangan bulat.")

        return cls(kode, nama, int(tarif))

    def biaya_sewa(self, jumlah_hari: int) -> int:
        if jumlah_hari < 0:
            raise ValueError("Jumlah hari tidak boleh negatif.")
        return self._tarif_harian * jumlah_hari

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        if hari_terlambat < 0:
            raise ValueError("Hari keterlambatan tidak boleh negatif.")

        per_hari = (
            self._tarif_harian * AlatTani.PERSEN_DENDA_HARIAN // 100
        )
        return per_hari * hari_terlambat

    def keterangan(self) -> str:
        tarif = AlatTani.format_rupiah(self._tarif_harian)
        return f"[{self._kode}] {self._nama} — {tarif}/hari"

    def __str__(self) -> str:
        return self.keterangan()

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"kode={self._kode!r}, "
            f"nama={self._nama!r}, "
            f"tarif_harian={self._tarif_harian!r})"
        )

    def __eq__(self, lain: object) -> bool:
        if not isinstance(lain, AlatTani):
            return NotImplemented
        return self._kode == lain._kode

    def __hash__(self) -> int:
        return hash(self._kode)
