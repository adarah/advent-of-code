from importlib.resources import files


def part1(text: str) -> int:
    sum = 0
    for line in text.splitlines():
        nums_gen = numbers(line)
        first = last = next(nums_gen)
        for n in numbers(line):
            last = n
        sum += first * 10 + last

    return sum


def numbers(line: str) -> int:
    for c in line:
        if c.isdecimal() and "0" <= c <= "9":
            yield int(c)


if __name__ == "__main__":
    text = files(__package__).joinpath("input.txt").read_text()
    part1()
