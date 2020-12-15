def load_rules(file):
    rules = {}

    for rule in [line.strip() for line in open(file)]:
        rule_parts = rule.split("contain")
        container = rule_parts[0].replace("bags", "").replace("bag", "").strip()
        rules[container] = []
        if rule_parts[1] != " no other bags.":
            for bag in rule_parts[1].split(","):
                rule = bag.replace("bags", "").replace(".", "").replace("bag", "").strip().split(" ", 1)
                rule[0] = int(rule[0])
                rules[container].append(rule)

    return rules

toFind = "shiny gold"

def checkFirst(rules, toCheck):
    if toFind in [c[1] for c in rules[toCheck]]:
        return True
    return any([checkFirst(rules, subCheck[1]) for subCheck in rules[toCheck]])

def first(rules):
    return sum([checkFirst(rules, toCheck) for toCheck in rules])


def checkSecond(rules, toCheck):
    total = 0
    for bag in rules[toCheck]:
        total += bag[0] + (bag[0] * checkSecond(rules, bag[1]))
    return total

def second(rules):
    return checkSecond(rules, toFind)



def main(file="input.txt"):
    answers = load_rules(file)
    return first(answers), second(answers)


if __name__ == '__main__':
    one, two = main()
    assert one == 248
    assert two == 57281
    print(one)
    print(two)
