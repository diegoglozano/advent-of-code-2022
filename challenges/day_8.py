import numpy as np


def check_line(line):
    is_visible = []
    for i, tree in enumerate(line):
        is_visible.append(all(line[:i] < tree))
    return is_visible

def check_scenic_score(line):
    is_visible = []
    for i, tree in enumerate(line):
        is_visible.append(sum(line[:i] <= tree))
    return is_visible

N_ROTATION = 4

with open('data/day-8-test.csv') as f:
    file = f.read().split('\n')

df = np.zeros(shape=(len(file), len(file)))
for i, row in enumerate(file):
    df[i, :] = list(str(row))

final_result = np.zeros(shape=(len(file), len(file)), dtype=bool)
new_df = df.copy()
for n_rot in range(N_ROTATION):
    forest = []
    for row in range(new_df.shape[0]):
        forest.append(check_line(new_df[row, :]))
    forest = np.array(forest)  # [1:-1, 1:-1]
    rotated_forest = np.rot90(forest, k=N_ROTATION - n_rot)
    final_result = final_result | rotated_forest
    new_df = np.rot90(new_df)

print(final_result.sum())


final_result = np.ones(shape=(len(file), len(file)))
new_df = df.copy()
for n_rot in range(N_ROTATION):
    forest = []
    for row in range(new_df.shape[0]):
        forest.append(check_scenic_score(new_df[row, :]))
    forest = np.array(forest)  # [1:-1, 1:-1]
    rotated_forest = np.rot90(forest, k=N_ROTATION - n_rot)
    final_result = final_result * rotated_forest
    new_df = np.rot90(new_df)

print(final_result)