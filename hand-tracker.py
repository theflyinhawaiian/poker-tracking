import os
from Poker import Player, Hand, Action

maxPlayers = 6
numStreets = 4
smallBlind = 0
bigBlind = 0
numCommands = 4
players = [None] * maxPlayers
handHistories = []

def initPlayers():
    global players, buttonPlayerIdx
    for i in range(maxPlayers):
        playerName = input(f"Input name for player {i+1} or enter to skip: ")
        if(playerName):
            players[i] = Player(playerName)
            if(i == 0):
                players[i].isSelf = True
        else:
            players[i] = Player("")
            players[i].sittingOut = True

def printMenu():
    print("1. Start hand")
    print("2. Modify players/settings")
    print("3. View Past Hands")
    print("4. Quit")

def acquireInput(maxChoice):
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

def getStreetName(i):
    if(i == 0):
        return "Preflop"
    elif(i == 1):
        return "Flop"
    elif(i == 2):
        return "Turn"
    elif(i == 3):
        return "River"
    else:
        return "Invalid street"

def getCommunityCards(street, communityCards):
    if(street == 1):
        communityCards += input("Input flop cards separated by a space: ").split()
    if(street == 2):
        communityCards.append(input("Input turn card: "))
    if(street == 3):
        communityCards.append(input("Input river card: "))

def showActionsByStreet(streetActions):
    count = 0
    for street in streetActions:
        print(f"{getStreetName(count)}")
        for action in street:
            if(action.action != "o"):
                print(action.toString())
        count = count + 1

def trackHand():
    global buttonPlayerIdx, maxPlayers, players
    holeCard1 = input("Input first hole card: ")
    holeCard2 = input("Input second hole card: ")
    startingPlayerIdx = int(input("Which seat is UTG? ")) - 1

    hand = Hand(holeCard1, holeCard2)
    communityCards = []
    actionsByStreet = []
    playerHands = []
    for player in players:
        if(not player.sittingOut):
            player.hasFolded = False

    for i in range(numStreets):
        cont = True
        if(i != 0):
            playerIdx = (startingPlayerIdx - 2) % maxPlayers
        else:
            playerIdx = startingPlayerIdx
        playerActions = []

        if(i > 0):
            getCommunityCards(i, communityCards)

        while(cont):
            currentPlayer = players[playerIdx]
            if(currentPlayer.hasFolded or currentPlayer.sittingOut):
                action = "o"
            else:
                action = input(f"({getStreetName(i)}) Input player {playerIdx} ({players[playerIdx].name})'s action: ")

            if(action.lower() == "end" or action.lower() == "e"):
                cont = False
            else:
                if(action.lower() == "fold" or action.lower() == "f"):
                    currentPlayer.hasFolded = True
                if(action.lower() == "o"):
                    currentPlayer.sittingOut = True
                playerActions.append(Action(players[playerIdx].name, action))

            playerIdx = (playerIdx + 1) % maxPlayers

        actionsByStreet.append(playerActions)

    for player in players:
        if(not (player.hasFolded or player.sittingOut or player.isSelf)):
            playerHands.append(input(f"Input {player.name}'s cards, separated by spaces: ").split())

    print("Your hand: " + hand.toString())
    print(communityCards)
    print(playerHands)
    showActionsByStreet(actionsByStreet)

def processInput(cmd):
    if(cmd == "1"):
        trackHand()

cont = True
cmd = ""

initPlayers()

while(cont):
    os.system('cls')
    printMenu()
    cmd = acquireInput(numCommands)
    if(cmd == "q"):
        cont = False
    else:
        processInput(cmd)
        input()
