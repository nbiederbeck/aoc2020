#!/bin/bash
date=$(date +'%a, %e %b')
day=$(date +'%e')
file="$(date +'%d').py"


template="\"\"\"${date}\"\"\"
from puzzles import get_puzzle

PUZZLE = get_puzzle(${day##* })
EXAMPLE = [
]


def test_one():
    \"\"\"Test Part One\"\"\"
    assert one(EXAMPLE) == False


def test_two():
    \"\"\"Test Part Two\"\"\"
    assert two(EXAMPLE) == False


def one(puzzle: list):
    \"\"\"Part One\"\"\"
    return NotImplemented


def two(puzzle: list):
    \"\"\"Part Two\"\"\"
    return NotImplemented


if __name__ == \"__main__\":
    test_one()
    print(\"1:\", one(PUZZLE))
    test_two()
    print(\"2:\", two(PUZZLE))"

if ! [[ -e "${file}" ]]; then
    echo "${template}" > "${file}"
else
    echo "${file} exists."
fi
