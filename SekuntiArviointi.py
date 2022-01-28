# Luo ohjelma, joka pyytää käyttäjää arvioimaan 15 sekunnin kulumisen mahdollisimman tarkasti.
# (Vinkki: Tuo aikakirjasto käyttöön import time -komennolla. Tapahtuman tarkan ajanhetken saa talteen tekemällä muuttujan, jonka arvo on time.time().)

import time

print("Arvioi 15 sekuntia. Ohjelma alkaa painamalla Enteria ja loppuu samalla tavalla")

aloita = input()
if aloita != "":
    print("Väärä aloitus")
else:
    alku = time.time()

lopeta = input()
if lopeta != "":
    print("Väärä lopetus")
else:
    loppu = time.time()

aika = round((loppu - alku), 2)

print("Aikaa meni: " + str(aika))