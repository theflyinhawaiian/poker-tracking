import json

class Player:
    sittingOut = False
    hasFolded = False
    isSelf = False
    turnHistory = []

    def __init__(self, name):
        self.name = name

class Hand:
    cards = []

    def __init__(self, card1, card2, communityCards, playerCards, actionsByStreet):
        self.cards.append(card1)
        self.cards.append(card2)
        self.communityCards = communityCards
        self.playerCards = playerCards
        self.actionsByStreet = actionsByStreet

    def toJson(self):
        return json.dumps(self, default=lambda obj: obj.__dict__)

class Action:
    def __init__(self, playerName, action):
        self.playerName = playerName
        self.action = action

    def getReadableAction(self, action):
        if(action == "f"):
            return "folded"
        if(action == "ch"):
            return "check"
        if(action == "c"):
            return "call"
        if(action[0] == "b"):
            return f"bet {action[1:]}"
        if(action[0] == "r"):
            return f"raise {action[1:]}"

    def toString(self):
        return f"{self.playerName}: {self.getReadableAction(self.action)}"
