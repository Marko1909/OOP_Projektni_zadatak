from artikl import ispis_artikla
from korisnik import ispis_korisnika

def ispis_prodaje(prodaja):
    print('Informacije o korisniku: ')
    ispis_korisnika(prodaja["Korisnik"])

    print('Informacije o artiklu: ')
    ispis_artikla(prodaja["Artikl"])

    print('Datum isteka prodaje: ')
    print(f'\t Dan: {prodaja["Datum"].day}')
    print(f'\t Mjesec: {prodaja["Datum"].month}')
    print(f'\t Godina: {prodaja["Datum"].year}')

    print('-' * 30)