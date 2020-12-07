import queue
print("start")
q = queue.Queue()
daten = []
ergebnis = 0
q.put("shiny gold")

try:
    datei = open("Daten.txt","r")
    zeilen = datei.read().splitlines()
    datei.close()
    for i in zeilen:
        daten.append(i)
except:
    print("Datei konnte nicht gelesen werden")
    
    
def durchlaufen(bag):
    print(bag)
    global ergebnis
    x=""
    for i in range(len(daten)):
        if bag in daten[i]:
            x = daten[i][:daten[i].index("contain")-6]
            if bag not in x:
                ergebnis+=1
                q.put(x)
                daten[i] = ""


while not q.empty():
    durchlaufen(q.get())
    
print(ergebnis)