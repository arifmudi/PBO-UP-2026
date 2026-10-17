""" Model domain: petugas UPJA yang bertugas melayani penyewaan """

class Petugas:
    """ Identitas petugas UPJA beserta gaji operasionalnya """

    def __init__(self, nama_petugas: str, no_telepon: str, jabatan: str = "Admin", gaji_harian: int = 50000) -> None:
        self._nama_petugas = nama_petugas
        self._no_telepon = no_telepon
        self._jabatan = jabatan
        self._gaji_harian = gaji_harian

    def gaji_petugas(self, jumlah_hari: int) -> int:
        return self._gaji_harian * jumlah_hari

    def tampilkan_identitas(self) -> str:
        format_gaji = "Rp{:,}".format(self._gaji_harian).replace(",", ".")            
        return f"{self._nama_petugas} ({self._jabatan}) nomor telepon: {self._no_telepon}, gaji harian: {format_gaji}"

    def hubungi_petugas(self) -> str:
        return f"{self._nama_petugas} - {self._no_telepon}"