result = []
datei = open("Daten.txt","r")
result = datei.read().splitlines()
datei.close()
daten = list(map(int,result))

def liste_verkleinern(l):
    ind = 25
    l.sort()
    mindest = y - l[0] + 1
    for i in l:
        if int(i) >= mindest:
            ind = l.index(i)
            break
    return l[:ind]

def check_sum(l,y):
    l_new = liste_verkleinern(l)
    for i in range(len(l_new)):
        for j in range(len(l_new)):
            if l_new[i] + l_new[j] == y:
                return l_new[i] , l_new[j]
    print("Kein Ergebnis für: ", y)
    
for i in range(len(daten)-25):
    l = daten[i:i+25]
    y = daten[i+25]
    a, b = check_sum(l,y)
    print(a, "+", b, "=", y)
