PLAYER_1 = "X"
PLAYER_2 = "O"
EMPTY = " "


def who_wins(game: list[str]) -> str:
    pass


def game_is_full(game: list[str]) -> bool:
    pass


def player_move(game: list[str], player: str) -> list[str]:
    pass


def print_game(game: list[str]) -> None:
    pass


def main() -> None:
    pass


def game_is_full(game: list[str]):
    for cell in game:
        if cell == EMPTY:
            return False
    return True


def who_wins(game: list[str]) -> str:
    if game[0] == game[1] == game[2] and game != EMPTY:
        return game[0]
    if game[0] == game[3] == game[6] and game != EMPTY:
        return game[0]
    if game[0] == game[4] == game[8] and game != EMPTY:
        return game[0]
    if game[1] == game[4] == game[7] and game != EMPTY:
        return game[1]
    if game[2] == game[5] == game[8] and game != EMPTY:
        return game[2]
    if game[2] == game[4] == game[6] and game != EMPTY:
        return game[2]
    if game[6] == game[7] == game[8] and game != EMPTY:
        return game[6]
    if game[3] == game[4] == game[5] and game != EMPTY:
        return game[3]

    return EMPTY


def play(game: list[str], player: str, position: int) -> list[str]:
    pass


def is_authorized_move(game: list[str], position: int) -> bool:
    pass


def display(game: list[str]) -> None:
    for i in range(len(game)):
        print(game[i], end=" ")
        if (i + 1) % 3 == 0:
            print()


if __name__ == "__main__":
    while True:
        game = [EMPTY] * 9
        current_player = PLAYER_1

        while True:
            try:
                position = int(input("Enter a position (1-9): "))
                if position < 1 or position > 9:
                    print("Please enter a number between 1 and 9")
                    continue
            except ValueError:
                print("Please enter a valid number")
                continue
            else:
                if not is_authorized_move(game, position):
                    print("Please enter a valid position")
                    continue
                break

        game = play(game, current_player, position)
        display(game)

        if game_is_full(game):
            print("Game is full!")
            break

        winner = who_wins(game)
        if winner != EMPTY:
            print(f"Player {winner} wins!")
            break

        current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1
