def load_instructions(file):
    return [[instruction.split(" ")[0].strip(), int(instruction.split(" ")[1].strip())] for instruction in [line.strip() for line in open(file)]]


def first(instructions):
    return iterate(instructions)[1]

def iterate(instructions, toSwap=None):
    acc = 0
    step = 0
    visited_steps = set()

    while True:
        if step in visited_steps:
            return False, acc
        visited_steps.add(step)
        try:
            line = instructions[step]
        except IndexError:
            return True, acc
        instruction = line[0]
        if step == toSwap:
            if instruction == "jmp":
                instruction = "nop"
            else:
                instruction = "jmp"
        if instruction == "acc":
            acc += line[1]
            step += 1
        elif instruction == "jmp":
            step += line[1]
        elif instruction == "nop":
            step += 1
        else:
            print("UNKNOWN INSTRUCTION!")



def second(instructions):
    for lineNumber in range(0, len(instructions)):
        if instructions[lineNumber][0] == "acc":
            continue
        result, acc = iterate(instructions, lineNumber)
        if result:
            return acc



def main(file="input.txt"):
    answers = load_instructions(file)
    return first(answers), second(answers)


if __name__ == '__main__':
    one, two = main()
    assert one == 1766
    assert two == 1639
    print(one)
    print(two)
