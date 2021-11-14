from table import Table
from player import Player
from loop import Loop


class StrangeGame:
    def __init__(self):
        self.table = Table([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.p1 = Player('X')
        self.p2 = Player('O')
        self.loop = Loop(self.p1, self.p2)

    def play(self):
        self.loop.do_loop(self.table, self.p1, self.p2)
