import re  # knjiznica za regularne izraze 



def izlusci_sezono(html, leto):
    """Iz HTML vsebine ene sezone izlusci prvaka, MVP-ja in najboljsega strelca."""

    prvak = re.search(r"League Champion</strong>:\s*<a[^>]*>([^<]+)</a>", html)

    mvp = re.search(
        r"Hart Memorial Trophy</strong>:\s*<a[^>]*>([^<]+)</a>\s*\(([^)]+)\)", html
    )

    strelec = re.search(
        r"Points Leaders</strong>:\s*<a[^>]*>([^<]+)</a>\s*\((\d+)\)", html
    )

    # privzete vrednosti - ce mvp ni najden, ostanejo None
    mvp_ime = mvp.group(1) if mvp else None
    mvp_goli = None
    mvp_asistence = None
    mvp_tocke = None
    mvp_zmage = None
    mvp_porazi = None
    mvp_otl = None
    mvp_gaa = None

    if mvp:
        # poskusimo obliko za igralce: "X G, Y A, Z P"
        igralec_stat = re.search(r"(\d+) G, (\d+) A, (\d+) P", mvp.group(2))

        # poskusimo obliko za vratarje: "X-Y-Z, W.WW GAA"
        vratar_stat = re.search(
            r"(\d+)-(\d+)-(\d+), ([\d.]+) GAA", mvp.group(2)
        )

        if igralec_stat:
            mvp_goli = int(igralec_stat.group(1))
            mvp_asistence = int(igralec_stat.group(2))
            mvp_tocke = int(igralec_stat.group(3))
        elif vratar_stat:
            mvp_zmage = int(vratar_stat.group(1))
            mvp_porazi = int(vratar_stat.group(2))
            mvp_otl = int(vratar_stat.group(3))
            mvp_gaa = float(vratar_stat.group(4))

    podatki = {
        "sezona": leto,
        "prvak": prvak.group(1) if prvak else None,
        "mvp": mvp_ime,
        "mvp_goli": mvp_goli,
        "mvp_asistence": mvp_asistence,
        "mvp_tocke": mvp_tocke,
        "mvp_zmage": mvp_zmage,
        "mvp_porazi": mvp_porazi,
        "mvp_otl": mvp_otl,
        "mvp_gaa": mvp_gaa,
        "najboljsi_strelec": strelec.group(1) if strelec else None,
        "najboljsi_strelec_tocke": int(strelec.group(2)) if strelec else None,
    }

    return podatki

def izlusci_vse_sezone(zacetno_leto, koncno_leto):
    """Izlusci podatke za vse sezone med zacetno_leto in koncno_leto (vkljucno)."""
    vse_sezone = []  #nov seznam za slovarje sezon

    for leto in range(zacetno_leto, koncno_leto + 1):
        with open(f"strani_sezon/NHL_{leto}.html", "r", encoding="utf-8") as f:
            html = f.read()

        podatki = izlusci_sezono(html, leto)

        vse_sezone.append(podatki) #dodamo slovar za to sezono v skupn seznam

    return vse_sezone