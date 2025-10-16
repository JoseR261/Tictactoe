import random
from constants import EMPTY
import time

class Player:
    symbol: str

    def __init__(self, symbol) -> None:
        self.symbol = symbol

    def win(self) -> None:
        print(f"player {self.symbol} wins!")

    def get_position(self, board, players) -> int:
        while True:
            position = input("Enter your position: ")
            try:
                return int(position)
            except ValueError:
                continue


class AIPlayer(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
        self.choice = None

    def get_position_old(self, board, players) -> int:
        if board.cells[1][1] == EMPTY:
            return 5
        winning = self.win_play_for_simbol(board, self.symbol)
        if winning > 0:
            return winning

        """
        other_players = []
        for row in board.cells:
            for cell in row:
                if cell not in other_players and cell != EMPTY and cell != self.symbol:
                    other_players.append(cell)
        
        for symbol in other_players:
        """

        winning = self.win_play_for_simbol(board, "O")
        print("O winning", winning)
        if winning > -1:
            return winning

        return random.randint(1, 9)

    def win_play_for_simbol(self, board, s: str) -> int:
        if (
            board.cells[0][0] == s
            and board.cells[0][1] == s
            and board.cells[0][2] == EMPTY
        ):  # r
            return 3
        if (
            board.cells[0][0] == s
            and board.cells[1][0] == s
            and board.cells[2][0] == EMPTY
        ):  # c
            return 7
        if (
            board.cells[0][0] == s
            and board.cells[1][1] == s
            and board.cells[2][2] == EMPTY
        ):  # cd
            return 9
        if (
            board.cells[1][0] == s
            and board.cells[1][1] == s
            and board.cells[1][2] == EMPTY
        ):  # r
            return 6
        if (
            board.cells[0][1] == s
            and board.cells[1][1] == s
            and board.cells[2][1] == EMPTY
        ):  # c
            return 8
        if (
            board.cells[0][2] == s
            and board.cells[1][2] == s
            and board.cells[2][2] == EMPTY
        ):  # c
            return 9
        if (
            board.cells[2][0] == s
            and board.cells[2][1] == s
            and board.cells[2][2] == EMPTY
        ):  # r
            return 9
        if (
            board.cells[0][2] == s
            and board.cells[1][1] == s
            and board.cells[2][0] == EMPTY
        ):  # cd 8/8
            return 7
        if (
            board.cells[2][0] == s
            and board.cells[1][1] == s
            and board.cells[0][2] == EMPTY
        ):  # cd
            return 3
        if (
            board.cells[0][2] == s
            and board.cells[0][1] == s
            and board.cells[0][0] == EMPTY
        ):  # r
            return 1
        if (
            board.cells[2][0] == s
            and board.cells[1][0] == s
            and board.cells[0][0] == EMPTY
        ):  # c
            return 1
        if (
            board.cells[2][2] == s
            and board.cells[1][1] == s
            and board.cells[0][0] == EMPTY
        ):  # cd
            return 1
        if (
            board.cells[1][2] == s
            and board.cells[1][1] == s
            and board.cells[1][0] == EMPTY
        ):  # r
            return 4
        if (
            board.cells[2][1] == s
            and board.cells[1][1] == s
            and board.cells[0][1] == EMPTY
        ):  # c
            return 2
        if (
            board.cells[2][2] == s
            and board.cells[1][2] == s
            and board.cells[0][2] == EMPTY
        ):  # c
            return 3
        if (
            board.cells[2][2] == s
            and board.cells[2][1] == s
            and board.cells[2][0] == EMPTY
        ):  # r 8/8
            return 7
        return -1

    def get_position(self, board, players) -> int:
        print(board.display())
        me, opponent = None, None

        for player in players:
            if player.symbol == self.symbol:
                me = player
            else:
                opponent = player

        result = self.minimax(0, board, me, opponent)
        print("Choice returned: ", self.choice)
        return self.choice

    def score(self, board) -> int:
        symbol = board.winner()
        if symbol == self.symbol:
            return 10
        elif symbol == EMPTY:
            return 0
        else:
            return -10

    def minimax(self, depth, board, current_player, other_player) -> int:
        if board.is_full() or board.winner() != EMPTY:
            return self.score(board)

        scores = []
        moves = []

        for move in range(1, 10):
            x, y = board.convert_position(move - 1)
            if board.cells[y][x] == EMPTY:
                move_board = board.copy()
                move_board.play_move(move, current_player)
                scores.append(self.minimax(depth + 1, move_board, other_player, current_player))
                moves.append(move)

        if current_player.symbol == self.symbol:
            max_score = max(scores)
            max_score_index = scores.index(max_score)
            self.choice = moves[max_score_index]
            return scores[max_score_index]
        else:
            min_score = min(scores)
            min_score_index = scores.index(min_score)
            self.choice = moves[min_score_index]
            return scores[min_score_index]
