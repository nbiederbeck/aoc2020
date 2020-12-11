"""Fri, 11 Dec"""
from puzzles import get_puzzle
from copy import deepcopy

PUZZLE = get_puzzle(11)
EXAMPLE = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL",
]

empty = "L"
occupied = "#"
space = "."


def test_one():
    """Test Part One"""
    assert one(EXAMPLE) == 37


def test_two():
    """Test Part Two"""
    assert two(EXAMPLE) == 26


def to_nested_list(floor: list) -> list:
    new = []
    for row in floor:
        new_row = []
        for c in row:
            new_row.append(c)
        new.append(new_row)

    return new


def get_direct_neighbors(seat: tuple, floorplan: list) -> str:
    """Return a string with seats, starting at the top going clockwise.

    Example: '  .LL   ' (upper left)

    """
    n = [" "] * 8

    rows = len(floorplan) - 1
    cols = len(floorplan[0]) - 1

    r, c = seat

    if r > 0:
        n[0] = floorplan[r - 1][c]
        if c > 0:
            n[7] = floorplan[r - 1][c - 1]
        if c < cols:
            n[1] = floorplan[r - 1][c + 1]

    if r < rows:
        n[4] = floorplan[r + 1][c]
        if c > 0:
            n[5] = floorplan[r + 1][c - 1]
        if c < cols:
            n[3] = floorplan[r + 1][c + 1]

    if c > 0:
        n[6] = floorplan[r][c - 1]
    if c < cols:
        n[2] = floorplan[r][c + 1]

    return "".join(n)


def in_bounds(r, c, floor):
    if r < 0:
        return False
    if c < 0:
        return False
    if r >= len(floor):
        return False
    if c >= len(floor[0]):
        return False

    return True


def get_neighbors(seat: tuple, floor: list) -> str:
    """Return a string with seats, starting at the top going clockwise.

    Example: '  .LL   ' (upper left)

    """

    n = [' '] * 8

    # above
    r, c = seat
    while True:
        r -= 1
        if in_bounds(r, c, floor):
            s = floor[r][c]
            if s != space:
                n[0] = s
                break
        else:
            break

    # above right
    r, c = seat
    while True:
        r -= 1
        c += 1
        if in_bounds(r, c, floor):
            s = floor[r][c]
            if s != space:
                n[1] = s
                break
        else:
            break

    # right
    r, c = seat
    while True:
        c += 1
        if in_bounds(r, c, floor):
            s = floor[r][c]
            if s != space:
                n[2] = s
                break
        else:
            break

    # below right
    r, c = seat
    while True:
        r += 1
        c += 1
        if in_bounds(r, c, floor):
            s = floor[r][c]
            if s != space:
                n[3] = s
                break
        else:
            break

    # below
    r, c = seat
    while True:
        r += 1
        if in_bounds(r, c, floor):
            s = floor[r][c]
            if s != space:
                n[4] = s
                break
        else:
            break

    # below left
    r, c = seat
    while True:
        r += 1
        c -= 1
        if in_bounds(r, c, floor):
            s = floor[r][c]
            if s != space:
                n[5] = s
                break
        else:
            break

    # left
    r, c = seat
    while True:
        c -= 1
        if in_bounds(r, c, floor):
            s = floor[r][c]
            if s != space:
                n[6] = s
                break
        else:
            break

    # above left
    r, c = seat
    while True:
        r -= 1
        c -= 1
        if in_bounds(r, c, floor):
            s = floor[r][c]
            if s != space:
                n[7] = s
                break
        else:
            break

    return "".join(n)


def print_floor(floor):
    print('=====')
    for row in floor:
        print("".join(row))


def count_occupied_seats(floor):
    n_occ = 0
    for row in floor:
        for seat in row:
            if seat == occupied:
                n_occ += 1

    return n_occ


def one(puzzle: list):
    """Part One"""

    floor = to_nested_list(puzzle)

    stable = False
    while not stable:
        new = deepcopy(floor)
        for r, row in enumerate(floor):
            for s, seat in enumerate(row):
                neighbors = get_direct_neighbors((r, s), floor)
                if seat == empty:
                    if occupied not in neighbors:
                        new[r][s] = occupied
                elif seat == occupied:
                    if neighbors.count(occupied) >= 4:
                        new[r][s] = empty

        if new == floor:
            stable = True
        else:
            floor = new

    return count_occupied_seats(floor)


def two(puzzle: list):
    """Part Two"""
    floor = to_nested_list(puzzle)

    stable = False
    while not stable:
        new = deepcopy(floor)
        for r, row in enumerate(floor):
            for s, seat in enumerate(row):
                neighbors = get_neighbors((r, s), floor)
                if seat == empty:
                    if occupied not in neighbors:
                        new[r][s] = occupied
                elif seat == occupied:
                    if neighbors.count(occupied) >= 5:
                        new[r][s] = empty

        if new == floor:
            stable = True
        else:
            floor = new

    return count_occupied_seats(floor)


if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", two(PUZZLE))
