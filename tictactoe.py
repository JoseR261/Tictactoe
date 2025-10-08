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

def play(game: list[str], player: str, position: int) -> list[str]:
    pass

def is_authorized_move(game: list[str], position: int) -> bool:
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

def display(game: list[str]) -> None:
    for i in range(len(game)):
        print(game[i], end=" ")
        if (i + 1) % 3 == 0:
            print()

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

if __name__ == "__main__":
            print(f"Player {winner} wins!")
            break

        print("Current player:", current_player)
        current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1
        print("Current player:", current_player)
