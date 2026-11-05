"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar.""" 

from src.mahasiswa import Mahasiswa 

def main() -> None:    
    saya = Mahasiswa("Mukhtar Lutfi", "2555201012", "Bangkinang Kota")    
    print(saya.perkenalan()) 
    
if __name__ == "__main__":    
    main()