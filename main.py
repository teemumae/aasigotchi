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
            aasikaytto.nayta_tila(aasidata)
            #???
        elif syote == aasimaaritelmat.KUTITA:
            #???
            aasilogiikka.kutita
            aasikaytto.nayta_tila(aasidata)
        elif syote == aasimaaritelmat.TYOSKENTELE:
            #???
            aasilogiikka.tyoskentele
            aasikaytto.nayta_tila(aasidata)
        elif syote == aasimaaritelmat.ALUSTA:
            #???
            aasilogiikka.alusta
if __name__ == "__main__":
    main()