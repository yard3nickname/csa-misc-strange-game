from table import Table
from player import Player
from loop import Loop
from ui import UI
from magic_square import MagicSquare


class StrangeGame:
    def __init__(self):
        self.table = Table([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.p1 = Player('X')
        self.p2 = Player('O')
        self.loop = Loop(self.p1, self.p2)
        self.magic_square = MagicSquare(3)

    def play(self):
        UI.print_strange_game_intro()
        UI.wait_key_press()
        self.loop.do_loop(self.table, self.p1, self.p2, self.magic_square)
