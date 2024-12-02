def check_line(line):
    #print("ine ", line)
    increased = False
    incremented = []
    for pos in range(0, (len(line)-1)):
        diff = line[pos] - line[pos+1]
        
        if abs(diff) in [1, 2, 3]:
            if diff > 0:
                increased = False

            else: 
                increased = True

            incremented.append(increased)

        else:
            safe = False
            return safe
    #print(incremented)
    if True in incremented and False in incremented:
        safe = False
    else:
        safe =  True
    
    return safe

def read_file():
    with open('Day 2/sampleData2.txt', 'r') as file:
        lines = file.readlines()

    return lines

def part_1():
    lines = read_file()

    safe_val = 0

    for line in range(len(lines)):
        lines[line] = (lines[line].split(" "))
        
        for i in range(len(lines[line])):
            lines[line][i] = int((lines[line][i])[:2])
        #print(lines[line])
        #print(line)

        if check_line(lines[line]) == True:
            safe_val += 1

    print(safe_val)

def part_2():
    lines = read_file()
    
    safe_val = 0

    for line in range(len(lines)):
        lines[line] = (lines[line].split(" "))
        
        for i in range(len(lines[line])):
            lines[line][i] = int((lines[line][i])[:2])
            #pass

        # Checks if it's safe anyway
        if check_line(lines[line]) == True:
            safe_val += 1
        
        else:
            # If line isn't safe
            line_hold = []
            bad_levels = []
            for data in range(len(lines[line])):
                line_hold.append(lines[line][data])

            #print("line holder:::", line_hold)

            for j in range(0, len(lines[line])):

                # if it's not safe, check the line again by deleting value 0, then value 1, then value 2 ... until it's safe
                # or the end of the line is reached
                
                #print("line hold ", line_hold)

                lines[line].pop(j)

                bad_levels.append(check_line(lines[line]))

                #print("line compared", lines[line])

                #print("bad levels ", bad_levels)

                #lines[line] = line_hold
                if lines[line] != line_hold:
                    lines[line] = []
                    for val in range(len(line_hold)):
                        lines[line].append(line_hold[val])
                

                #print("line ", lines[line])

            if True in bad_levels:
                safe_val += 1
                

    print(safe_val)

part_1()
part_2()