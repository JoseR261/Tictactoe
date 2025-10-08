from constants import EMPTY


class Board:
    def __init__(self, columns: int, rows: int):
        self.columns = columns
        self.rows = rows
        self.cells = [[EMPTY for _ in range(columns)] for _ in range(rows)]

    # TODO: Write method "display" that prints the board
    # You'll need my help
    def display(self) -> None:
        ...