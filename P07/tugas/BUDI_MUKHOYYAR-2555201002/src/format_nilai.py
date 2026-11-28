
from functools import singledispatch


@singledispatch
def sebagai_teks(nilai: object) -> str:
    """Bentuk umum jika tidak ada format khusus untuk tipe data."""
    return str(nilai)


@sebagai_teks.register(int)
def _bilangan_bulat(nilai: int) -> str:
    """Mengubah bilangan bulat menjadi format rupiah."""
    return "Rp" + f"{nilai:,}".replace(",", ".")


@sebagai_teks.register(float)
def _bilangan_pecahan(nilai: float) -> str:
    """Mengubah bilangan pecahan menjadi format persentase."""
    return f"{nilai * 100:.1f}%"


@sebagai_teks.register(list)
def _daftar(nilai: list[object]) -> str:
    """Mengubah isi daftar menjadi teks."""
    return ", ".join(sebagai_teks(butir) for butir in nilai)
