
Tree = '#'


def first(across=3, down=1):
    file = [line.strip() for line in open("input.txt")]

    current_across = 0
    current_down = 0
    trees = 0

    while True:
        current_across += across
        current_down += down

        if current_across + 1 > len(file[0]):
            current_across -= len(file[0])

        if current_down + 1 > len(file):
            break

        if file[current_down][current_across] == Tree:
            trees += 1

    return trees


def second():
    one   = first(1, 1)
    two   = first(3, 1)
    three = first(5, 1)
    four  = first(7, 1)
    five  = first(1, 2)

    return one * two * three * four * five


if __name__ == '__main__':
    print(first())
    print(second())
