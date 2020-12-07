#!/bin/bash
date=$(date +'%A, %_d %b')
day=$(date +'%d')
echo "'''${date}'''
from puzzles import get_puzzle

puzzle = get_puzzle(${day})


def test():
    '''Test'''
    assert False


def one(puzzle: list):
    '''Part One'''
    return None


def two(puzzle: list):
    '''Part Two'''
    return None


if __name__ == '__main__':
    test()
    print(one(puzzle))
    print(two(puzzle))
" | tee "${day}".py
