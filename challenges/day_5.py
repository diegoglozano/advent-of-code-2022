import pandas as pd
import re

from copy import deepcopy

df = (
    pd
    .read_csv(
        'data/day-5-1.csv',
        header=None,
        sep=','
    )
    .applymap(
        lambda x: (
            re
            .sub(
                '\[|\]',
                '',
                x.strip()
            )
        )
    )
)
with open('data/day-5-2.csv') as f:
    movements = f.read().split('\n')

stacks = [
    [
        crate 
        for crate 
        in stack[::-1] 
        if crate != ''
    ]
    for stack 
    in df.transpose().values.tolist()
]

stacks_1 = deepcopy(stacks)
for movement in movements:
    clean_movement = re.sub(
        '\s*[a-z]\s*', '', movement
    )
    n_crates = int(clean_movement[:-2])
    from_stack = int(clean_movement[-2]) - 1
    to_stack = int(clean_movement[-1]) - 1

    for _ in range(n_crates):
        stacks_1[to_stack].append(stacks_1[from_stack].pop())

print(''.join([
    stack[-1]
    for stack in stacks_1
]))

stacks_2 = deepcopy(stacks)
for i, movement in enumerate(movements):
    clean_movement = re.sub(
        '\s*[a-z]\s*', '', movement
    )
    n_crates = int(clean_movement[:-2])
    from_stack = int(clean_movement[-2]) - 1
    to_stack = int(clean_movement[-1]) - 1

    stacks_2[to_stack].extend(stacks_2[from_stack][-n_crates:])
    stacks_2[from_stack] = stacks_2[from_stack][:-n_crates]

print(''.join([
    stack[-1]
    for stack in stacks_2
]))