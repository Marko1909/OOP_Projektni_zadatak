from artikl import ispis_artikla

def get_kategorija(redni_broj, kategorija):
    return f'\t{redni_broj}. {kategorija["Naziv"]}'


def ispis_kategorije(kategorija):
    print(f'{kategorija["Naziv"]}')


def ispis_svih_kategorija(kategorije):
    for kategorija in kategorije:
        ispis_kategorije(kategorija)

        for j, artikl in enumerate(kategorija["Artikli"], start=1):
            print(f"Informacije o {j}. artiklu: ")
            ispis_artikla(artikl)

        print("\n")
