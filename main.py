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
            break
        elif syote == aasimaaritelmat.TYOSKENTELE:
            #???
            break
        elif syote == aasimaaritelmat.ALUSTA:
            #???
            break

if __name__ == "__main__":
   # ???