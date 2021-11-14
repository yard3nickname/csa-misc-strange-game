from table import MoveUnavailableError
from utils import is_any_comb3_sum_eq15

class RoundCondition:
    pass


class InProgress(RoundCondition):
    pass


class Win(RoundCondition):
    pass


class Tie(RoundCondition):
    pass


class Round:
    @staticmethod
    def play(table, p1, p2):
        players = [p1, p2]

        while True:
            for player in players:

                print(table.cards)
                print(player.cards)

                Round.do_move(table, player)
                if Round.is_win(player):
                    return Win()
                if Round.is_tie(table):
                    return Tie()

    @staticmethod
    def do_move(table, player):
        try:
            player.append_card(table.pop_card(player.choose_move()))
        except MoveUnavailableError as e:
            print(e)
            Round.do_move(table, player)

    @staticmethod
    def is_win(player):
        return is_any_comb3_sum_eq15(player.cards)

    @staticmethod
    def is_tie(table):
        return not len(table.cards)
