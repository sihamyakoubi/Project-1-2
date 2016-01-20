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
    def __init__(self, id, rcp, bot, turn, hp):
        self.playerID = id
        self.remainingConditionPoints = rcp
        self.isComputer = bot
        self.currentTurn = turn
        self.healthPoints = hp
