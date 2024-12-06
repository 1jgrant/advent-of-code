from typing import List, Tuple

def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as text:
        return text.read()

test_input = read_from_file('src/input/d4_test.txt')
real_input = read_from_file('src/input/d4.txt')
input = real_input

lines = input.split('\n')

def extract_word_in_range(ranges: Tuple[List[str]], lines: List[str]):
    x_range, y_range = ranges
    string = ''
    try:
        for i, x in enumerate(x_range):
            if x < 0 or y_range[i] < 0:
                return ''
            string += lines[y_range[i]][x]
        return string
    except IndexError:
        return ''

max_y = len(lines) - 1
xmas_count = 0
for y, line in enumerate(lines):
    max_x = len(line) - 1
    for x, char in enumerate(line):
        if char != 'X':
            continue
        u_ranges = ([x,x,x,x], [y,y-1,y-2,y-3])
        ur_ranges = ([x,x+1,x+2,x+3], [y,y-1,y-2,y-3])
        r_ranges = ([x,x+1,x+2,x+3], [y,y,y,y])
        rd_ranges = ([x,x+1,x+2,x+3], [y,y+1,y+2,y+3])
        d_ranges = ([x,x,x,x], [y,y+1,y+2,y+3])
        dl_ranges = ([x,x-1,x-2,x-3], [y,y+1,y+2,y+3])
        l_ranges = ([x,x-1,x-2,x-3], [y,y,y,y])
        ul_ranges = ([x,x-1,x-2,x-3], [y,y-1,y-2,y-3])

        ranges = [u_ranges, ur_ranges, r_ranges, rd_ranges, d_ranges, dl_ranges, l_ranges, ul_ranges]
        for range in ranges:
            word = extract_word_in_range(range, lines)
            if word == 'XMAS':
                xmas_count += 1

print('part1:', xmas_count)

x_mas_count = 0
for y, line in enumerate(lines):
    max_x = len(line) - 1
    for x, char in enumerate(line):
        if char != 'A':
            continue
        ranges = [[[x-1,x,x+1],[y-1,y,y+1]], [[x-1,x,x+1],[y+1,y,y-1]]]
        words = [extract_word_in_range(range, lines) for range in ranges]
        if all(word == 'MAS' or word == 'SAM' for word in words):
            x_mas_count += 1

print('part2:', x_mas_count)

