#DATEN = [0,3,6]
DATEN = [15,12,0,14,3,1]



for i in range(6,30000000):
    aktuell = 0
    last = DATEN[i-1]
    if DATEN.count(last) > 1:
        x=0
        y=0
        for j, k in reversed(list(enumerate(DATEN))):
            if k == last and x == 0:
                x=j
            if k == last and x != j:
                y=j
                break
        aktuell = x-y
    DATEN.append(aktuell)
    print(aktuell)

    
    
    