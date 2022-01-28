# Pythagoran lauseella voidaan ratkaista suorakulmaisen kolmion pisimmän sivun c pituus, kun kolmion korkeus a ja leveys b tiedetään. 
# Pisimmän sivun c pituus on tällöin c = √(a^2 + b^2).

# Luo ohjelma, joka kysyy käyttäjältä suorakulmaisen kolmion korkeuden ja leveyden ja ratkaisee kolmion pisimmän sivun pituuden yhden desimaalin tarkkuudella.
# (Vinkki: Neliöjuuri toimii komennolla math.sqrt(luku), kun olet ottanut math-kirjaston käyttöösi komennolla math import.)

# a^2 + b^2 = c^2
# c = √(a^2 + b^2)

import math

a = float(input("Anna kolmion korkeus:"))
b = float(input("Anna kolmion leveys:"))
c = math.sqrt(a**2 + b**2)
d = round(c, 1)

print(d)