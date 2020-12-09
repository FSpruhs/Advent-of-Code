result = []
result_part_1 = 1038347917
datei = open("Daten.txt","r")
result = datei.read().splitlines()
datei.close()
daten = list(map(int,result))

low = 0
high = 0

while high <= len(daten) - 1:
    summe = sum(daten[low:high+1])
    if summe < result_part_1:
        high +=1
    if summe > result_part_1:
        low+=1
    if summe == result_part_1:
        print(min(daten[low:high+1])+max(daten[low:high+1]))
