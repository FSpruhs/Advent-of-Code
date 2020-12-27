daten = []
ergebnis = 0

try:
    datei = open("Daten.txt", "r")
    text = datei.read().splitlines()
    datei.close()
    tmp = ""
    for link in text:
        tmp += link
        if link == "":
            daten.append(tmp)
            tmp = ""
except:
    print("Datei konnte nicht geladen werden")


def zaehl_buchstaben(x):
    count = 0
    print(x)
    count += len(set(x))
    print(count)
    return count


for i in range(len(daten)):
    ergebnis += zaehl_buchstaben(daten[i])


print(ergebnis)
