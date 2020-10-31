import aasikaytto
import aasilogiikka
import aasimaaritelmat

def main():
    aasidata = aasilogiikka.alusta
    
    while True:
        aasikaytto.nayta_tila(aasidata)
        syote = aasikaytto.pyyda_syote(aasidata)
        
        if syote == aasimaaritelmat.LOPETA:
            break
        elif syote == aasimaaritelmat.RUOKI:
            aasilogiikka.ruoki
            #???
        elif syote == aasimaaritelmat.KUTITA:
            #???
            aasilogiikka.kutita
        elif syote == aasimaaritelmat.TYOSKENTELE:
            #???
            aasilogiikka.tyoskentele
        elif syote == aasimaaritelmat.ALUSTA:
            #???
            aasilogiikka.alusta
if __name__ == "__main__":
   # ???