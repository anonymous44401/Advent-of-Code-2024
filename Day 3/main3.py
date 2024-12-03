def read_file():
    with open('Day 3/sampleData3.txt', 'r') as file:
        lines = file.readlines()

    return lines

def mul(x):
    try:
        x = x.split(",")

        num1 = int(x[0])
        num2 = int(x[1])

        ans = num1 * num2
    except:
        ans = 0

    return ans

def part_one():
    total = 0
    lines = read_file()
    
    split_lines = [line.split("mul(") for line in lines]

    for line in range(len(split_lines)):
        for i in range(len(split_lines[line])):
            split_lines[line][i] = (split_lines[line][i].split(")"))[0]
            total += mul(split_lines[line][i])

    print(total)

def part_two():
    total = 0
    cont = True
    lines = read_file()
    
    split_lines = [line.split("mul(") for line in lines]

    for line in range(len(split_lines)):
        for i in range(len(split_lines[line])):
            split_lines[line][i] = (split_lines[line][i].split(")"))
            for j in range(len(split_lines[line][i])):
                if "do(" in split_lines[line][i][j]:
                    cont = True
                
                elif "don't(" in split_lines[line][i][j]:
                    cont = False

                else:
                    if cont == True:
                        total += mul(split_lines[line][i][j])

    print(total)

part_one()
part_two()