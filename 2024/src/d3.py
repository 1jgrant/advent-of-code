import re
from typing import List

def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as text:
        return text.read()

test_input = read_from_file('src/input/d3_test.txt')
real_input = read_from_file('src/input/d3.txt')
input = real_input

def calculate_total_from_commands(commands: List[str]):
    total = 0
    for command in commands:
        [val1, val2] = re.findall('\d+', command)
        total += int(val1) * int(val2)
    return total

single_line_input = input.replace('\n', '')
p1_matches = re.findall('mul\(\d{1,3},\d{1,3}\)', single_line_input)
total_p1 = calculate_total_from_commands(p1_matches)

print('part1:', total_p1)

p2_matches = re.findall('(?:mul\(\d{1,3},\d{1,3}\)|don\'t|do)', single_line_input)
commands_to_execute = []
is_execute_enabled = True
for match in p2_matches:
    if match == 'don\'t':
        is_execute_enabled = False
        continue
    if match == 'do':
        is_execute_enabled = True
        continue
    if is_execute_enabled:
        commands_to_execute.append(match)

total_p2 = calculate_total_from_commands(commands_to_execute)

print('part2:', total_p2)