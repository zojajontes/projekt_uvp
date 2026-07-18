from dobivanje_spletnih_strani import prenesi_sezone  #uvozimo sem to funkijo iz durge datoteke
prenesi_sezone(2000, 2024)#nalozimo sezone od 2000 do 2024


from izluscenje_podatkov import izlusci_sezono

with open("strani_sezon/NHL_2023.html", "r", encoding="utf-8") as f:
    html = f.read()

podatki = izlusci_sezono(html, 2023)
print(podatki)