import pandas as pd
import string

from itertools import cycle


PRIORITY = {
    letter: i 
    for letter, i 
    in zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1))
}
df = (
    pd
    .read_csv('data/day-3.csv', header=None)
)

df['first'] = (
    df
    .apply(lambda x: x[0][:(len(x[0]) // 2)], axis=1)
)
df['second'] = (
    df
    .apply(lambda x: x[0][(len(x[0]) // 2):], axis=1)
)

df['intersection'] = (
    df
    .apply(
        lambda x: list(set(x['first']).intersection(set(x['second'])))[0], axis=1
    )
)

df['priority'] = (
    df
    ['intersection']
    .map(PRIORITY)
)

print(df['priority'].sum())

df.loc[2::3, 'new_index'] = range(df[2::3].shape[0])
df = df.fillna(method='bfill')

c = cycle(range(3))
df.loc[:, 'group'] = [next(c) for _ in range(df.shape[0])]

df_pivoted = (
    df
    .pivot(
        index='new_index',
        columns='group', 
        values=0 
    )
)

print(
    df_pivoted
    .apply(
        lambda x: list(
            set(x[0])
            .intersection(set(x[1]))
            .intersection(set(x[2])), 
        )[0],
        axis=1
    )
    .squeeze()
    .map(PRIORITY)
    .sum()
)
