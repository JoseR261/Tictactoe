from constants import EMPTY

class Board:

    number_columns: int
    number_rows: int

    def __init__(self, number_columns: int, number_rows: int):
        self.number_columns = number_columns
        self.number_rows = number_rows
        self.cells = [[EMPTY for _ in range(number_columns)] for _ in range(number_rows)]

    # TODO: Write method "display" that prints the board
    # You'll need my help
    def display(self) -> None:
        for row in self.cells:
            for col in row:
                print(col, end=' ')
            print()


