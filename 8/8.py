daten = []
figur = 0
acc_zahl=0

datei = open("Daten.txt","r")
r=datei.read().splitlines()
datei.close()
for satz in r:
    daten.append(satz)


def nop():
    global figur
    figur += 1

def acc(vorzeichen, zahl):
    global acc_zahl, figur
    if vorzeichen == "+":
        acc_zahl += int(zahl)
    else:
        acc_zahl -= int(zahl)
    figur += 1

def jmp(vorzeichen, zahl):
    global figur
    if vorzeichen == "+":
        figur += int(zahl)
    else:
        figur -= int(zahl)

def var_erstellen(l):
    befehl = l[0:3]
    vorzeichen = l[4:5]
    zahl = l[5:]
    return befehl, vorzeichen, zahl

while figur != "END":
    print(daten[figur])
    befehl, vorzeichen, zahl = var_erstellen(daten[figur])
    daten[figur] = "END"
    if befehl == "nop":
        nop()
    elif befehl == "acc":
        acc(vorzeichen, zahl)
    elif befehl == "jmp":
        jmp(vorzeichen, zahl)
    else:
        print("Fehler")
        break
print(daten)
print(acc_zahl)

    
    
        
    