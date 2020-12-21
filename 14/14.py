daten = []
mask = ""
mem_value = 0
speicher = {}
datei = open("Daten.txt","r")
daten = datei.read().splitlines()
datei.close()

def dez_umrechnen(mem_value):
    mem_bin = ""
    for i in range(36):
        x = mem_value%2
        if x == 1:
            mem_bin += "1"
        else:
            mem_bin += "0"
        mem_value = mem_value // 2
    return mem_bin[::-1]

def bin_umrechnen(bin_zahl):
    zahl = 0
    for i in range(36):
        zahl += int(bin_zahl[i])*(2**(35-i))
    return zahl
                

def speichern(mask,mem_value):
    mem_bin = dez_umrechnen(mem_value)
    mem_value_new = ""
    for i in range(36):
        if mask[i] == "X":
            mem_value_new += mem_bin[i]
        else:
            mem_value_new += mask[i]
    return bin_umrechnen(mem_value_new)

for zeile in daten:
    if zeile[:4] == "mask":
        mask = zeile[7:]
    else:
        mem_key = zeile[:zeile.index("]")+1]
        mem_value = int(zeile[zeile.index("=")+2:])
        mem_value_new = speichern(mask,mem_value)
        
        if mem_key in mask:
            speicher[mem_key] = mem_value_new
        else:
            speicher.update({mem_key:mem_value_new})
            
print(speicher)
print(sum(speicher.values()))
