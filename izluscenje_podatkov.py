import re  # knjiznica za regularne izraze 


def izlusci_sezono(html, leto):
    """Iz HTML vsebine ene sezone izlusci prvaka, MVP-ja in najboljsega strelca."""

    
    prvak = re.search(r"League Champion</strong>:\s*<a[^>]*>([^<]+)</a>", html)

    
    mvp = re.search(
        r"Hart Memorial Trophy</strong>:\s*<a[^>]*>([^<]+)</a>\s*\((\d+) G, (\d+) A, (\d+) P\)",
        html,
    )

   
    strelec = re.search(
        r"Points Leaders</strong>:\s*<a[^>]*>([^<]+)</a>\s*\((\d+)\)", html
    )

   
    podatki = {
        "sezona": leto,
        "prvak": prvak.group(1) if prvak else None,
        "mvp": mvp.group(1) if mvp else None,
        "mvp_goli": mvp.group(2) if mvp else None,
        "mvp_asistence": mvp.group(3) if mvp else None,
        "mvp_tocke": mvp.group(4) if mvp else None,
        "najboljsi_strelec": strelec.group(1) if strelec else None,
        "najboljsi_strelec_tocke": strelec.group(2) if strelec else None,
    }

    return podatki