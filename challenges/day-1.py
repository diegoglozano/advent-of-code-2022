import pandas as pd

df = (
    pd
    .read_csv(
        'data/day-1.csv', 
        header=None, 
        skip_blank_lines=False
    )
    .assign(
        is_group=lambda x: x.isna(),
        group_number=lambda x: x['is_group'].astype('int').cumsum()
    )
    .groupby('group_number')
    .agg(total=(0, 'sum'))
)
print(
    df
    .max()
)

print(
    df
    .nlargest(3, columns='total')
    .sum()
)
