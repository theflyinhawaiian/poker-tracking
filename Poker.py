class Player:
    sittingOut = False
    hasFolded = False
    turnHistory = []

    def __init__(self, name):
        self.name = name

class Hand:
    cards = []

    def __init__(self, card1, card2):
        cards.append(card1)
        cards.append(card2)
