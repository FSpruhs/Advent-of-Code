daten = []

datei = open("Daten.txt","r")
daten = datei.read().splitlines()
datei.close()
daten = list(map(int,daten))
daten.sort()
daten.append(daten[len(daten)-1]+3)

besucht = {}

def rek(num):
    if num in besucht:
        return besucht[num]
    if num == daten[len(daten)-1]:
        return 1
    else:
        x = 0
        if num+1 in daten:
            x += rek(num+1)
        if num+2 in daten:
            x += rek(num+2)
        if num+3 in daten:
            x += rek(num+3)
            
        besucht[num] = x
        return besucht[num]        


ergebnis = rek(0)
print(ergebnis)
print(besucht)

