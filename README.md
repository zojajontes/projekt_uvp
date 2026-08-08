# Analiza NHL sezon (2000-2024)

V svoji projektni nalogi za predmet Uvod v programiranje sem se odločila analizirati 
NHL sezon med letoma 2000 in 2024 - kdo je bil prvak (Stanley Cup), kdo MVP lige 
(Hart Memorial Trophy) in kdo najboljsi strelec vsake sezone. Podatke sem dobila s 
spletne strani https://www.hockey-reference.com/leagues/.

## NAVODILA

Za pridobitev podatkov iz interneta in njihovo pretvorbo v csv datoteko poženite 
`main.py`.

Analiza NHL sezon je dostopna v datoteki `analiza.ipynb`.

## PRIDOBIVANJE PODATKOV

* V datoteki `dobivanje_spletnih_strani.py` je funkcija, ki za vsako sezono med 
  letoma 2000 in 2024 shrani html datoteko strani te sezone.
* Funkcija v datoteki `izluscenje_podatkov.py` nato z regularnimi izrazi iz vsake 
  html datoteke naredi slovar s podatki o prvaku, MVP-ju lige (skupaj z njegovo 
  statistiko - ločeno za igralce in vratarje) ter najboljsem strelcu sezone.
* Nazadnje funkcija v datoteki `naredi_csv.py` seznam slovarjev sezon prepiše v 
  datoteko `nhl_sezone.csv`.
* Vse funkcije poženemo v `main.py`.

## ANALIZA

V analizi, vidni v datoteki `analiza.ipynb`, lahko vidite razne grafe in tabele, 
ki prikazujejo trend tock najboljsega strelca skozi cas, razmerje med MVP-ji, ki 
so bili igralci ali vratarji, povezavo med MVP-jem in najboljsim strelcem lige, 
ter katere ekipe in igralci so bili v tem obdobju najuspesnejsi.