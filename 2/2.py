from typing import Callable

def decode_lines(callback: Callable[[str, str, int, int], bool]) -> int:
    input = open("input.txt")
    output = 0

    for line in input.split("\n"):
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


def first():
    """
    Password contains between min and max (inclusive) instances of character
    """
    valid_passwords = decode_lines(
        lambda password, character, min_count, max_count:
            min_count <= password.strip().count(character.strip()) <= max_count)

    print(f"Found {valid_passwords} total valid passwords")


def second():
    """
    min and max represent 1-indexed positions that must be match the character
    """
    valid_passwords = decode_lines(
        lambda password, character, min_count, max_count:
            (password[min_count - 1] == character and password[max_count - 1] != character)
            or
            (password[min_count - 1] != character and password[max_count - 1] == character)
    )
    print(f"Found {valid_passwords} total valid passwords")


if __name__ == '__main__':
    first()
    second()
