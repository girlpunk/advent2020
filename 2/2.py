from typing import Callable

def decode_lines(file, callback: Callable[[str, str, int, int], bool]) -> int:
    input = open(file)
    output = 0

    for line in input:
        line = line.strip()

        if line == "":
            continue

        regex, password = line.split(":")
        count, character = regex.split(" ")
        min_count, max_count = count.split("-")

        min_count: int = int(min_count)
        max_count: int = int(max_count)

        output += callback(password.strip(), character.strip(), min_count, max_count)

    return output


def first(file):
    """
    Password contains between min and max (inclusive) instances of character
    """
    return decode_lines(
        file,
        lambda password, character, min_count, max_count:
            min_count <= password.strip().count(character.strip()) <= max_count)


def second(file):
    """
    min and max represent 1-indexed positions that must be match the character
    """
    return decode_lines(
        file,
        lambda password, character, min_count, max_count:
            (password[min_count - 1] == character and password[max_count - 1] != character)
            or
            (password[min_count - 1] != character and password[max_count - 1] == character)
    )


def main(file="input.txt"):
    return first(file), second(file)


def test_jm_2(benchmark):
    one, two = benchmark(main, file="2/input.txt")
    assert one == 422
    assert two == 451


if __name__ == '__main__':
    one = first("input.txt")
    two = second("input.txt")
    assert one == 422
    assert two == 451
    print(one)
    print(two)
