import re
from collections.abc import Iterator
from importlib.resources import files
from typing import Optional


def part1(text: str) -> int:
    sum = 0
    for line in text.splitlines():
        nums_gen = numbers(line)
        first = last = next(nums_gen)
        for n in numbers(line):
            last = n
        sum += first * 10 + last

    return sum


def is_ascii_decimal(c: str):
    return c.isdecimal() and "0" <= c <= "9"


def numbers(line: str) -> Iterator[int]:
    for c in line:
        if is_ascii_decimal():
            yield int(c)


def part2(text: str) -> int:
    sum = 0
    match_group = "[0-9]|one|two|three|four|five|six|seven|eight|nine"
    prog = re.compile(f"({match_group}).*({match_group})")
    fallback_prog = re.compile(f"({match_group})")

    for line in text.splitlines():
        matches = prog.search(line)
        if not matches:
            matches = fallback_prog.search(line)
        if not matches:
            continue

        groups = matches.groups()
        if len(groups) == 2:
            (first, last) = groups
        else:
            first = last = groups[0]
        sum += to_number(first) * 10 + to_number(last)
    return sum


def to_number(string: str) -> Optional[int]:
    if string.isdecimal():
        return int(string)
    match string:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return None


if __name__ == "__main__":
    text = files(__package__).joinpath("input.txt").read_text()
    res = part2(text)
    print(res)
