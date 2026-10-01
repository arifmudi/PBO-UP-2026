"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar.""" 

from src.mahasiswa import Mahasiswa 

def main() -> None:    
    saya = Mahasiswa("MHD. Khairul Fadli", "2555201029", "Salo")    
    print(saya.perkenalan()) 
    
if __name__ == "__main__":    
    main()