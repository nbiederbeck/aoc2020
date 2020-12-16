"""Wed, 16 Dec"""
from puzzles import get_puzzle

PUZZLE = get_puzzle(16)
EXAMPLE = [
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50",
    "",
    "your ticket:",
    "7,1,14",
    "",
    "nearby tickets:",
    "7,3,47",
    "40,4,50",
    "55,2,20",
    "38,6,12",
]

EXAMPLE_TWO = [
    "class: 0-1 or 4-19",
    "row: 0-5 or 8-19",
    "seat: 0-13 or 16-19",
    "",
    "your ticket:",
    "11,12,13",
    "",
    "nearby tickets:",
    "3,9,18",
    "15,1,5",
    "5,14,9",
]


def test_one():
    """Test Part One"""
    assert one(EXAMPLE) == 71


def test_two():
    """Test Part Two"""
    assert two(EXAMPLE_TWO) == {'class': 12, 'row': 11, 'seat': 13}


def rules_tickets(puzzle):
    first_empty_line_idx = puzzle.index("")
    rules = puzzle[:first_empty_line_idx]

    ticket = puzzle[first_empty_line_idx + 2]
    nearby_tickets = puzzle[first_empty_line_idx + 5:]

    return rules, ticket, nearby_tickets

def valid_numbers_per_rule(rules):
    nums = dict()

    for rule in rules:
        name, numbers = rule.split(':')

        if name not in nums:
            nums[name] = set()

        lower, upper = numbers.split(' or ')

        llower, ulower = map(int, lower.split('-'))
        for i in range(llower, ulower + 1):
            nums[name].add(i)

        lupper, uupper = map(int, upper.split('-'))
        for i in range(lupper, uupper + 1):
            nums[name].add(i)

    return nums


def valid_numbers(val):
    nums = set()
    for num in val.values():
        for n in num:
            nums.add(n)

    return nums


def one(puzzle: list):
    """Part One"""
    rules, _, nearby_tickets = rules_tickets(puzzle)

    nums = valid_numbers(valid_numbers_per_rule(rules))

    ticket_scanning_error_rate = 0

    for ticket in nearby_tickets:
        for n in map(int, ticket.split(',')):
            if n not in nums:
                ticket_scanning_error_rate += n

    return ticket_scanning_error_rate


def two(puzzle: list):
    """Part Two"""
    rules, your_ticket, nearby_tickets = rules_tickets(puzzle)

    num_rule = valid_numbers_per_rule(rules)
    nums = valid_numbers(num_rule)
    valid_tickets = []

    for ticket in nearby_tickets:
        valid = True
        for n in map(int, ticket.split(',')):
            if n not in nums:
                valid = False
        if valid:
            valid_tickets.append(ticket)

    valid_tickets.append(your_ticket)

    fields = dict()
    for ticket in valid_tickets:
        for field_id, number in enumerate(map(int, ticket.split(','))):
            if field_id not in fields:
                fields[field_id] = []
            fields[field_id].append(number)

    id_to_name = dict()

    for fid, fvalues in fields.items():
        for rname, rvalues in num_rule.items():
            if len(set(fvalues) & rvalues) == len(set(fvalues)):
                if rname not in id_to_name:
                    id_to_name[rname] = fid

    my_ticket = dict()
    for name, values in zip(id_to_name, fields.values()):
        my_ticket[name] = values[-1]

    return my_ticket


def part_two(puzzle):
    my_ticket = two(puzzle)

    answer = 1
    for name, value in my_ticket.items():
        if name.startswith('departure'):
            answer *= value

    return answer


if __name__ == "__main__":
    test_one()
    print("1:", one(PUZZLE))
    test_two()
    print("2:", part_two(PUZZLE))
