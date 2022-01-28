# Luo ohjelma, joka arpoo kaksi lukua väliltä 1-9. 
# Jos arvotut kaksi lukua ovat samat, niin kone tulostaa tekstin "Aikamoinen sattuma". 
# Jos luvut eivät olesamat, niin kone tulostaa tekstin "Aina ei voi voittaa".
# (Vinkki: Tuo käyttöön random-kirjasto import random -komennolla ja arvo kaksi lukua random.randint(alku,loppu) -komennolla.)

import random

luku1 = random.randint(1, 9)
luku2 = random.randint(1, 9)

if luku1 == luku2:
    print("Aikamoinen sattuma")
else:
    print("Aina ei voi voittaa")