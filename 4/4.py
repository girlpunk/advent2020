import re


def first(file):
    return len([
        part for part in [
            {k: v for k, v in [
                part.split(":") for part in passport.split()]
             } for passport in [
                line.strip() for line in open(file).read().split("\n\n")
            ]
        ] if ("byr" in part) & ("iyr" in part) & ("eyr" in part) & ("hgt" in part) & ("hcl" in part) & ("ecl" in part) & ("pid" in part)])


def second(file):
    all_passports = [line.strip() for line in open(file).read().split("\n\n")]

    passports_with_parts = []

    for passport in all_passports:
        passports_with_parts.append({k: v for k, v in [part.split(":") for part in passport.split()]})

    passports_with_parts = [part for part in passports_with_parts if
                            ("byr" in part) & ("iyr" in part) & ("eyr" in part) & ("hgt" in part) & ("hcl" in part) & ("ecl" in part) & (
                                    "pid" in part)]

    valid_passports = 0

    for passport in passports_with_parts:
        valid_passports += (1920 <= int(passport["byr"]) <= 2002) and \
                           (2010 <= int(passport["iyr"]) <= 2020) and \
                           (2020 <= int(passport["eyr"]) <= 2030) and \
                           ((("cm" in passport["hgt"]) and (len(passport["hgt"]) == 5) and (150 <= int(passport["hgt"][0:3]) <= 193)) or
                            (("in" in passport["hgt"]) and (len(passport["hgt"]) == 4) and (59 <= int(passport["hgt"][0:2]) <= 76))) and \
                           (passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and \
                           (re.fullmatch("#[0-9a-f]{6}", passport["hcl"]) is not None) and \
                           (len(passport["pid"]) == 9)

    return valid_passports

def main(file="input.txt"):
    return first(file), second(file)

def test_jm_4(benchmark):
    one, two = benchmark(main, file="4/input.txt")
    assert one == 202
    assert two == 137

if __name__ == '__main__':
    one, two = main()
    assert one == 202
    assert two == 137
    print(one)
    print(two)

