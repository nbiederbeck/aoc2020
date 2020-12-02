"""Puzzles for Advent of Code 2020."""
import requests
from pathlib import Path

with open(Path("~/.config/advent-of-code/token").expanduser()) as f:
    session = f.read().strip()

url = "http://adventofcode.com/2020/day/{}/input"


def get_puzzle(day: int):

    r = requests.get(url.format(day), cookies={"session": session})
    r.raise_for_status()

    return r.text.split('\n')[:-1]
