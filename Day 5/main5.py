def read_file():
    # with open('Day 5/sampleData5.txt', 'r') as file:
    with open('Day 5/test.txt', 'r') as file:
        lines = file.readlines()

    return lines

def check_line(line: str, rules):
    try:
        line = line.split(",")
    except:
        line = line
    valid = False
    for rule in rules:
        rule_set = rule.split("|")
        first = rule_set[0]
        last = rule_set[1]

        if (first in line) and (last in line): 
            for i in range(0, line.index(last)+1):
                if line[i] == first:
                    valid = True
                    break
                else:
                    valid = False

            if not valid:
                return valid

    return valid

def get_centre(line):
    try:
        line = line.split(",")
    except:
        line = line
    centre = len(line) // 2

    return int(line[centre])

def part_one():
    total = 0
    rules = []
    updates = []
    lines = read_file()


    for line in lines:
        if "|" in line:
            rules.append(line.strip())
        else:
            updates.append(line.strip())

    updates.pop(0)

    for update in updates:
        if check_line(update, rules):
            total += get_centre(update)


    return total
    

# print(part_one())