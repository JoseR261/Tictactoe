from constants import EMPTY
from player import Player


class Board:
    number_columns: int
    number_rows: int

    def __init__(self, number_columns: int, number_rows: int):
        self.number_columns = number_columns
        self.number_rows = number_rows
        self.cells = [
            [EMPTY for _ in range(number_columns)] for _ in range(number_rows)
        ]

    # TODO: Write method "display" that prints the board
    # You'll need my help
    def display(self) -> None:
        print("==================")
        for row in self.cells:
            for col in row:
                print(col, end=" ")
            print()
        print("==================")

    def is_move_valid(self, position: int) -> bool:
        if position < 1:
            print("Enter a valid position between 1 and 9")
            return False
        if position > self.number_rows * self.number_columns:
            print("Enter a valid position between 1 and 9")
            return False
        x, y = self.convert_position(position - 1)
        if self.cells[y][x] != EMPTY:
            return False
        return True

    def convert_position(self, position: int) -> tuple[int, int]:
        x = position % self.number_columns
        y = position // self.number_columns
        return x, y

    def play_move(self, position: int, player: Player) -> None:
        x, y = self.convert_position(position - 1)
        self.cells[y][x] = player.symbol

    def is_full(self) -> bool:
        for row in self.cells:
            for cell in row:
                if cell == EMPTY:
                    return False
        return True

    def number_of_moves(self) -> int:
        result = 0
        for row in self.cells:
            for cell in row:
                if cell != EMPTY:
                    result += 1
        return result
    def copy(self):
        new_board = Board(self.number_columns, self.number_rows)

        for i, r in enumerate(self.cells):
            for j, c in enumerate(r):
                new_board.cells[i][j] = c

        return new_board

    def winner(self) -> str:
        if self.cells[0][0] == self.cells[0][1] == self.cells[0][2] != EMPTY:
            return self.cells[0][0]
        if self.cells[1][0] == self.cells[1][1] == self.cells[1][2] != EMPTY:
            return self.cells[1][0]
        if self.cells[2][0] == self.cells[2][1] == self.cells[2][2] != EMPTY:
            return self.cells[2][0]
        if self.cells[0][0] == self.cells[1][0] == self.cells[2][0] != EMPTY:
            return self.cells[0][0]
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != EMPTY:
            return self.cells[0][0]
        if self.cells[0][2] == self.cells[1][2] == self.cells[2][2] != EMPTY:
            return self.cells[0][2]
        if self.cells[0][1] == self.cells[1][1] == self.cells[2][1] != EMPTY:
            return self.cells[0][1]
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] != EMPTY:
            return self.cells[0][2]
        return EMPTY

    # if player.simbol == self.cells[0][0] == self.cells[0][1]  == self.cells[0][2]:
    #     return True
