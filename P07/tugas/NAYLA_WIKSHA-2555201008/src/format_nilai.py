
from functools import singledispatch


@singledispatch
def sebagai_teks(nilai: object) -> str:
    """Mengubah nilai menjadi teks."""
    return str(nilai)


@sebagai_teks.register(int)
def _bilangan_bulat(nilai: int) -> str:
    return "Rp" + f"{nilai:,}".replace(",", ".")


@sebagai_teks.register(float)
def _bilangan_pecahan(nilai: float) -> str:
    return f"{nilai * 100:.1f}%"


@sebagai_teks.register(list)
def _daftar(nilai: list[object]) -> str:
    return ", ".join(sebagai_teks(butir) for butir in nilai)
