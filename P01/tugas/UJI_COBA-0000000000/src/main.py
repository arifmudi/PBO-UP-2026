"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar."""

from src.mahasiswa import Mahasiswa


def main() -> None:
    saya = Mahasiswa("Hikmatul Mardhatillah", "2555201013", "Bangkinang")
    print(saya.perkenalan())


if __name__ == "__main__":
    main()