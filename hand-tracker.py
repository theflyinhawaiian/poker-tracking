import os
from Poker import Player

maxPlayers = 6
numStreets = 4
smallBlind = 0
bigBlind = 0
numCommands = 4
players = [None] * maxPlayers
playerHistories = []
buttonPlayerIdx = 0

def initPlayers():
    global players, buttonPlayerIdx
    for i in range(maxPlayers):
        playerName = input(f"Input name for player {i+1} or enter to skip: ")
        if(playerName):
            players[i] = Player(playerName)

        buttonPlayerIdx = int(input("Which player is on the button?"))

def printMenu():
    print("1. Start hand")
    print("2. Modify players/settings")
    print("3. View Past Hands")
    print("4. Quit")

def acquireNumericalInput(maxChoice):
    validInput = False
    while(not validInput):
        try:
            userInput = input("What would you like to do? ")
            if(userInput == "q"):
                validInput = True
            elif(int(userInput) >= 1 and int(userInput) <= maxChoice):
                validInput = True
            else:
                print("Invalid Input!")
        except:
            print("Invalid input!")

    return userInput

def trackHand():
    global buttonPlayerIdx, maxPlayers, players
    holeCard1 = input("Input first hole card: ")
    holeCard2 = input("Input second hole card: ")

    hand = Hand(holeCard1, holeCard2)

    for i in range(numStreets):
        bettingClosed = False
        playerIdx = (buttonPlayerIdx + 3) % maxPlayers
        while(not bettingClosed):
            currentPlayer = players[playerIdx]
            if(currentPlayer.hasFolded or currentPlayer.sittingOut):
                action = "out"
            else:
                action = input(f"Input player {playerIdx} ({players[playerIdx].name})'s action: ")



            playerIdx = (playerIdx + 1) % maxPlayers

def processInput(cmd):
    if(cmd == 1):
        trackHand()
        printHandInfo()

cont = True
cmd = ""

initPlayers()

while(cont):
    os.system('cls')
    printMenu()
    cmd = acquireNumericalInput(numCommands)
    if(cmd == "q"):
        cont = False
    else:
        processInput(cmd)
        input()
