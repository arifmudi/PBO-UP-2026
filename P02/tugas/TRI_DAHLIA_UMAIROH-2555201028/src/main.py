from .mahasiswa import Mahasiswa


def main() -> None:
    mahasiswa = Mahasiswa("Budi Santoso", "2410123456", "Kuok")
    print(mahasiswa.perkenalan())


if __name__ == "__main__":
    main()