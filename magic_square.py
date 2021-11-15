from utils import generate_magic_square


class MagicSquare:
    def __init__(self, n):
        self.n = n
        self.magic_square = generate_magic_square(n)

    def get_cell_index(self, cell):
        for i in range(self.n):
            for j in range(self.n):
                if cell == self.magic_square[i][j]:
                    return i, j

        raise ValueError

    def set_cell_index(self, x, y, cell):
        self.magic_square[x][y] = cell
