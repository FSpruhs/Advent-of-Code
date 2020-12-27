zahlen = []

try:
    datei = open("daten.txt", "r")
    spieler_link = datei.read().splitlines()
    datei.close()
    for link in spieler_link:
        zahlen.append(link)
except FileNotFoundError:
    print("Datei konnte nicht geladen werden")


for zahl in zahlen:
    if int(zahl) < 1000:
        zahl1 = zahl
        for i in zahlen:
            ergebnis = int(zahl1) + int(i)
            if ergebnis == 2020:
                print(ergebnis)
                print(zahl1)
                print(i)
