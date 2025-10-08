class Player:
    symbol: str

    def __init__(self, symbol) -> None:
        self.symbol = symbol


    def win(self) -> None:
        print(f"player {self.symbol} wins!")

