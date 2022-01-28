#Luo ohjelma, joka kysyy käyttäjältä sanoja ja lisää ne listaan. Kun käyttäjä lisää sanan "loppu", niin ohjelma järjestää listan aakkosjärjestykseen ja tulostaa sen.
#(Vinkki: Tee aluksi tyhjä lista. Tee sen jälkeen while-silmukka, joka kestää kunnes käyttäjä sanoo "loppu". While-silmukassa ohjelma kysyy käyttäjältä sanoja ja lisää ne tyhjään listaan.)

lista = []

print('Anna sana, "loppu" lopettaa:')

while(True):
    sana = input()
    if sana == "loppu":
        break
    else:
        lista.append(sana)

lista.sort()
print(lista)
