daten = []
passport = ""
ergebnis = 0


try:
    datei = open("Daten.txt", "r")
    spieler_link = datei.read().splitlines()
    datei.close()
    for link in spieler_link:
        daten.append(link)
except FileNotFoundError:
    print("Datei konnte nicht geladen werden")

def split(passport):
    liste = passport.split()
    d = {}
    for value in liste:
        x = value.split(":")
        d[x[0]]=x[1]
    return d["byr"], d["iyr"], d["eyr"], d["hgt"], d["hcl"], d["ecl"], d["pid"]

def byr_test(byr):
    try:
        int(byr)
    except:
        return 0
    if 1920 <= int(byr) <= 2002:
        return 1
    return 0

def iyr_test(iyr):
    try:
        int(iyr)
    except:
        return 0
    if 2010 <= int(iyr) <= 2020:
        return 1
    return 0

def eyr_test(eyr):
    try:
        int(eyr)
    except:
        return 0
    if 2020 <= int(eyr) <= 2030:
        return 1
    return 0

def hgt_test(hgt):
    if hgt[-2:] == "cm":
        if  150 <= int(hgt[:-2]) <= 193:
            return 1
    if hgt[-2:] == "in":
        if  59 <= int(hgt[:-2]) <= 76:
            return 1    
    return 0

def hcl_test(hcl):
    liste=["0","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f",]
    if hcl[0] != "#" or len(hcl) != 7:
        return 0
    for i in range(1,7):
        if hcl[i] not in liste:
            return 0
    return 1

def ecl_test(ecl):
    liste = ["amb","blu","brn","gry","grn","hzl","oth"]
    if ecl in liste:
        return 1
    return 0

def pid_test(pid):
    try:
        int(pid)
    except:
        return 0
    if len(pid) == 9:
        return 1
    return 0



def check(passport):
    global ergebnis
    number = passport.count("byr:")+passport.count("iyr:")+passport.count("eyr:")+passport.count("hgt:")+passport.count("hcl:")+passport.count("ecl:")+passport.count("pid:")
    if number == 7:  
        byr, iyr, eyr, hgt, hcl, ecl, pid = split(passport)
        print(byr, iyr, eyr, hgt, hcl, ecl, pid)
        number2 = byr_test(byr) + iyr_test(iyr) + eyr_test(eyr) + hgt_test(hgt) + hcl_test(hcl) + ecl_test(ecl) + pid_test(pid)
        if number2 == 7:
            ergebnis += 1
    


for i in range(len(daten)):
    passport+=daten[i] + " "
    if daten[i] == "":
        check(passport)
        passport=""

print(ergebnis)
