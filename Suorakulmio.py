# Luo ohjelma, joka kysyy käyttäjältä kaksi lukua: suorakulmion leveyden ja korkeuden. 
# Ohjelma laskee ja ilmoittaa suorakulmion piirin ja pinta-alan.

luku1 = float(input("Suorakulmion leveys:"))
luku2 = float(input("Suorakulmion korkeus:"))
piiri = luku1 * 2 + luku2 * 2
pinta_ala = luku1 * luku2
print("Piiri on: " + str(piiri))
print("Pinta-ala on: " + str(pinta_ala))
