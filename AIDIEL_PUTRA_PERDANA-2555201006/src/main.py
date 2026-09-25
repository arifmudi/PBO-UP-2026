"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar.""" 

from src.mahasiswa import Mahasiswa 

def main() -> None:    
    saya = Mahasiswa("Aidiel Putra Perdana", "2555201006", "Ridan Permai")    
    print(saya.perkenalan()) 
    
if __name__ == "__main__":    
    main()