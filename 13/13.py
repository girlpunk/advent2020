
def first(file):
    with open(file) as f:
        time_now = int(f.readline().strip())
        busses = {int(bus) if bus != "x" else None for bus in f.readline().split(",")}
    busses.remove(None)

    next_busses = [[((time_now // bus) * bus) + bus, bus] for bus in busses]
    bus_can_take = min(next_busses, key=lambda buss_details: buss_details[0])
    return bus_can_take[1] * (bus_can_take[0] - time_now)


def second(file):
    with open(file) as f:
        f.readline()
        raw_busses = [bus for bus in f.readline().split(",")]

    wildcards = 0
    busses = set()

    for bus in raw_busses:
        if bus == "x":
            wildcards += 1
        else:
            busses.add(int(bus))

    time = 100000000000000  # "Surely the actual earliest timestamp will be larger than this"
    stop = False
    while not stop:
        print(f"checking {time}")
        remaining_busses = busses.copy()
        time_increase = -1
        wildcards_remaining = wildcards
        while True:
            time_increase += 1
            next_bus = next((bus for bus in remaining_busses if time+time_increase % bus == 0), None)
            if next_bus is None:
                if wildcards_remaining == 0:
                    break
                wildcards_remaining -= 1
            else:
                remaining_busses.remove(next_bus)
            if len(remaining_busses) == 0:
                return time
        time = min({((time // bus) * bus) + bus for bus in busses})


def main(file="input.txt"):
    return first(file), second(file)


if __name__ == '__main__':
    one, two = main()
    assert one == 1656
    assert two == 56693912375296
    print(one)
    print(two)
