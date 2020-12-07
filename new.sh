#!/bin/bash
date=$(date +'%a, %e %b')
day=$(date +'%e')
file="$(date +'%d').py"


template="\"\"\"${date}\"\"\"
from puzzles import get_puzzle

puzzle = get_puzzle(${day##* })


def test():
    \"\"\"Test\"\"\"
    assert False


def one(puzzle: list):
    \"\"\"Part One\"\"\"
    return None


def two(puzzle: list):
    \"\"\"Part Two\"\"\"
    return None


if __name__ == \"__main__\":
    test()
    print(one(puzzle))
    print(two(puzzle))"

echo "${template}"| tee "${file}"
