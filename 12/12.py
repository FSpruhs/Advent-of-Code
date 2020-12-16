position = [0,0]
north_south = 0
west_east = 0
direction = 90
daten = []

datei = open("Daten.txt","r")
daten = datei.read().splitlines()
datei.close()

def forward(zahl):
    global direction
    zahl = zahl
    richtung = ""
    if direction == 0:
        richtung = "N"
    if direction == 90:
        richtung = "E"
    if direction == 180:
        richtung = "S"
    if direction == 270:
        richtung = "W"
    flug(richtung, zahl)

def ausrichten(befehl, zahl):
    global direction
    if befehl == "L":
        direction = (direction - zahl)%360
    else:
        direction = (direction + zahl)%360

def flug(befehl, zahl):
    global position, direction, north_south,west_east
    if befehl == "N":
        north_south += zahl
    elif befehl == "S":
        north_south -= zahl
    elif befehl == "W":
        west_east -= zahl
    elif befehl == "E":
        west_east += zahl
    elif befehl == "F":
        forward(zahl)
    

for i in daten:
    befehl =i[0]
    zahl = int(i[1:])
    if befehl == "L" or befehl == "R":
        ausrichten(befehl, zahl)
    else:
        flug(befehl, zahl)
    print(north_south, west_east)
    
ergebnis = abs(north_south) + abs(west_east)
print(ergebnis)