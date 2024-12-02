def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as text:
        return text.read()

test_input = read_from_file('src/input/d1_test.txt')
real_input = read_from_file('src/input/d1.txt')

input = real_input

input_lines = input.split('\n')
left = []
right = []
right_dict = {}
for line in input_lines:
    [l, r] = line.split()
    left.append(int(l))
    right.append(int(r))
    right_dict[r] = right_dict.get(r, 0) + 1

left.sort()
right.sort()

diff_count = 0
for i, val in enumerate(left):
    diff_count += abs(val - right[i])

print('part1:', diff_count)

similarity_count = 0
for val in left:
    similarity_count += val * right_dict.get(f'{val}', 0)

print('part2:', similarity_count)
