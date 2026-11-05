
from dataclasses import dataclass
from typing import Final

PANJANG_NOMOR_PEGAWAI: Final[int] = 18


@dataclass(frozen=True)
class NomorPegawai:
    """Menyimpan nomor pegawai yang tidak dapat diubah."""

    nilai: str

    def __post_init__(self) -> None:
        if not isinstance(self.nilai, str) or not self.nilai.isdigit():
            raise ValueError("Nomor pegawai harus berupa angka.")
        if len(self.nilai) != PANJANG_NOMOR_PEGAWAI:
            raise ValueError(
                "Nomor pegawai harus terdiri dari "
                f"{PANJANG_NOMOR_PEGAWAI} digit."
            )
