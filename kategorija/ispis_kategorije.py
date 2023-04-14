from artikl import ispis_artikla

def get_kategorija(redni_broj, kategorija):
    return f'\t{redni_broj}. {kategorija["Naziv"]}'


def ispis_kategorije(kategorija):
    print(f'{kategorija["Naziv"]}')

def ispis_svih_kategorija(kategorije):
    for i, kategorija in enumerate(kategorije, start=1):
        ispis_kategorije(kategorija)

        for j, artikl in enumerate(kategorije[i-1]["Artikli"], start=1):
            print("Informacije o artiklu: ")
            ispis_artikla(artikl)

        print("\n")
