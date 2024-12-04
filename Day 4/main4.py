def read_file():
    with open('Day 4/sampleData4.txt', 'r') as file:
        lines = file.readlines()

    return lines

def part_one():
    total = 0
    lines = read_file()
    for line in lines:
        total += check_horizontal(line)
        # print(total)

    for x in range(len(lines) - 3):
        total += check_vertical(lines[x], lines[x+1], lines[x+2], lines[x+3])

        total += check_diagonal(lines[x], lines[x+1], lines[x+2], lines[x+3])

        # print(lines[x], lines[x+1], lines[x+2], lines[x+3])

    print(total)

def check_horizontal(line):
    total = 0
    for i in range(len(line) - 3):
        word = line[i] + line[i+1] + line[i+2] + line[i+3]
        if word == "XMAS" or word == "SAMX":
            total += 1
    
    return total

def check_vertical(line1, line2, line3, line4):
    total = 0
    for i in range(len(line1)):
        if line1[i] == "X" and line2[i] == "M" and line3[i] == "A" and line4[i] == "S":
            total += 1

        elif line1[i] == "S" and line2[i] == "A" and line3[i] == "M" and line4[i] == "X":
            total += 1

    return total

def check_diagonal(line1, line2, line3, line4):
    total = 0
    for i in range(len(line1) - 3):
        if line1[i] == "X" and line2[i+1] == "M" and line3[i+2] == "A" and line4[i+3] == "S":
            total += 1
        
        elif line1[i] == "S" and line2[i+1] == "A" and line3[i+2] == "M" and line4[i+3] == "X":
            total += 1

        if line4[i] == "X" and line3[i+1] == "M" and line2[i+2] == "A" and line1[i+3] == "S":
            total += 1

        elif line4[i] == "S" and line3[i+1] == "A" and line2[i+2] == "M" and line1[i+3] == "X":
            total += 1

    return total
    
def part_two():
    total = 0
    lines = read_file()

    for x in range(len(lines) - 2):
        total += check_diagonal_2(lines[x], lines[x+1], lines[x+2])

    print(total)

def check_diagonal_2(line1, line2, line3):
    total = 0
    for i in range(len(line1) - 3):
        diag1 = line1[i] + line2[i+1] + line3[i+2]
        diag2 = line1[i+2] + line2[i+1] + line3[i]
        if diag1 == "MAS" and diag2 == "MAS":
            total += 1
        elif diag1 == "SAM" and diag2 == "SAM":
            total += 1
        elif diag1 == "MAS" and diag2 == "SAM":
            total += 1
        elif diag1 == "SAM" and diag2 == "MAS":
            total += 1

    return total

part_one()
part_two()