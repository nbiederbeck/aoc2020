"""Tue, 22 Dec"""
from puzzles import get_puzzle

PUZZLE = get_puzzle(22)
EXAMPLE = [
    "Player 1:",
    "9",
    "2",
    "6",
    "3",
    "1",
    "",
    "Player 2:",
    "5",
    "8",
    "4",
    "7",
    "10",
]


def test_one():
    """Test Part One"""
    assert one(EXAMPLE) == 306


def test_two():
    """Test Part Two"""
    assert two(EXAMPLE) == False


def split_players_hands(puzzle):
    empty_line = puzzle.index("")
    p1 = [int(x) for x in puzzle[1:empty_line]]
    p2 = [int(x) for x in puzzle[empty_line + 2:]]
    return p1, p2


def calculate_score(deck: list) -> int:
    score = 0
    for card, number in zip(deck, range(len(deck), 0, -1)):
        s = card * number
        score += s

    return score


def one(puzzle: list):
    """Part One"""
    p1, p2 = split_players_hands(puzzle)

    # game loop
    turn = 0
    while True:
        turn += 1
        # print(f"-- Round {turn: 3d} --")
        # print(f"Player 1's deck: {p1}")
        # print(f"Player 2's deck: {p2}")

        p1_played = p1.pop(0)
        p2_played = p2.pop(0)

        # print(f"Player 1 plays: {p1_played}")
        # print(f"Player 2 plays: {p2_played}")

        if p1_played > p2_played:
            p1.append(p1_played)
            p1.append(p2_played)
            # print("Player 1 wins the round!")
        elif p2_played > p1_played:
            p2.append(p2_played)
            p2.append(p1_played)
            # print("Player 2 wins the round!")
        else:
            raise ValueError("Same cards were played.")

        print()

        if len(p1) == 0:
            winner = p2
            break
        if len(p2) == 0:
            winner = p1
            break

    # print("\n")
    # print("==== Post-game results ==")
    # print(f"Player 1's deck: {p1}")
    # print(f"Player 2's deck: {p2}")

    score = calculate_score(winner)

    return score


def two(puzzle: list):
    """Part Two"""
    return NotImplemented


if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", two(PUZZLE))
