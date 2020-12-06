daten = []
ergebnis = 0

try:
    datei = open("daten.txt", "r")
    spieler_link = datei.read().splitlines()
    datei.close()
    for link in spieler_link:
        daten.append(link)
except FileNotFoundError:
    print("Datei konnte nicht geladen werden")


def string_splitten(dateien):
    zeile = dateien
    if zeile.index("-") == 1:
        zahl1 = zeile[0]
        
    else:
        zahl1 = zeile[0:2]
    buchstabe = zeile[(zeile.index(":")-1)]
    zahl2 = zeile[zeile.index("-")+1:zeile.index(" ")]
    passwort = zeile[zeile.index(":")+2:]
    return zahl1, zahl2, buchstabe, passwort

def passwort_prüfen(zahl,zahl2,buchstabe,passwort):
    anzahl = passwort.count(buchstabe)
    if anzahl >= int(zahl1) and anzahl <= int(zahl2):
        print(zahl,zahl2,buchstabe,passwort)
        return 1
    return 0
    
    

for i in range(len(daten)):
    zahl1, zahl2, buchstabe, passwort = string_splitten(daten[i])
    ergebnis = ergebnis + passwort_prüfen(zahl1,zahl2,buchstabe, passwort)

print(ergebnis)
    
    
