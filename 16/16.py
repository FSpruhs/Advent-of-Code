START_NEARBY_TICKETS = 25


def readValidNumbers(puzzle):
    validNumbers = []
    for line in puzzle:
        if line == "":
            break
        slicedString = line[line.index(":")+2:].replace(" ", "")
        splitString = slicedString.split("or")
        firstNumberPair = splitString[0].split("-")
        secondNumberPair = splitString[1].split("-")
        for i in range(int(firstNumberPair[0]), int(firstNumberPair[1])+1):
            if i not in validNumbers:
                validNumbers.append(i)
        for i in range(int(secondNumberPair[0]), int(secondNumberPair[1])+1):
            if i not in validNumbers:
                validNumbers.append(i)
    return validNumbers


def readPuzzle():
    daten = []
    datei = open("Daten.txt", "r")
    daten = datei.read().splitlines()
    datei.close()
    return daten


def readNearbyTickets(puzzle):
    nearbyTicketNumbers = []
    for zeile in range(START_NEARBY_TICKETS, len(puzzle)):
        splitZeile = puzzle[zeile].split(",")
        for ticketNumber in splitZeile:
            nearbyTicketNumbers.append(int(ticketNumber))
    return nearbyTicketNumbers


def checkValidTicketNumbers(validNumbers, nearbyTicketNumbers):
    unvalidNumbers = []
    for number in nearbyTicketNumbers:
        if number not in validNumbers:
            unvalidNumbers.append(number)
    return unvalidNumbers


puzzle = readPuzzle()
validNumbers = readValidNumbers(puzzle)
nearbyTicketNumbers = readNearbyTickets(puzzle)
unvalidNumbers = checkValidTicketNumbers(validNumbers, nearbyTicketNumbers)
print(sum(unvalidNumbers))
