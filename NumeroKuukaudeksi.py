# Luo ohjelma, joka kysyy käyttäjältä lukua 1-12 ja kertoo numeron perusteella, mitä kuukautta numero vastaa.
# (Vinkki: Voit tehdä joko listan, joka sisältää kaikki kuukaudet ja viitata niihin komennolla lista[järjestysluku] tai tehdä if-ehdon jokaista kuukautta varten.)
kuukaudet = ['Tammikuu', 'Helmikuu', 'Maaliskuu', 'Huhtikuu', 'Toukokuu', 'Kesäkuu', 'Heinäkuu', 'Elokuu', 'Syyskuu', 'Lokakuu', 'Marraskuu', 'Joulukuu']

luku = int(input("Anna numero 1-12 väliltä:"))

if luku < 1 or luku > 12:
    print("Väärä luku")
else:
    luku -= 1
    print(kuukaudet[luku])

