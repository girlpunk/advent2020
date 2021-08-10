def load_notes(file):
    rules_raw, my_ticket, other_tickets = open(file).read().split("\n\n")
    rules = []
    for rule in rules_raw.split("\n"):
        rule_name, rule_details = rule.split(":")
        rule_name = rule_name.strip()
        rule_details = [[int(num) for num in detail.strip().split("-")] for detail in rule_details.split(" or ")]
        rules.append([rule_name, rule_details])

    my_ticket = [int(num) for num in my_ticket.split("\n")[1].split(",")]
    other_tickets = [[int(num) for num in ticket.split(",")] for ticket in other_tickets.strip().split("\n")[1:]]

    return rules, my_ticket, other_tickets


def first(rules, my_ticket, other_tickets):
    invlid_sum = 0

    for num in my_ticket:
        invalid = True
        for rule in rules:
            if (rule[1][0][0] <= num <= rule[1][0][1]) or (rule[1][1][0] <= num <= rule[1][1][1]):
                invalid = False
                break
        if invalid:
            invlid_sum += num

    for ticket in other_tickets:
        for num in ticket:
            invalid = True
            for rule in rules:
                if (rule[1][0][0] <= num <= rule[1][0][1]) or (rule[1][1][0] <= num <= rule[1][1][1]):
                    invalid = False
                    break
            if invalid:
                invlid_sum += num

    return invlid_sum

def second(rules, my_ticket, other_tickets):
    valid_tickets = []
    for ticket in other_tickets:
        valid = True
        for num in ticket:
            invalid = True
            for rule in rules:
                if (rule[1][0][0] <= num <= rule[1][0][1]) or (rule[1][1][0] <= num <= rule[1][1][1]):
                    invalid = False
                    break
            if invalid:
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    field_possibilities = {}
    ticket_length = len(rules)

    for field in range(0, ticket_length):
        if field not in field_possibilities:
            field_possibilities[field] = rules.copy()
        for rule in rules:
            invalid = False
            for ticket in valid_tickets:
                if (rule[1][0][0] <= ticket[field] <= rule[1][0][1]) or (rule[1][1][0] <= ticket[field] <= rule[1][1][1]):
                    pass
                else:
                    invalid = True
                    break
            if invalid:
                field_possibilities[field].remove(rule)

    while True:
        for field in range(0, ticket_length):
            if len(field_possibilities[field]) == 1:
                # Only one possibility for this field, remove the known one from all others
                for i in range(0, ticket_length):
                    if i == field:
                        continue
                    if field_possibilities[field][0] in field_possibilities[i]:
                        field_possibilities[i].remove(field_possibilities[field][0])
        if all([len(field_possibilities[field]) == 1 for field in field_possibilities]):
            for field in range(0, ticket_length):
                field_possibilities[field] = field_possibilities[field][0]
            break

    departure_fields = []

    for field in field_possibilities:
        if "departure" in field_possibilities[field][0]:
            departure_fields.append(my_ticket[field])

    return departure_fields[0] * departure_fields[1] * departure_fields[2] * departure_fields[3] * departure_fields[4] * departure_fields[5]


def main(file="input.txt"):
    rules, my_ticket, other_tickets = load_notes(file)
    return first(rules, my_ticket, other_tickets), second(rules, my_ticket, other_tickets)


if __name__ == '__main__':
    one, two = main()
    assert one == 23115
    assert two == 239727793813
    print(one)
    print(two)
