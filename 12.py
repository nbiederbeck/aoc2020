"""Sa, 12 Dez"""
from puzzles import get_puzzle

PUZZLE = get_puzzle(12)
EXAMPLE = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
]


def test_one():
    """Test Part One"""
    assert one(EXAMPLE) == 25


def test_two():
    """Test Part Two"""
    assert two(EXAMPLE) == 286


def manhatten(x, y):
    return abs(x) + abs(y)


rotation = {
    0: "N",
    90: "E",
    180: "S",
    270: "W",
}

rotation_deg = {value: key for key, value in rotation.items()}


def one(puzzle: list):
    """Part One"""
    x = y = 0

    facing = "E"

    for instruction in puzzle:
        action = instruction[0]
        value = int(instruction[1:])

        if action == "R":
            facing = rotation[(rotation_deg[facing] + value) % 360]
        elif action == "L":
            facing = rotation[(rotation_deg[facing] - value) % 360]
        elif action == "F":
            action = facing

        if action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "E":
            x += value
        elif action == "W":
            x -= value

    return manhatten(x, y)


def two(puzzle: list):
    """Part Two"""
    ship = [0, 0]
    waypoint = [10, 1]

    for instruction in puzzle:
        action = instruction[0]
        value = int(instruction[1:])

        if action == "F":
            ship[0] += value * waypoint[0]
            ship[1] += value * waypoint[1]

        elif ((action == "R") and (value == 90)) or ((action == "L") and (value == 270)):
            waypoint = [waypoint[1], -waypoint[0]]
        elif ((action == "L") and (value == 90)) or ((action == "R") and (value == 270)):
            waypoint = [-waypoint[1], waypoint[0]]
        elif (action in ("L", "R")) and (value == 180):
            waypoint = [-waypoint[0], -waypoint[1]]

        if action == "N":
            waypoint[1] += value
        elif action == "S":
            waypoint[1] -= value
        elif action == "E":
            waypoint[0] += value
        elif action == "W":
            waypoint[0] -= value

    return manhatten(*ship)


if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", two(PUZZLE))
