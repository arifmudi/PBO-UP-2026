
"""Demonstrasi name mangling pada Python."""


class Dompet:
    """Dompet sederhana untuk menunjukkan name mangling."""

    def __init__(self, saldo: int) -> None:
        self.__saldo = saldo

    def lihat_saldo(self) -> int:
        """Mengembalikan saldo melalui metode resmi."""
        return self.__saldo
