import csv  # vgrajena knjiznica za delo s CSV datotekami


def shrani_v_csv(vse_sezone, ime_datoteke="nhl_sezone.csv"):
    """Shrani seznam slovarjev (sezon) v CSV datoteko."""

    # imena stolpcev vzamemo iz kljucev prvega slovarja v seznamu
    stolpci = vse_sezone[0].keys()

    with open(ime_datoteke, "w", newline="", encoding="utf-8") as f:
        pisalec = csv.DictWriter(f, fieldnames=stolpci) #orodje ki pise slovarje direktno v csv vrstice, 
        #fieldsman je katera imena stolpcev naj uporabi v katerem vrstnem redu
        pisalec.writeheader()  # zapise vrstico z imeni stolpcev, glavo tabele
        pisalec.writerows(vse_sezone)  # zapise vse sezone, vrstico za vrstico, samo vrednosti brez kljucev

    print(f"Podatki shranjeni v {ime_datoteke}")