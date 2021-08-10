import numpy


def first(file):
    z_size = 6+6
    x_size = 8+6+6
    y_size = 8+6+6
    pocket = numpy.full([z_size, x_size, y_size], False)
    line_num = 5
    for line in open(file):
        char_num = 5
        for char in line:
            pocket[5, line_num, char_num] = char == "#"
            char_num += 1
        line_num += 1

    for i in range(0, 6):
        newPocket = pocket.copy()
        for z in range(0, z_size):
            for x in range(0, x_size):
                for y in range(0, y_size):
                    surrounding = pocket[min(z-1, 0):3, min(x-1, 0):3, min(y-1, 0):3]
                    if pocket[z, x, y] and (sum(sum(sum(surrounding))) == 3 or sum(sum(sum(surrounding))) == 4):
                        newPocket[z, x, y] = False
                    elif (not pocket[z, x, y]) and (sum(sum(sum(surrounding))) == 3):
                        newPocket[z, x, y] = True
        pocket = newPocket

    return sum(pocket is True)

def second(file):
    return -1


def main(file="input.txt"):
    return first(file), second(file)


if __name__ == '__main__':
    one, two = main()
    assert one == 23115
    assert two == 239727793813
    print(one)
    print(two)
