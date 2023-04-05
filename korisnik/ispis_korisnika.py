def ispis_korisnika(korisnik):
    print(f'\tIme: {korisnik["Ime"]}')
    print(f'\tPrezime: {korisnik["Prezime"]}')
    print(f'\tTelefon: {korisnik["Telefon"]}')
    print(f'\tEmail: {korisnik["Email"]}')

def get_korisnik(redni_broj, korisnik):
    return f'\t{redni_broj}. {korisnik["Ime"]} {korisnik["Prezime"]}'
