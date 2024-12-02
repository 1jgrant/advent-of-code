import regex as re

test_input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

with open('src/input/day_1.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()

input = actual_input
input_lines = input.split('\n')

count_p1 = 0
for line in input_lines:
    digits = re.findall(r'\d', line)
    num = int(f'{digits[0]}{digits[-1]}')
    count_p1 += num

test_input_2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

input_lines_2 = test_input_2.split('\n')

map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

count_p2 = 0
for line in input_lines:
    digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
    first = digits[0]
    last = digits[-1]
    if len(first) > 1:
        first = map[first]
    if len(last) > 1:
        last = map[last]
    num = int(f'{first}{last}')
    count_p2 += num

print(count_p2)
