"""Sat,  5 Dec"""
from puzzles import get_puzzle

puzzle = get_puzzle(5)


def test():
    examples = [
        "FBFBBFFRLR",
        "BFFFBBFRRR",
        "FFFBBBFRRR",
        "BBFFBBFRLL",
    ]

    r, c = get_row_column(examples[0])
    assert r == 44
    assert c == 5
    assert id_from_seat(r, c) == 357
    assert one(examples) == 820


def id_from_seat(row: int, column: int) -> int:
    return int(row * 8 + column)


def get_row_column(line: str, max_row: int=127, max_col: int=7) -> (int, int):
    min_row = 0
    min_col = 0
    for c in line:
        half_row = (max_row - min_row) // 2
        half_col = (max_col - min_col) // 2

        if c == "F":
            max_row = half_row + min_row
        elif c == "B":
            min_row += half_row + 1

        elif c == "L":
            max_col = half_col + min_col
        elif c == "R":
            min_col += half_col + 1

    return min_row, min_col


def one(puzzle: list) -> int:
    max_id = 0
    for line in puzzle:
        row, column = get_row_column(line)
        seat_id = id_from_seat(row, column)
        if seat_id > max_id:
            max_id = seat_id

    return max_id


def two(puzzle: list) -> int:

    seats = set()

    for line in puzzle:
        r, c = get_row_column(line)
        s = id_from_seat(r, c)
        seats.add(s)

    for possible_seat in range(min(seats), max(seats)):
        if possible_seat not in seats:
            return possible_seat


if __name__ == "__main__":
    test()
    print(one(puzzle))
    print(two(puzzle))
