"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar."""

from src.mahasiswa import Mahasiswa


def main() -> None:
    saya = Mahasiswa("Reyhan Pratama", "2555201016", "Batu Langkah Kecil")
    print(saya.perkenalan())


if __name__ == "__main__":
    main()
