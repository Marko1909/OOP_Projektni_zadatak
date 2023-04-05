def ispis_artikla(artikl):
    print(f'\tNaslov: {artikl["Naslov"]}')
    print(f'\tOpis: {artikl["Opis"]}')
    print(f'\tCijena: {artikl["Cijena"]}')

def get_artilk(redni_broj, artikl):
    return f'\t{redni_broj}. {artikl["Naslov"]}'
