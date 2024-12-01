def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    
    midpoint = len(array) // 2
    left_half = array[:midpoint]
    right_half = array[midpoint:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left: list, right: list) -> list:
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])

    return merged_list

with open('Day 1/sampleData.txt', 'r') as file:
    lines = file.readlines()
    
values = []
left = []
right = []
total = 0

for line in lines:
    values.append(line.strip().split(" "))

for numbers in values:
    left.append(int(numbers[0]))
    right.append(int(numbers[3]))

left = merge_sort(left)
right = merge_sort(right)

for i in range(len(left)):
    total = total + abs(int(left[i]) - int(right[i]))

print(total)

similarities = 0

for val in range(len(left)):
    count = 0
    for values in range(len(right)):
        if left[val] == right[values]:
            count += 1
    if count == 0:
        pass
    else:
        similarities = similarities + (left[val] * count)

print(similarities)