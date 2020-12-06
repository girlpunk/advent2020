def load_answers(file):
    return [line.strip() for line in open(file).read().split("\n\n")]


def first(answers):
    total = 0

    for group in answers:
        group_answers = set(group)
        if "\n" in group_answers:
            group_answers.remove("\n")
        total += len(group_answers)

    return total


def second(answers):
    total = 0

    for group in answers:
        people = group.split("\n")
        total += sum([all([answer in person for person in people]) for answer in people[0]])

    return total



def main(file="input.txt"):
    answers = load_answers(file)
    return first(answers), second(answers)



def test_jm_6(benchmark):
    one, two = benchmark(main, file="6/input.txt")
    assert one == 6273
    assert two == 3254


if __name__ == '__main__':
    one, two = main()
    assert one == 6273
    assert two == 3254
    print(one)
    print(two)
