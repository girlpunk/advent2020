import itertools

def first(file, end=2020):
    current_turn = 1
    numbers = {}
    last_number = 0

    with open(file) as f:
        for last_number in f.readline().strip().split(","):
            last_number = int(last_number)
            numbers[last_number] = [current_turn]
            current_turn += 1

    while current_turn <= end:
        if last_number in numbers and len(numbers[last_number]) == 2:
            last_number = (numbers[last_number][1] - numbers[last_number][0])
        else:
            last_number = 0

        if last_number in numbers:
            if len(numbers[last_number]) == 2:
                del numbers[last_number][0]
            numbers[last_number].append(current_turn)
        else:
            numbers[last_number] = [current_turn]
        current_turn += 1

    return last_number


def second(file):
    return first(file, 30000000)


def main(file="input.txt"):
    return first(file), second(file)


if __name__ == '__main__':
    one, two = main()
    assert one == 1325
    assert two == 59006
    print(one)
    print(two)
