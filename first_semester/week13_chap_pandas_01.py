import numpy as np
import pandas as pd

df1 = pd.DataFrame(
    {
        "a": [4, 5, 6],
        "b": [7, 8, 9],
        "c": [10, 11, 12]
    }, index=[1, 2, 3]
)
# print(df1)

df2 = pd.DataFrame(
    [
        [4, 7, 10],
        [5, 38, 11],
        [6, 9, 12]
    ], index=[1, 2, 3], columns=['a', 'b', 'c']
)
print(df2)
df3 = pd.melt(df2).rename(columns={'variable':'var', 'value':'val'}).query('val >= 9')
print(df3)

# print(df1.head(2))
# print(df1.tail(2))

print(df2.sort_values('c', ascending=False))
df4 = df2.drop(columns='a')
print(df4)
df5 = df2.iloc[:, [0, 2]]
print(df5)
df6 = df2.loc[:, ['a', 'c']]
print(df6)
df7 = df2.loc[df2['b'] >= 9, ['a', 'c']]
print(df7)

print(df2.iat[1, 1])  # by index
print(df2.at[2, 'b'])  # by label
