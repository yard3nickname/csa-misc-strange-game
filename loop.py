from round import Round
from ui import UI


class Loop:
    def __init__(self, p1, p2):
        # ?(score board)

        self.round = 1

    def do_loop(self, table, p1, p2, magic_square):
        UI.print_round(self.round)
        UI.print_line_separator()
        # play round
        game_condition = Round.play(table, p1, p2, magic_square)

        # reset table's cards
        table.reset_cards()

        print(game_condition)

        # reset players' cards
        p1.reset_cards()
        p2.reset_cards()

        self.round += 1

        # loop
        self.do_loop(table, p1, p2, magic_square)
