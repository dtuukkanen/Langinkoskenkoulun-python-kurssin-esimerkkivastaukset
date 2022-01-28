# a)
# Luo ohjelma, joka kysyy käyttäjältä kuvion leveyden ja korkeuden. 
# Ohjelma tulostaa leveyden ja korkeuden perusteella risuaitakuvion. 
# Esimerkiksi, jos leveys on neljä ja korkeus on kolme, niin kuvio on
#####
#####
#####

# b)
# Korjaa a)-kohdan ohjelmaa siten, että risuaidat ovat vain kuvion reunoilla ja niiden keskellä on tyhjää tilaa.



# Tästä alkaa a)-kohta. Kommentoimalla voit ottaa tämän kohdan pois käytöstä
def risuaita(n, m):
     
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print("#", end="")
        print()

leveys = int(input("Anna leveys kuviolle:"))
korkeus = int(input("Anna korkeus kuviolle:"))

risuaita(korkeus, leveys)

# Tästä alkaa b)-kohta. Kommentoimalla voit ottaa tämän kohdan pois käytöstä
def onttorisuaita(n, m):
     
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 or i == n or
                j == 1 or j == m):
                print("#", end="")           
            else:
                print(" ", end="")           
         
        print()

leveys = int(input("Anna leveys kuviolle:"))
korkeus = int(input("Anna korkeus kuviolle:"))

onttorisuaita(korkeus, leveys)
