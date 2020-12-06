daten = []
ergebnis = 0

def zaehlen(x):
    new_set =[]
    for i in range(len(x)) :
        if i:
            new_set=new_set.intersection(set(x[i]))
        else:
            new_set = set(x[i])
    print(new_set)
    print(len(new_set))
    return len(new_set)


datei = open("Daten.txt","r")
text = datei.read().splitlines()
datei.close()
for i in range(len(text)):
    daten.append(text[i])
    if text[i] == "":
        ergebnis += zaehlen(daten[0:-1])
        daten=[]
    

    


print(ergebnis)
