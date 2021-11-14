from round import Round


class Loop:
    def __init__(self, p1, p2):
        # ?(score board)

        self.round = 0

    def do_loop(self, table, p1, p2):
        game_condition = Round.play(table, p1, p2)
        print(game_condition)
        self.round += 1

        # reset
        table.reset_cards()
        p1.reset_cards()
        p2.reset_cards()

        # loop
        self.do_loop(table, p1, p2)
