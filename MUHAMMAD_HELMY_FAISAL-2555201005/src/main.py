"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar.""" 

from src.mahasiswa import Mahasiswa 

def main() -> None:    
    saya = Mahasiswa("Muhammad Helmy Faisal", "2555201005", "Kumantan")    
    print(saya.perkenalan()) 
    
if __name__ == "__main__":    
    main()