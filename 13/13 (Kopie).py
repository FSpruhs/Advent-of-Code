daten = []
busse = {}
datei = open("Test.txt","r")
daten = datei.read().splitlines()
datei.close()

bus = daten[1].split(",")

for i in range(len(bus)):
    if bus[i] != "x":
        print(bus[i])
        busse.update({i:int(bus[i])})

print(busse)

    
        





