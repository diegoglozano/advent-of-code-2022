CYCLE_DICT = {
    'noop': 1,
    'addx': 2
}

CYCLES_OUTPUT = range(20, 220 + 1, 40)

with open('data/day-10-test.csv') as f:
    program = f.read().split('\n')

X = 1
cycles = 0
output = 0
for line in program:
    try:
        action, number = line.split(' ')
    except:
        action = line
    for _ in range(CYCLE_DICT[action]):
        cycles += 1
        if cycles in CYCLES_OUTPUT:
            output += X * cycles
    if action == 'addx':
        X += int(number)

print(output)

# Sprites
import numpy as np
output = np.repeat('.', repeats=240).reshape(6, 40)

X = 1
cycles = 0
sprite_pos = np.array([0, 1, 2])
row = 0
print(row)
print(sprite_pos)
for line in program:
    try:
        action, number = line.split(' ')
    except:
        action = line
    for _ in range(CYCLE_DICT[action]):
        if cycles in sprite_pos:
            output[row, cycles] = '#'
        cycles = (cycles + 1) % 40
        if cycles % 40 == 0:
            row += 1
            print(row)
            sprite_pos = np.array([0, 1, 2])
    if action == 'addx':
        X += int(number)
        sprite_pos += int(number)
        print(sprite_pos)

print(output)