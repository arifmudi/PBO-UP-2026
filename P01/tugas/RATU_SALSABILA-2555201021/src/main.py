"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar."""

from src.mahasiswa import Mahasiswa


def main() -> None:
    saya = Mahasiswa("Ratu Salsabila", "2555201021", "Kumantan")
    print(saya.perkenalan())


if __name__ == "__main__":
    main()