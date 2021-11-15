from copy import deepcopy


class UI:
    @staticmethod
    def print_strange_game_intro():
        print(
            """
==================
   Strange Game
==================

* We take turns picking numbers from 1 to 9.
* The same number can't be chosen twice.
* First player to hold 3 numbers which, when added, make 15, wins.
* If all numbers are exhausted without a winner, the game is a tie.
* We will play 15 rounds of this game, alternating who goes first.
* Win or tie all 15 rounds and I'll give you the flag.





"""
        )

    @staticmethod
    def wait_key_press():
        input('Press any key...')

    @staticmethod
    def print_round(n):
        print(f'Round {n}!')

    @staticmethod
    def print_line_separator():
        print('==================================================')

    @staticmethod
    def print_available_moves(table):
        print('Available moves: ' + ' '.join(map(str, table.cards)))

    @staticmethod
    def print_past_moves(p1, p2):
        print('Past moves:')
        UI.print_player_moves(p1)
        UI.print_player_moves(p2)

    @staticmethod
    def print_player_moves(player):
        print(f'\t\t Player {player.name}: ' + ' '.join(map(str, player.cards)))

    @staticmethod
    def print_game_still_in_progress():
        print('Game still in progress')

    @staticmethod
    def print_past_moves_magic_square(p1, p2, magic_square):
        magic_square_view = deepcopy(magic_square)
        players = [p1, p2]

        for player in players:
            for card in player.cards:
                x, y = magic_square_view.get_cell_index(card)
                magic_square_view.set_cell_index(x, y, player.name)

        for i in range(magic_square.n):
            for j in range(magic_square.n):
                print('%2s ' % (magic_square_view.magic_square[i][j]),
                      end='')

                # To display output
                # in matrix form
                if j == magic_square.n - 1:
                    print()
