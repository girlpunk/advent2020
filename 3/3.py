from functools import reduce

Tree = '#'


def first(across=3, down=1):
    file = [line.strip() for line in open("input.txt")]

    current_across = across
    current_down = down
    trees = 0

    while current_down + 1 <= len(file):
        if file[current_down][current_across] == Tree:
            trees += 1

        current_across = (current_across + across) % len(file[0])
        current_down += down

    return trees


def second():
    pairs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    results = [first(across, down) for across, down in pairs]
    result = reduce((lambda x, y: x * y), results)

    return result


if __name__ == '__main__':
    print(first())
    print(second())
