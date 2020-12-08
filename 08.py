"""Tue,  8 Dec"""
from puzzles import get_puzzle

puzzle = get_puzzle(8)


def test():
    """Test"""
    example = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]

    assert one(example) == 5

    assert two(example) == 8


def boot(puzzle):
    acc = 0

    n_instructions = len(puzzle)
    instructions_executed = set()

    i = 0

    terminated = False
    while True:
        if i in instructions_executed:
            break

        if i == n_instructions:
            terminated = True
            break

        instructions_executed.add(i)

        op, arg = puzzle[i].split()
        arg = int(arg)

        if op == "nop":
            i += 1
        elif op == "acc":
            i += 1
            acc += arg
        elif op == "jmp":
            i += arg

    return acc, terminated


def one(puzzle: list):
    """Part One"""
    acc, term = boot(puzzle)
    return acc


def two(puzzle: list):
    """Part Two"""
    for i, instruction in enumerate(puzzle):
        p = puzzle.copy()
        nop = "nop"
        jmp = "jmp"
        if nop in instruction:
            p[i] = instruction.replace(nop, jmp)
        elif jmp in instruction:
            p[i] = instruction.replace(jmp, nop)
        else:
            continue

        acc, term = boot(p)

        if term:
            break

    return acc


if __name__ == "__main__":
    test()
    print("1:", one(puzzle))
    print("2:", two(puzzle))
