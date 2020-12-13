"""So, 13 Dez"""
from puzzles import get_puzzle

PUZZLE = get_puzzle(13)
EXAMPLE = [
    "939",
    "7,13,x,x,59,x,31,19",
]


def test_one():
    """Test Part One"""
    assert one(EXAMPLE) == 295


def test_two():
    """Test Part Two"""
    assert two(EXAMPLE) == 1068781
    assert two(["", "17,x,13,19"]) == 3417
    assert two(["", "67,7,59,61"]) == 754018
    assert two(["", "67,x,7,59,61"]) == 779210
    assert two(["", "67,7,x,59,61"]) == 1261476
    assert two(["", "1789,37,47,1889"]) == 1202161486


def one(puzzle: list):
    """Part One"""
    earliest_timestamp = int(puzzle[0])
    bus_ids = [int(b) for b in puzzle[1].split(",") if b != "x"]

    waiting_times = []

    for bus_id in bus_ids:
        prod = earliest_timestamp // bus_id
        waiting_time = ((prod + 1) * bus_id) - earliest_timestamp
        waiting_times.append(waiting_time)

    waiting_time = min(waiting_times)
    idx = waiting_times.index(waiting_time)
    bus_id = bus_ids[idx]

    return bus_id * waiting_time


def two(puzzle: list):
    """Part Two"""
    bus_ids = puzzle[1].split(",")

    multiples = dict()

    for idx, bus_id in enumerate(bus_ids):
        if bus_id == "x":
            continue
        bus_id = int(bus_id)
        multiples[bus_id] = set(i * bus_id for i in range(1000))

    return NotImplemented


if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", two(PUZZLE))
