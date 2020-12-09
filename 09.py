"""Wed,  9 Dec"""
from puzzles import get_puzzle

PUZZLE = get_puzzle(9)
EXAMPLE = [
    "35",
    "20",
    "15",
    "25",
    "47",
    "40",
    "62",
    "55",
    "65",
    "95",
    "102",
    "117",
    "150",
    "182",
    "127",
    "219",
    "299",
    "277",
    "309",
    "576",
]


def test_one():
    """Test Part One"""
    assert one(EXAMPLE, 5) == 127


def test_two():
    """Test Part Two"""
    assert two(EXAMPLE, 5) == 62


def is_sum_of(possible_candidates, number):
    for i, x in enumerate(possible_candidates):
        for y in possible_candidates[i:]:
            if (x + y == number) and (x != y):
                return True

    return False


def one(puzzle: list, preamble_length=25):
    """Part One"""
    puzzle = [int(x) for x in puzzle]
    for i, p in enumerate(puzzle[preamble_length:], preamble_length):
        if not is_sum_of(puzzle[i - preamble_length:i], p):
            return p


def two(puzzle: list, preamble_length=25):
    """Part Two"""
    puzzle = [int(x) for x in puzzle]
    for i, p in enumerate(puzzle[preamble_length:], preamble_length):
        if not is_sum_of(puzzle[i - preamble_length:i], p):
            weakness = p
            break

    _p = 0
    nums = []
    i = 0
    while _p != weakness:
        for p in puzzle[i:]:
            _p += p
            nums.append(p)
            if _p > weakness:
                i += 1
                _p = 0
                nums = []
                break
            elif _p == weakness:
                break

    return min(nums) + max(nums)



if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", two(PUZZLE))
