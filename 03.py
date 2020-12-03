"""Thursday, 3. Dec"""
from puzzles import get_puzzle

puzzle = get_puzzle(3)


def test():
    example = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]

    assert one(example) == 7
    assert two(example) == 336


def one(puzzle: list, right=3, down=1):
    n_trees = 0

    i = 0
    for line in puzzle[::down]:
        if line[i] == "#":
            n_trees += 1
        i = (i + right) % len(line)

    return n_trees


def two(puzzle: list):
    right = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]

    m = 1
    for r, d in zip(right, down):
        m *= one(puzzle, r, d)

    return m


if __name__ == "__main__":
    test()
    print(one(puzzle))
    print(two(puzzle))
