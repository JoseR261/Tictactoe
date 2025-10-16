from game import Game
from src.player import Player, AIPlayer
from src.board import Board

if __name__ == "__main__":
    player1 = Player("O")
    player2 = AIPlayer("X")
    score = [0, 0]
    while True:

        board = Board (3,3)
        game = Game(board,[player1, player2])

        winner = game.play()
        if winner == -1:
            print("score:", score)
            pass
        else:
            score[winner] = score[winner] + 1
            print("score:",score)














