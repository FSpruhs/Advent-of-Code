daten = []
ergebnis = {}
datei = open("Daten.txt","r")
daten = datei.read().splitlines()
datei.close()

bus = daten[1].split(",")
bus_neu = []

for i in bus:
    if i != "x":
        bus_neu.append(i)

bus_neu = map(int,bus_neu)

for i in bus_neu:
    start = 0
    while start < int(daten[0]):
        start += i
    ergebnis.update({start:i})

print((min(ergebnis)-int(daten[0]))*ergebnis[min(ergebnis)])