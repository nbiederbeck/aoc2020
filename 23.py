"""Wed, 23 Dec"""
from puzzles import get_puzzle

PUZZLE = "284573961"
EXAMPLE = "389125467"


def test_one():
    """Test Part One"""
    assert one(EXAMPLE, n_moves=10) == "92658374"
    assert one(EXAMPLE, n_moves=100) == "67384529"


def test_two():
    """Test Part Two"""
    assert two(EXAMPLE) == False


def print_cups(cups, cup):
    p = ""
    for c in cups:
        if c != cup:
            p += f"{c} "
        else:
            p += f"({c}) "

    print("cups:", p)


def find_destination(cups, idx):
    cup = cups[idx]
    while True:
        cup = cup - 1
        if cup < min(cups):
            cup = max(cups)
        if cup not in cups:
            continue
        break
    return cup


def one(puzzle: list, n_moves=100):
    """Part One"""
    cups = list(map(int, list(puzzle)))

    idx = cups.index(1) + 1
    idx = 0
    cup = cups[idx]

    for m in range(n_moves):
        print(f'-- move {m+1: 3d} --')

        print_cups(cups, cup)
        pickup = [cups.pop(idx + 1) for _ in range(3)]
        print("pick up:", pickup)

        dest = find_destination(cups, idx)
        print(f"destination: {dest}")

        dest_idx = cups.index(dest)
        for cup in pickup[::-1]:
            cups.insert(dest_idx + 1, cup)

        idx = (idx + 1) % len(cups)
        cup = cups[idx]

    return NotImplemented


def two(puzzle: list):
    """Part Two"""
    return NotImplemented


if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", two(PUZZLE))
