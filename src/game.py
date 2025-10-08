from math import trunc

from board import Board
from player import Player

class Game:
    board: Board
    players: list[Player]
    scores: list[int]
    turn: int

    def __init__(self, board: Board, players: list[Player]):
        self.board = board
        self.players = players
        self.scores = []
        for _ in players:
            self.scores.append(0)

        self.turn = 0

    def play(self):
        play_x, play_y = self.players[self.turn].get_move()
        while not self.board.is_valid_move(play_x, play_y):
            play_x, play_y = self.players[self.turn].get_move()

        self.board.make_move(play_x, play_y)
        self.turn = self.turn + 1 % len(self.players)
    # Write the list of attributes here

    # Write the init method
