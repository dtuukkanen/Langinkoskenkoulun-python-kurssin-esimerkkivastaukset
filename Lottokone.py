# Ohjelmoi lottokone, joka kysyy käyttäjältä seitsemän lukua. 
# Sen jälkeen ohjelma arpoo seitsemän lukua väliltä 1-40 ja vertaa käyttäjän lukua arvottuihin lukuihin sekä ilmoittaa kuinka monta meni oikein.
# (Vinkki: Tee while-silmukka, joka lisää käyttäjän kirjoittamia lukuja listaan. 
# Silmukka päättyy, kun listassa on seitsemän lukua. Sen jälkeen toinen silmukka käy läpi käyttäjän antamat luvut arvotuista luvuista muodostetun listan kanssa.)

import random

samoja = 0
omalista = []
konelista = []

while (len(omalista) < 7):
    omaluku = int(input("Anna luku väliltä 1-40:"))
    if omaluku in omalista:
        print("Väärä luku")
    elif omaluku < 1 or omaluku > 40:
        print("Väärä luku")
    else:
        omalista.append(omaluku)

while (len(konelista) < 7):
    koneluku = random.randint(1, 40)
    if koneluku in konelista:
        continue
    elif koneluku < 1 or koneluku > 40:
        continue
    else:
        konelista.append(koneluku)

for i in omalista:
    if i in konelista:
        samoja += 1
    
print("Samoja on " + str(samoja))
