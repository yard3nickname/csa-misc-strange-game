from table import MoveUnavailableError
from utils import is_match_game_object
from ui import UI


class RoundCondition:
    pass


class InProgress(RoundCondition):
    pass


class Win:
    def __init__(self, player):
        self.winner = player

    def __str__(self):
        return f'Winner: Player {self.winner.name}'


class Tie:
    def __str__(self):
        return 'Tie'


class Round:
    @staticmethod
    def play(table, p1, p2, magic_square):
        players = [p1, p2]
        # current player index
        cpi = 0

        while True:
            UI.print_available_moves(table)
            UI.print_past_moves(p1, p2)
            UI.print_game_still_in_progress()
            UI.print_past_moves_magic_square(p1, p2, magic_square)

            Round.do_move(table, players[cpi])
            if Round.is_win(players[cpi]):
                return Win(players[cpi])
            if Round.is_tie(table):
                return Tie()

            UI.print_line_separator()
            UI.print_line_separator()

            cpi = (cpi + 1) % 2

    @staticmethod
    def do_move(table, player):
        try:
            player.append_card(table.pop_card(player.choose_move()))
        except MoveUnavailableError as e:
            print(e)
            Round.do_move(table, player)

    @staticmethod
    def is_win(player):
        return is_match_game_object(player.cards)

    @staticmethod
    def is_tie(table):
        return not len(table.cards)

    @staticmethod
    def update_strange_magic_square(p1, p2, strange_magic_square):
        players = [p1, p2]

        for player in players:
            for card in player.cards:
                cellX, cellY = strange_magic_square.get_cell_index(card)
                strange_magic_square.set_cell_index(cellX, cellY, player.name)
