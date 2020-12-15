import itertools

def first(file):
    zero_mask = 68719476735
    one_mask = 0
    memory = {}

    with open(file) as f:
        for line in f:
            instruction, value = line.strip().split(" = ")
            if instruction == "mask":
                one_mask  = int("0b"+value.replace("X", "0"), 2)
                zero_mask = int("0b"+value.replace("X", "1"), 2)
            elif "mem[" in instruction:
                address = instruction.split("[")[1].strip().strip("]")
                value = int(value)
                value |= one_mask
                value &= zero_mask
                memory[address] = value
            else:
                print("UNKNOWN INSTRUCTION!")

    return sum(memory.values())


def second(file):
    float_mask = 0
    one_mask = 0
    memory = {}

    with open(file) as f:
        for line in f:
            instruction, value = line.strip().split(" = ")
            if instruction == "mask":
                one_mask  = int("0b"+value.replace("X", "0"), 2)
                float_mask = int("0b"+value.replace("1", "0").replace("X", "1"), 2)
            elif "mem[" in instruction:
                address = int(instruction.split("[")[1].strip().strip("]"))
                address |= one_mask
                address |= float_mask
                addresses = set()
                for zeroedBitsCount in range(0, len(set(bits(float_mask)))+1):
                    for maskBits in itertools.combinations(bits(float_mask), zeroedBitsCount):
                        masked_address = address
                        for bit in maskBits:
                            masked_address &= ~bit
                        addresses.add(masked_address)
                for address in addresses:
                    memory[address] = int(value)
            else:
                print("UNKNOWN INSTRUCTION!")

    return sum(memory.values())


def bits(n):
    while n:
        b = n & (~n+1)
        yield b
        n ^= b


def main(file="input.txt"):
    return first(file), second(file)


if __name__ == '__main__':
    one, two = main()
    assert one == 9628746976360
    assert two == 4574598714592
    print(one)
    print(two)
