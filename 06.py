"""Sun,  6 Dec"""
from puzzles import get_puzzle

puzzle = get_puzzle(6)


def test():
    example = [
        "abc",
        "",
        "a",
        "b",
        "c",
        "",
        "ab",
        "ac",
        "",
        "a",
        "a",
        "a",
        "a",
        "",
        "b",
    ]

    assert one(example) == 11

    assert len(get_groups(example)) == 5
    assert two(example) == 6


def get_groups(puzzle: list) -> dict:
    groups = dict()
    grp_idx = 0
    for line in puzzle:
        if line != "":
            if grp_idx not in groups:
                groups[grp_idx] = [line]
            else:
                groups[grp_idx].append(line)
        else:
            grp_idx += 1

    return groups


def count_anyone(group: list) -> int:
    answers = "".join(group)
    n = len(set(answers))
    return n


def one(puzzle: list):
    n = 0
    groups = get_groups(puzzle)
    for group in groups.values():
        n += count_anyone(group)

    return n


def count_everyone(group: list):
    n_persons = len(group)
    answers = dict()
    for char in "".join(group):
        if char not in answers:
            answers[char] = 1
        else:
            answers[char] += 1

    n_answers = 0
    for n_have_answered in answers.values():
        if n_have_answered == n_persons:
            n_answers += 1

    return n_answers


def two(puzzle: list):
    groups = get_groups(puzzle)
    n = 0
    for group in groups.values():
        n += count_everyone(group)

    return n


if __name__ == "__main__":
    test()
    print(one(puzzle))
    print(two(puzzle))
