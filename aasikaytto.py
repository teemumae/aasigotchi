import aasilogiikka
import aasimaaritelmat

def pyyda_syote(tila):
    """
    Näyttää käyttäjälle aasin tilaa vastaavat mahdolliset syötteet ja kysyy uutta
    syötettä kunnes käyttäjä antaa laillisen syötteen. Saatu syöte palautetaan.
    """
    print("Valinnat: q, r, k, t")
    syote = input("Anna seuraava valinta: ")
    return syote
def nayta_tila(tila):
    """
    Tulostaa aasin tilan.
    """
    print("Aasi on {} vuotta vanha ja rahaa on {} mk.".format(tila['IKÄ'], tila['RAHA']))
    print("Kylläisyys: {}".format(tila['KYLLÄISYYS']))
    print("Onnellisuus:{}".format(tila['ONNELLISUUS']))
    print("Jaksaminen:{}".format(tila['JAKSAMINEN']))