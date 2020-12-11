"""Mon,  7 Dec"""
from puzzles import get_puzzle
from pprint import pprint

PUZZLE = get_puzzle(7)

EXAMPLE = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]


def test_one():
    """Test Part One"""
    assert one(EXAMPLE) == 4


def test_two():
    """Test Part One"""
    assert two(EXAMPLE) == False



def one(puzzle: list, my_bag='shiny gold'):
    """Part One"""

    all_colors = set()

    # bags is a dictionary-version of the puzzle
    bags = dict()

    for rule in puzzle:
        containing, contains = rule.split('bags contain')

        ccol = containing.strip()
        all_colors.add(ccol)
        bags[ccol] = []

        if 'no other bags' in contains:
            pass
        elif ',' not in contains:
            _, attr, col, _ = contains.strip().split()
            color = f"{attr} {col}"
            bags[ccol].append(color)
            all_colors.add(color)
        else:
            contains = contains.split(',')
            for cont in contains:
                _, attr, col, _ = cont.strip().split()
                color = f"{attr} {col}"
                bags[ccol].append(color)
                all_colors.add(color)

    # contained_in is the reverse of the puzzle
    contained_in = {color: [] for color in all_colors}

    for bag, _in in contained_in.items():
        for _bag, _con in bags.items():
            if bag in _con:
                _in.append(_bag)

    print("read as key is in value")
    pprint(contained_in)
    print(find_toplevel_bag(contained_in, 'shiny gold'))


def find_toplevel_bag(bags, color):
    for c in bags[color]:
        return find_toplevel_bag(bags, c)
    return color



def two(puzzle: list):
    """Part Two"""
    return NotImplemented


if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", two(PUZZLE))
