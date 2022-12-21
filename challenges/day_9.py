import numpy as np


with open('data/day-9-test.csv') as f:
    steps = f.read().split('\n')

SIZE = 10000
grid = np.zeros([SIZE, SIZE])
x, y = 0, 0
grid[x, y] = 1
for step in steps:
    direction = step[0]
    n_steps = int(step[-1])
    if direction == 'U':
        for _ in range(n_steps):
            x, y = x, y+1
            grid[x, y] += 1
    elif direction == 'D':
        for _ in range(n_steps):
            x, y = x, y-1
            grid[x, y] += 1
    elif direction == 'L':
        for _ in range(n_steps):
            x, y = x-1, y
            grid[x, y] += 1
    elif direction == 'R':
        for _ in range(n_steps):
            x, y = x+1, y
            grid[x, y] += 1

print(
    grid[:grid.argmax(axis=0), :grid.argmax(axis=1)]
)