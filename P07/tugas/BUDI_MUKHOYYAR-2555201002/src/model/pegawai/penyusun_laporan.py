from collections.abc import Sequence

from src.model.pegawai.pegawai import Pegawai


class PenyusunLaporan:
    """Menyusun laporan penghasilan seluruh pegawai."""

    def __init__(self, daftar_pegawai: Sequence[Pegawai]) -> None:
        self._daftar_pegawai = daftar_pegawai

    def rekap_penghasilan(self) -> list[tuple[str, int]]:
        """Menghasilkan daftar nama dan penghasilan setiap pegawai."""
        return [
            (pegawai.nama, pegawai.hitung_penghasilan())
            for pegawai in self._daftar_pegawai
        ]

    def pegawai_tertinggi(self) -> tuple[str, int] | None:
        """Mengambil pegawai dengan penghasilan tertinggi."""
        if not self._daftar_pegawai:
            return None

        return max(
            (
                (pegawai.nama, pegawai.hitung_penghasilan())
                for pegawai in self._daftar_pegawai
            ),
            key=lambda data: data[1],
        )

    def pegawai_terendah(self) -> tuple[str, int] | None:
        """Mengambil pegawai dengan penghasilan terendah."""
        if not self._daftar_pegawai:
            return None

        return min(
            (
                (pegawai.nama, pegawai.hitung_penghasilan())
                for pegawai in self._daftar_pegawai
            ),
            key=lambda data: data[1],
        )

    def total_penghasilan(self) -> int:
        """Menghitung total penghasilan seluruh pegawai."""
        return sum(
            pegawai.hitung_penghasilan()
            for pegawai in self._daftar_pegawai
        )