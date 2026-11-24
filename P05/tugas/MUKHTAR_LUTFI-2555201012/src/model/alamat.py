
"""Objek nilai untuk menyimpan alamat penyewa."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Alamat:
    """Alamat penyewa yang nilainya tidak dapat diubah."""

    dusun: str
    desa: str
    kecamatan: str

    def __post_init__(self) -> None:
        if not self.desa.strip():
            raise ValueError("Desa tidak boleh kosong.")

        if not self.kecamatan.strip():
            raise ValueError("Kecamatan tidak boleh kosong.")

    def lengkap(self) -> str:
        """Mengembalikan alamat lengkap."""
        return (
            f"Dusun {self.dusun}, Desa {self.desa}, "
            f"Kecamatan {self.kecamatan}"
        )

    def singkat(self) -> str:
        """Mengembalikan alamat tanpa nama dusun."""
        return f"{self.desa}, {self.kecamatan}"
