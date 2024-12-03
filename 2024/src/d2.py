from typing import List

def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as text:
        return text.read()

test_input = read_from_file('src/input/d2_test.txt')
real_input = read_from_file('src/input/d2.txt')
input = real_input

def is_safe(levels, direction):
    for i in range(0, len(levels) - 1):
        if direction < 0:
            if levels[i] - levels[i+1] > 3 or levels[i] - levels[i+1] < 1:
                return False
        elif levels[i] - levels[i+1] < -3 or levels[i] - levels[i+1] > -1:
            return False
    return True

input_lines = input.split('\n')
safe_count = 0
for line in input_lines:
    levels = [int(n) for n in line.split()]
    should_be_ascending = levels[0] < levels[-1]
    direction_multiplier = -1
    if should_be_ascending:
        direction_multiplier = 1
    if is_safe(levels, direction_multiplier):
        safe_count += 1
print('part1:', safe_count)

def is_safe_2(levels: List[int]):
    diffs = [levels[i+1] - levels[i] for i in range(len(levels) -1)]
    inc = 0
    dec = 0
    for diff in diffs:
        if diff == 0 or not 1<=abs(diff)<=3:
            return False
        if diff > 0:
            inc += 1
        if diff < 0:
            dec += 1
    
    return not(inc > 0 and dec > 0)

safe_count_2 = 0
for line in input_lines:
    levels = [int(n) for n in line.split()]
    for i in range(len(levels)):
        target = levels[:i] + levels[i+1:]
        if is_safe_2(target):
            safe_count_2 += 1
            break

print('part2:', safe_count_2)