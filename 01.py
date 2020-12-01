"""Tuesday, 1 Dec"""
from puzzles import puzzles

puzzle = puzzles[1]


def test_solution():
    example = [1721, 979, 366, 299, 675, 1456]

    assert one(example) == 514579
    assert two(example) == 241861950


def one(puzzle: list):
    puzzle = sorted(puzzle)
    for i, a in enumerate(puzzle):
        for b in puzzle[i:]:
            if a + b == 2020:
                return a * b


def two(puzzle: list):
    puzzle = sorted(puzzle)
    for i, a in enumerate(puzzle):
        for j, b in enumerate(puzzle, i):
            for c in puzzle[j:]:
                if a + b + c == 2020:
                    return a * b * c


if __name__ == "__main__":
    test_solution()
    print(one(puzzle))
    print(two(puzzle))
