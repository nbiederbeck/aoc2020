"""Tue, 15 Dec"""
PUZZLE = [2, 20, 0, 4, 1, 17]
EXAMPLE = [0, 3, 6]


def test_one():
    """Test Part One"""
    assert one(EXAMPLE) == 436
    assert one([1, 3, 2]) == 1
    assert one([2, 1, 3]) == 10
    assert one([1, 2, 3]) == 27
    assert one([2, 3, 1]) == 78
    assert one([3, 2, 1]) == 438
    assert one([3, 1, 2]) == 1836


def test_two():
    """Test Part Two"""
    assert two(EXAMPLE) == 175594
    assert two([1, 3, 2]) == 2578
    assert two([2, 1, 3]) == 3544142
    assert two([1, 2, 3]) == 261214
    assert two([2, 3, 1]) == 6895259
    assert two([3, 2, 1]) == 18
    assert two([3, 1, 2]) == 362


def one(puzzle: list, nth_number=2020):
    """Part One"""
    for turn in range(len(puzzle), nth_number):
        if turn % 1000 == 0:
            print(f'{turn / nth_number:.5f}')
        last_spoken_number = puzzle[-1]
        if last_spoken_number not in puzzle[:-1]:
            next_number = 0
        else:
            p = puzzle[:-1]
            turn_number_was_spoken = len(p) - p[::-1].index(last_spoken_number)
            next_number = turn - turn_number_was_spoken

        puzzle.append(next_number)

    return next_number


def two(puzzle: list):
    """Part Two"""
    return one(puzzle, 30000000)


if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", two(PUZZLE))
