"""Puzzles for Advent of Code 2020."""
from pathlib import Path
import requests

url = "http://adventofcode.com/2020/day/{}/input"


def get_puzzle(day: int):
    with open(Path("~/.config/advent-of-code/token").expanduser()) as f:
        session = f.read().strip()

    r = requests.get(url.format(day), cookies={"session": session})
    r.raise_for_status()

    return r.text.split('\n')[:-1]
