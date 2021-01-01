import queue


def loadPuzzle():
    daten = []
    datei = open("Daten.txt", "r")
    daten = datei.read().splitlines()
    datei.close()
    return daten


def loadDecks(puzzle):
    target = player1Deck
    for zeile in puzzle:
        if zeile == "Player 1:":
            target = player1Deck
        elif zeile == "Player 2:":
            target = player2Deck
        else:
            target.put(zeile)


def printDeck(deck):
    for qItem in list(deck.queue):
        print(qItem, end=" ")
    print("\n")



def startGame(player1Deck, player2Deck):
    roundCounter = 1
    while not player1Deck.empty() and not player2Deck.empty():
        cardPlayer1, cardPlayer2 = player1Deck.get(), player2Deck.get()
        print("Runde: ", roundCounter, "\nPlayer 1 card: ", cardPlayer1,
              "\nPlayer 2 card: ", cardPlayer2)
        winner = determineWinner(cardPlayer1, cardPlayer2)
        print("Gewinner ist: ", winner, "\n")
        if winner == "Player 1":
            player1Deck.put(cardPlayer1)
            player1Deck.put(cardPlayer2)
        else:
            player2Deck.put(cardPlayer2)
            player2Deck.put(cardPlayer1)
        roundCounter += 1
    if not player1Deck.empty():
        return player1Deck
    else:
        return player2Deck


def determineWinner(cardPlayer1, cardPlayer2):
    if int(cardPlayer1) < int(cardPlayer2):
        winner = "Player 2"
    else:
        winner = "Player 1"
    return winner


def determinePuzzleSolution(winner):
    solution = 0
    counter = len(list(winner.queue))
    for qItem in list(winner.queue):
        #print(qItem, end=" ")
        solution = solution + (counter * int(qItem))
        counter -= 1
    print(solution)
    

puzzle = loadPuzzle()
player1Deck, player2Deck = queue.Queue(), queue.Queue()
loadDecks(puzzle)
winner = startGame(player1Deck, player2Deck)
determinePuzzleSolution(winner)
