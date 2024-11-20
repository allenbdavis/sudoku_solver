import numpy as np
import random

#CLASSES
class Board:

    class Square:
        def __init__(self, row:int, col:int, value:int, locked:bool):
            self.row = row
            self.col = col
            self.value = value
            self.locked = locked

        def __str__(self):
            return self.value

    def __init__(self):
        self.grid = [[self.Square(row, col, random.randint(0,9), False) for col in range(9)] for row in range(9)]

    def __str__(self):
        return '\n'.join([' '.join([str(square.value) for square in row]) for row in self.grid])

    def solve(self):
        return

#OBJECT CREATION
bo = Board()
print(bo)

bo.solve()

