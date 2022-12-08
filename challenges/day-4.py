from os import name
import pandas as pd

df = (
    pd
    .read_csv(
        'data/day-4.csv', 
        header=None, 
        names=['first', 'second']
    )
)

df['first_in_second'] = (
    df
    .apply(
        lambda x: all([
            i in range(int(x['second'].split('-')[0]), int(x['second'].split('-')[1]) + 1)
            for i 
            in range(int(x['first'].split('-')[0]), int(x['first'].split('-')[1]) + 1)
        ]),
        axis=1
    )
)

df['second_in_first'] = (
    df
    .apply(
        lambda x: all([
            i in range(int(x['first'].split('-')[0]), int(x['first'].split('-')[1]) + 1)
            for i 
            in range(int(x['second'].split('-')[0]), int(x['second'].split('-')[1]) + 1)
        ]),
        axis=1
    )
)

print(
    df
    ['first_in_second']
    .__or__(df['second_in_first'])
    .sum()
)

df['overlap'] = (
    df
    .apply(
        lambda x: len(
            set(range(int(x['first'].split('-')[0]), int(x['first'].split('-')[1]) + 1))
            .intersection(set(range(int(x['second'].split('-')[0]), int(x['second'].split('-')[1]) + 1)))
        ) > 0,
        axis=1
    )
)
print(
    df['overlap']
    .sum()
)