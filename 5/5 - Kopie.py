daten = []
ergebnis = 0
liste = []

try:
    datei = open("Daten.txt", "r")
    spieler_link = datei.read().splitlines()
    datei.close()
    for link in spieler_link:
        daten.append(link)
except FileNotFoundError:
    print("Datei konnte nicht geladen werden")



def check_reihe(reihe):
    x = 0
    y = 127
    for i in range(7):
        if reihe[i] == "F":
            z = y+1 - x
            y = y - z//2
        if reihe[i] == "B":
            z = y+1 - x
            x = x + z//2
    return x

def check_sitz(sitz):
    x = 0
    y = 7
    for i in range(3):
        if sitz[i] == "L":
            z = y+1 - x
            y = y - z//2
        if sitz[i] == "R":
            z = y+1 - x
            x = x + z//2
    return x

def sitz_id(reihe, sitz):
    return reihe * 8 + sitz
    
        

for i in daten:
    reihe = check_reihe(i[:-3])
    sitz = check_sitz(i[-3:])
    id_nummer = sitz_id(reihe, sitz)
    liste.append(id_nummer)
    if id_nummer > ergebnis:
        ergebnis = id_nummer
        print(reihe, sitz, id_nummer)
liste.sort()
x = 61
for i in range(len(liste)):
    if x not in liste:
        print(x)
    x+=1






    
