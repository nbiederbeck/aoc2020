"""Thu, 10 Dec"""
from puzzles import get_puzzle

PUZZLE = get_puzzle(10)
EXAMPLE = [
    "16",
    "10",
    "15",
    "5",
    "1",
    "11",
    "7",
    "19",
    "6",
    "12",
    "4",
]
EXAMPLE_LARGE = [
    "28",
    "33",
    "18",
    "42",
    "31",
    "14",
    "46",
    "20",
    "48",
    "47",
    "24",
    "23",
    "49",
    "45",
    "19",
    "38",
    "39",
    "11",
    "1",
    "32",
    "25",
    "35",
    "8",
    "17",
    "7",
    "9",
    "4",
    "2",
    "34",
    "10",
    "3",
]


def test_one():
    """Test Part One"""
    assert one(EXAMPLE) == 35
    assert one(EXAMPLE_LARGE) == 220


def test_two():
    """Test Part Two"""
    assert two(EXAMPLE) == 8
    assert two(EXAMPLE_LARGE) == 19208


def one(puzzle: list):
    """Part One"""
    diffs = {1: 0, 2: 0, 3: 0}

    adapters = sorted([int(p) for p in puzzle] + [0])
    adapters.append(adapters[-1] + 3)

    for i, a in enumerate(adapters[1:]):
        diff = a - adapters[i]
        diffs[diff] += 1

    return diffs[1] * diffs[3]


def is_valid_arrangement(adapters, device, outlet=0):
    adapters = [outlet] + adapters + [device]
    for i, a in enumerate(adapters[1:]):
        diff = a - adapters[i]
        if diff > 3:
            return False

    return True


def two(puzzle: list):
    """Part Two"""
    adapters = sorted([int(p) for p in puzzle])
    device = max(adapters) + 3

    n_valid_arrangements = 0

    # something like this but recursive
    for i in range(len(adapters)):
        adaps = adapters.copy()
        for j in range(3):
            if j + i >= len(adapters):
                break
            adaps.pop(i)
            if is_valid_arrangement(adaps, device=device):
                print(adaps)
                n_valid_arrangements += 1

    return n_valid_arrangements


if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", two(PUZZLE))
