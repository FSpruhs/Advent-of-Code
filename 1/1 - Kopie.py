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
            if int(i) < 1000 and i != zahl1:
                zahl2 = i
                for j in zahlen:
                    if int(j) != zahl1 and j != zahl2:
                        zahl3 = j
                        ergebnis = int(zahl1) + int(zahl2)+ int(zahl3)
                        print(ergebnis, zahl1, zahl2, zahl3)
                        if ergebnis == 2020:
                            print(ergebnis, zahl1, zahl2, zahl3)

print("fertig")
                    
            
            

        
    
