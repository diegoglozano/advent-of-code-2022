import pandas as pd


TRANSLATE = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

TRANSLATE_2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
SHAPE_POINTS = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

adjacency_matrix = (
    pd
    .DataFrame(
        [[3, 0, 6],
        [6, 3, 0],
        [0, 6, 3]],
        index=['rock', 'paper', 'scissors'],
        columns=['rock', 'paper', 'scissors']
    )
    .rename_axis('local')
    .reset_index()
    .melt(id_vars=['local'], var_name='rival', value_name='result_points')
)


df = (
    pd
    .read_csv('data/day-2.csv', header=None, sep=' ')
    .assign(
        rival=lambda x: x[0].replace(TRANSLATE),
        local_1=lambda x: x[1].replace(TRANSLATE),
        shape_points_1=lambda x: x['local_1'].map(SHAPE_POINTS),
    )
    .merge(
        adjacency_matrix,
        left_on=['rival', 'local_1'],
        right_on=['rival', 'local'],
        how='left'
    )
    .drop(columns='local')
    .rename(columns={'result_points': 'result_points_1'})
    .assign(
        total_points_1=lambda x: x['shape_points_1'] + x['result_points_1']
    )
)

print(
    df
    ['total_points_1']
    .sum()
)

df_2 = (
    df
    .assign(
        result_points_2=lambda x: x[1].replace(TRANSLATE_2),
    )
    .merge(
        adjacency_matrix,
        left_on=['rival', 'result_points_2'],
        right_on=['rival', 'result_points']
    )
    .drop(columns='result_points')
    .rename(columns={'local': 'local_2'})
    .assign(
        shape_points_2=lambda x: x['local_2'].map(SHAPE_POINTS),
        total_points_2=lambda x: x['shape_points_2'] + x['result_points_2']
    )
)

print(
    df_2
    ['total_points_2']
    .sum()
)
