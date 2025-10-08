from board import Board
from player import Player
from game import Game


board = Board(3,3)
board.display()

if __name__ == "__main__":
    player1 = Player("X")
    player2 = Player("O")
    game = Game(board, [player1, player2])

    while




