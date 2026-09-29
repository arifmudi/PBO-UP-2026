"""Titik masuk program. Satu-satunya berkas yang boleh mencetak ke layar.""" 

from src.mahasiswa import Mahasiswa 

def main() -> None:    
    saya = Mahasiswa("Budi Mukhoyyar", "2555201002", "bangkinang")   
    print(saya.perkenalan()) 
    
if __name__ == "__main__":   
     main()