from player import Player
from board import Board
from src.constants import EMPTY


class Game:
    board: Board
    players: list[Player]
    scores: list[int]
    turn: int

    def __init__(self, board: Board, players: list[Player]):
        self.board = board
        self.players = players
        self.scores = []
        self.is_over = False


        for _ in players:
            self.scores.append(0)

        self.turn = 0

    def play(self) -> int:
        while True:
            current_player = self.players[self.turn]
            while True:
                position = current_player.get_position(self.board, self.players)
                if self.board.is_move_valid(position):
                    break
            print("Move:", position)

            self.board.play_move(position, current_player)
            self.board.display()
            if self.board.winner() != EMPTY:
                current_player.win()
                return self.turn
            self.turn = (self.turn + 1) % len(self.players)
            if self.board.is_full():
                print("Game tied")
                return -1




