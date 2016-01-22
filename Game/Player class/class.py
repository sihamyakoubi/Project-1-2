class Node:
    def __init__(self, head, tail):
        self.tail = tail
        self.head = head
        self.isEmpty = False

class Empty: 
    def __init__(self):
        self.isEmpty = True
empty = Empty()

class Player:
    def __init__(self, ID, rcp, bot, ct, hp):
        self.playerID = ID
        self.remainingConditionPoints = rcp
        self.isComputer = bot
        self.currentTurn = ct
        self.healthPoints = hp

    def playerCreation(self, a, b):
        self.playerID = a + 1
        self.remainingConditionPoints = 15
        self.healthPoints = 100
        if b == 0:
            self.isComputer = False
        elif b == 1:
            self.isComputer = True
        self.currentTurn = False

