from src.model.pegawai import Pegawai


class PenyusunLaporan:
    """Menyusun rekap penghasilan dari berbagai jenis pegawai."""

    def __init__(self, pegawai: list[Pegawai]) -> None:
        if not pegawai:
            raise ValueError(
                "laporan tidak dapat disusun dari daftar pegawai kosong"
            )

        self._pegawai = list(pegawai)

    @property
    def jumlah_pegawai(self) -> int:
        return len(self._pegawai)

    def rekap_penghasilan(self) -> list[tuple[str, int]]:
        return [
            (pegawai.nama, pegawai.hitung_penghasilan())
            for pegawai in self._pegawai
        ]

    def tertinggi(self) -> Pegawai:
        return max(
            self._pegawai,
            key=lambda pegawai: pegawai.hitung_penghasilan(),
        )

    def terendah(self) -> Pegawai:
        return min(
            self._pegawai,
            key=lambda pegawai: pegawai.hitung_penghasilan(),
        )

    def total_penghasilan(self) -> int:
        return sum(
            pegawai.hitung_penghasilan()
            for pegawai in self._pegawai
        )
