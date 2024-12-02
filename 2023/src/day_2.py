import re

test_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

with open('src/input/day_2.txt', 'r', encoding='utf-8') as text:
    actual_input = text.read()

input = actual_input
lines = input.split('\n')

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total_1 = 0

for i, line in enumerate(lines):
    [_, game] = line.split(':')
    groups = re.split(', |; ', game.strip())
    game_counts = {}
    possible = True
    for group in groups:
        [count, colour] = group.split(' ')
        if int(count) > limits[colour]:
            possible = False
    if possible:
        total_1 += i + 1

print(total_1)

total_2 = 0
powers = []
for i, line in enumerate(lines):
    game_id = i + 1
    [_, game] = line.split(':')
    rounds = game.strip().split('; ')
    min_totals = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for round in rounds:
        groups = round.split(', ')
        for group in groups:
            [count, colour] = group.split(' ')
            if min_totals[colour] < int(count):
                min_totals[colour] = int(count)
    power = 1
    for value in min_totals.values():
        power = power * value
    powers.append(power)

print(sum(powers))
