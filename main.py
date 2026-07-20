from dobivanje_spletnih_strani import prenesi_sezone
from izluscenje_podatkov import izlusci_vse_sezone
from naredi_csv import shrani_v_csv

prenesi_sezone(2000, 2024)
vse_sezone = izlusci_vse_sezone(2000, 2024)
shrani_v_csv(vse_sezone)