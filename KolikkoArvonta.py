# Luo ohjelma, joka kysyy käyttäjältä, kuinka monta kertaa kolikkoa heitetään. 
# Joka heitolla ohjelma arpoo kruunan tai klaavan. 
# Lopuksi ohjelma kertoo kruunien ja klaavojen lukumäärät ( ja prosenttiosuudet).

import random

monta = int(input("Kuinka monta kertaa kolikkoa heitetään:"))
kruuna = 0
klaava = 0

for i in range(monta):
    kolikko = random.randint(0, 1)
    if kolikko == 0:
        kruuna += 1
    else:
        klaava += 1

krProsentti = round((kruuna / monta) * 100, 2)
klProsentti = round((klaava / monta) * 100, 2)

print("Kruunien määrä: " + str(kruuna))
print("Klaavojen määrä: " + str(klaava))
print("Kruunan prosenttiosuus: " + str(krProsentti) + "%")
print("Klaavan prosenttiosuus: " + str(klProsentti) + "%")