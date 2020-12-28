LENGTH_TERM = 2
solutioPart1 = 0


def readPuzzle():
    daten = []
    datei = open("Daten.txt", "r")
    daten = datei.read().splitlines()
    datei.close()
    return daten


def calculateWithoutParentheses(puzzle):
    actualNumber = int(puzzle[0])
    for i in range(len(puzzle)//LENGTH_TERM):
        calculateOperation = puzzle[1 + LENGTH_TERM*i]
        calculateNumber = puzzle[2 + LENGTH_TERM*i]
        if calculateOperation == "+":
            actualNumber += int(calculateNumber)
        else:
            actualNumber *= int(calculateNumber)
    return actualNumber


def dissolveParentheses(puzzle):
    newPuzzle = puzzle
    while ")" in newPuzzle:
        indexClosedClip = 0
        indexOpenClip = 0
        for i in range(len(newPuzzle)):
            if newPuzzle[i] == ")":
                indexClosedClip = i
                for j in range(indexClosedClip, 0, -1):
                    if newPuzzle[j] == "(":
                        indexOpenClip = j
                        break
                if indexOpenClip != 0:
                    break
        innerParentheses = newPuzzle[indexOpenClip+1:indexClosedClip]
        solution = newPuzzle[:indexOpenClip]
        solution.append(calculateWithoutParentheses(innerParentheses))
        solution += newPuzzle[indexClosedClip+1:]
        newPuzzle = solution
    return newPuzzle


puzzle = readPuzzle()
for line in puzzle:
    puzzleFormat = list(line.replace(" ", ""))
    print(puzzleFormat)
    puzzleFormat = dissolveParentheses(puzzleFormat)
    solution = calculateWithoutParentheses(puzzleFormat)
    print(solution)
    solutioPart1 += solution
print(solutioPart1)
