from utilities import unos_pozitivnog_cijelog_broja

def unos_korisnika(redni_broj):
    korisnik = {}

    korisnik["Ime"] = input(f"Unesite ime {redni_broj}. korisnika: ").capitalize()
    korisnik["Prezime"] = input(f"Unesite prezime {redni_broj}. korisnika: ").capitalize()
    korisnik["Telefon"] = unos_pozitivnog_cijelog_broja(f"Unesite telefon {redni_broj}. korisnika: ")
    korisnik["Email"] = input(f"Unesite email {redni_broj}. korisnika: ").strip()

    return korisnik
