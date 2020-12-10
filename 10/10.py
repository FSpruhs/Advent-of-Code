daten = []

einer = 1
dreier = 1

datei = open("Daten.txt","r")
daten = datei.read().splitlines()
datei.close()
daten = list(map(int,daten))
daten.sort()

for i in range(len(daten)-1):
    diff = daten[i+1] - daten[i]
    if diff == 1:
        einer +=1
    elif diff == 3:
        dreier +=1
    else:
        print("Fehler bei", daten[i])
    print(daten[i], daten[i+1])

print(einer, dreier)