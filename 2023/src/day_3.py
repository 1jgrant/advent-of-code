import re

test_input = '''467..114..
...*.....
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

with open('src/input/day_3.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()

input = actual_input

lines = input.split('\n')
input_length = len(lines)
line_length = len(lines[0])

symbol_indices = {}

for i, line in enumerate(lines):
    symbol_iter = re.finditer(r'[^a-zA-Z\d\s:\.]', line)
    line_indices = [match.start(0) for match in symbol_iter]
    for index in line_indices:
        symbol_indices[f'{i},{index}'] = True


nums_adjacent_to_symbol = []
for i, line in enumerate(lines):
    num_iter = re.finditer(r'\d+', line)
    line_matches = [(m.group(), m.span()) for m in num_iter]
    for match_group in line_matches:
        [num_str, indices] = match_group
        num = int(num_str)
        num_start = indices[0]
        num_end = indices[1]
        num_adjacent_range = []
        for j in range(num_start - 1, num_end + 1):
            num_adjacent_range.extend([f'{i-1},{j}',f'{i},{j}',f'{i+1},{j}'])
        for coords in num_adjacent_range:
            if coords in symbol_indices:
                nums_adjacent_to_symbol.append(num)

print('part 1:', sum(nums_adjacent_to_symbol))

star_coords = []
for i, line in enumerate(lines):
    star_iter = re.finditer(r'\*', line)
    star_indices = [match.start(0) for match in star_iter]
    for index in star_indices:
        star_coords.append(f'{i},{index}')

num_adjacent_map = {}
for i, line in enumerate(lines):
    num_iter = re.finditer(r'\d+', line)
    line_matches = [(m.group(), m.span()) for m in num_iter]
    for match_group in line_matches:
        [num_str, indices] = match_group
        num = int(num_str)
        num_start = indices[0]
        num_end = indices[1]
        num_adjacent_range = []
        for j in range(num_start - 1, num_end + 1):
            check_range = [f'{i-1},{j}',f'{i},{j}',f'{i+1},{j}']
            for coord in check_range:
                if coord in num_adjacent_map:
                    num_adjacent_map[coord].append(num)
                else:
                    num_adjacent_map[coord] = [num]


gear_ratios = []
for star_coord in star_coords:
    adjacent_nums = num_adjacent_map[star_coord]
    if len(adjacent_nums) == 2:
        gear_ratio = adjacent_nums[0] * adjacent_nums[1]
        gear_ratios.append(gear_ratio)

print('part 2:', sum(gear_ratios))