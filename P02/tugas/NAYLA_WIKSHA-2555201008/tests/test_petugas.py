from src.model.petugas import Petugas


def test_petugas_awalnya_tidak_bertugas() -> None:
    petugas = Petugas("Budi", "Pengurus UPJA")

    assert "Tidak bertugas" in petugas.ringkasan_tugas()


def test_mulai_bertugas() -> None:
    petugas = Petugas("Budi", "Pengurus UPJA")

    hasil = petugas.mulai_bertugas()

    assert hasil == "Budi mulai bertugas melayani penyewaan"
    assert "Sedang bertugas" in petugas.ringkasan_tugas()


def test_petugas_melayani_penyewaan() -> None:
    petugas = Petugas("Budi", "Pengurus UPJA")
    petugas.mulai_bertugas()

    hasil = petugas.layani_penyewaan()

    assert hasil == "Budi telah melayani penyewaan"
    assert "Penyewaan dilayani: 1" in petugas.ringkasan_tugas()


def test_petugas_belum_bertugas_tidak_melayani() -> None:
    petugas = Petugas("Siti", "Administrasi")

    hasil = petugas.layani_penyewaan()

    assert hasil == "Siti belum mulai bertugas"
    assert "Penyewaan dilayani: 0" in petugas.ringkasan_tugas()


def test_petugas_melayani_beberapa_penyewaan() -> None:
    petugas = Petugas("Budi", "Pengurus UPJA")
    petugas.mulai_bertugas()

    petugas.layani_penyewaan()
    petugas.layani_penyewaan()
    petugas.layani_penyewaan()

    assert "Penyewaan dilayani: 3" in petugas.ringkasan_tugas()


def test_selesai_bertugas() -> None:
    petugas = Petugas("Budi", "Pengurus UPJA")
    petugas.mulai_bertugas()

    hasil = petugas.selesai_bertugas()

    assert hasil == "Budi selesai bertugas"
    assert "Tidak bertugas" in petugas.ringkasan_tugas()


def test_dua_petugas_memiliki_data_terpisah() -> None:
    petugas_a = Petugas("Budi", "Pengurus UPJA")
    petugas_b = Petugas("Siti", "Administrasi")

    petugas_a.mulai_bertugas()
    petugas_a.layani_penyewaan()

    assert "Penyewaan dilayani: 1" in petugas_a.ringkasan_tugas()
    assert "Penyewaan dilayani: 0" in petugas_b.ringkasan_tugas()
