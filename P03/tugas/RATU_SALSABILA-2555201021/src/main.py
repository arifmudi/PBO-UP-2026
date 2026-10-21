"""Program utama demonstrasi PBO P03."""

from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


alamat_ratu = Alamat("Kumantan", "Kumantan", "Bangkinang")
ratu = Penyewa(
    "2555201021000001",
    "Ratu Salsabila",
    alamat_ratu,
    "083132755771",
)

alamat_nayla = Alamat("Uway", "Uway", "Bangkinang")
nayla = Penyewa(
    "1406014403950002",
    "Nayla Wikhsa",
    alamat_nayla,
)

traktor = AlatTani("TR-01", "Traktor Roda Dua Kubota", 150000)

print(ratu.identitas())
print(ratu.kontak())
print(nayla.kontak())
print(traktor.keterangan())
