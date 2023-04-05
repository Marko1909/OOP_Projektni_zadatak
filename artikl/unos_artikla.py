def unos_artikla(redni_broj):
    artikl = {}
    artikl["Naslov"] = input(f"Unesite naslov {redni_broj}. artikla: ")
    artikl["Opis"] = input(f"Unesite opis {redni_broj}. artikla: ")
    artikl["Cijena"] = float(input(f"Unesite cijenu {redni_broj}. artikla: "))

    return artikl
