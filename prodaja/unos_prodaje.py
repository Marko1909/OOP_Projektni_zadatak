from artikl import get_artilk
from kategorija import get_kategorija
from korisnik import get_korisnik
from datetime import date

def unos_prodaje(korisnici, kategorije, redni_broj):
    prodaja = {}

    dan = int(input(f"Unesite dan isteka {redni_broj}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {redni_broj}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {redni_broj}. prodaje: "))

    prodaja["Datum"] = date(godina, mjesec, dan)

#Odabir korisnika
    print(f"Odaberite korisnika {redni_broj}. prodaje: ")
    for i, korisnik in enumerate(korisnici, start=1):
        print(get_korisnik(i, korisnik))

    odabrani_korisnik = int(input("Odabrani korisnik: "))

#Odabir kategorije
    print(f"Odaberite kategoriju {redni_broj}. prodaje: ")
    for i, kategorija in enumerate(kategorije, start=1):
        print(get_kategorija(i, kategorija))

    odabrana_kategorija = int(input("Odabrana kategorija: "))

#Odabir artikla
    print(f"Odaberite artikl {redni_broj}. prodaje: ")

    for i, artikl in enumerate(kategorije[odabrana_kategorija - 1]["Artikli"], start=1):
        print(get_artilk(i, artikl))

    odabrani_artikl = int(input("Odabrani artikl: "))

    prodaja["Korisnik"] = korisnici[odabrani_korisnik - 1]
    prodaja["Artikl"] = kategorije[odabrana_kategorija - 1]["Artikli"][odabrani_artikl - 1]

    return prodaja