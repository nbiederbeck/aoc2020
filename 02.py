"""Wed,  2 Dec"""
from puzzles import get_puzzle

puzzle = get_puzzle(2)


def test():
    example = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]

    assert one(example) == 2

    assert two(example) == 1


def one(puzzle: list):
    valid = 0
    for line in puzzle:
        limits, pattern, password = line.split()
        char = pattern[0]
        lower, upper = map(int, limits.split("-"))
        num = 0
        for c in password:
            if c == char:
                num += 1
        if lower <= num and num <= upper:
            valid += 1

    return valid


def two(puzzle: list):
    valid = 0
    for line in puzzle:
        limits, pattern, password = line.split()
        char = pattern[0]
        lower, upper = map(int, limits.split("-"))
        # zero-index
        lc = password[lower - 1]
        uc = password[upper - 1]

        if (lc == char and uc != char) or (lc != char and uc == char):
            valid += 1

    return valid


if __name__ == "__main__":
    test()
    print(one(puzzle))
    print(two(puzzle))
