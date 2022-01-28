# Luo ohjelma, joka kertoo onko annettu luku parillinen vai ei.
# (Vinkki: Jos luku on parillinen, niin jakojäännös kakkosella jaettuna on nolla. Parittomalla luvulla jakojäännös on yksi.)

luku = int(input("Anna luku:"))

if luku % 2 == 0:
    print("Luku on parillinen")
else:
    print("Luku ei ole parillinen")