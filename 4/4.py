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

def check(passport):
    global ergebnis
    number = passport.count("byr:")+passport.count("iyr:")+passport.count("eyr:")+passport.count("hgt:")+passport.count("hcl:")+passport.count("ecl:")+passport.count("pid:")
    if number == 7:
        print("Valid")
        ergebnis+=1
    else:
        print("not Valid")

for i in range(len(daten)):
    passport+=daten[i]
    if daten[i] == "":
        print(passport)
        check(passport)
        passport=""

print(ergebnis)
