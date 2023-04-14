from artikl import get_artilk
from kategorija import get_kategorija
from korisnik import get_korisnik
from datetime import date
from utilities import unos_datuma, unos_intervala

def unos_prodaje(korisnici, kategorije, redni_broj):
    prodaja = {}

    prodaja["Datum"] = unos_datuma(f"Unesite datum isteka {redni_broj}. prodaje: ")

#Odabir korisnika
    print(f"Odaberite korisnika {redni_broj}. prodaje: ")
    for i, korisnik in enumerate(korisnici, start=1):
        print(get_korisnik(i, korisnik))

    odabrani_korisnik = unos_intervala(1,i)

#Odabir kategorije
    print(f"Odaberite kategoriju {redni_broj}. prodaje: ")
    for i, kategorija in enumerate(kategorije, start=1):
        print(get_kategorija(i, kategorija))

    odabrana_kategorija = unos_intervala(1,i)

#Odabir artikla
    print(f"Odaberite artikl {redni_broj}. prodaje: ")

    for i, artikl in enumerate(kategorije[odabrana_kategorija - 1]["Artikli"], start=1):
        print(get_artilk(i, artikl))

    odabrani_artikl = unos_intervala(1,i)

    prodaja["Korisnik"] = korisnici[odabrani_korisnik - 1]
    prodaja["Artikl"] = kategorije[odabrana_kategorija - 1]["Artikli"][odabrani_artikl - 1]

    return prodaja