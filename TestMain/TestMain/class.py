class Node:
    def __init__(self, head, tail):
        self.tail = tail
        self.head = head
        self.IsEmpty = False

class Empty: 
    def __init__(self):
        self.IsEmpty = True

Empty = Empty()
