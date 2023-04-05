from artikl import unos_artikla
def unos_kategorije(redni_broj):
    kategorija = {}
    kategorija["Naziv"] = input(f"Unesite naziv {redni_broj}. kategorije: ")

    broj_artikala = int(input(f"Unesite broj artikala za {redni_broj}. kategoriju: "))

    artikli = []
    for i in range(1, broj_artikala + 1):
        artikli.append(unos_artikla(i))

    kategorija["Artikli"] = artikli

    return kategorija