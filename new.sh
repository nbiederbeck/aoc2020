#!/bin/bash
date=$(date +'%a, %e %b')
day=$(date +'%e')
file="$(date +'%d').py"


template="\"\"\"${date}\"\"\"
from puzzles import get_puzzle

puzzle = get_puzzle(${day##* })
example = [
]


def test_one():
    \"\"\"Test Part One\"\"\"
    assert one(example) == False


def test_two():
    \"\"\"Test Part Two\"\"\"
    assert two(example) == False


def one(puzzle: list):
    \"\"\"Part One\"\"\"
    return NotImplemented


def two(puzzle: list):
    \"\"\"Part Two\"\"\"
    return NotImplemented


if __name__ == \"__main__\":
    test_one()
    print(\"1:\", one(puzzle))
    test_two()
    print(\"2:\", two(puzzle))"

if ! [[ -e "${file}" ]]; then
    echo "${template}" > "${file}"
else
    echo "${file} exists."
fi
