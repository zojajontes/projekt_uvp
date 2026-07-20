import os         # za mape (da lahko ustvarimo mapo za shranjevanje)
import requests   # za prenos spletnih strani


def prenesi_sezone(zacetno_leto, koncno_leto):
    """Prenese HTML strani NHL sezon in jih shrani v mapo strani_sezon."""

    # nardi mapo da shranmo not HTML datoteke
    if not os.path.exists("strani_sezon"):  # ce mapa ne obstaja
        os.makedirs("strani_sezon") #nardi mapo

    #gremo cez vsa leta od prvega do vkljucno zadnega
    for leto in range(zacetno_leto, koncno_leto + 1):

        # sestavimo pravi URL za to sezono, npr. za leto=2000:
        # https://www.hockey-reference.com/leagues/NHL_2000.html
        url = f"https://www.hockey-reference.com/leagues/NHL_{leto}.html"

        # poslemo zahtevo na internet in dobimo nazaj HTML vsebino strani
        stran = requests.get(url) #gre na net in najde to stran
        stran.encoding = "utf-8"
        # shranimo HTML v datoteko, npr. strani_sezon/NHL_2000.html
        with open(f"strani_sezon/NHL_{leto}.html", "w", encoding="utf-8") as f: #with je zato da se tut sama zapre da ne rabmo mi
            f.write(stran.text) #v mapi kjer shranjuje sezone naredi datoteko s tem imenom in pol besedilo iz splene strani napise not

        # izpisemo v terminal, da vidimo napredek
        print(f"Sezona {leto} shranjena.")