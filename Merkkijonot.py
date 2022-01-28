# a) Luo ohjelma, joka tulostaa kaikki merkkijonot, joissa esiintyvät kirjaimet A, B, C ja D. Esimerkiksi AAAA, AAAB, AABB jne.
# (Vinkki: luo lista ["A", "B", "C", "D"] ja käytä for-komentoa neljä kertaa. Katso kappale "Toistorakenne".)

# b)* Korjaa a)-kohdan ohjelmaa siten, että sama kirjain ei saa esiintyä merkkijonossa kahta kertaa. Esimerkiksi ABCD, ABDC, ACBD jne.
# (Vinkki: Käytä if-lauseita for-komentojen jälkeen, jotta sama kirjain ei esiinny useampaa kertaa tulosteessa.)

merkit = ['A', 'B', 'C', 'D']

# Tästä alkaa a)-kohta. Kommentoimalla voit ottaa kohdan pois käytöstä.
print("a)-kohta")
for i in merkit:
    for j in merkit:
        for k in merkit:
            for l in merkit:
                print(i,j,k,l)

# Tästä alkaa b)-kohta. Kommentoimalla voit ottaa kohdan pois käytöstä.
print("b)-kohta")
for i in merkit:
    for j in merkit:
        if j == i:
            continue
        for k in merkit:
            if k == j or k == i:
                continue
            for l in merkit:
                if l == k or l == j or l == i:
                    continue
                print(i,j,k,l)