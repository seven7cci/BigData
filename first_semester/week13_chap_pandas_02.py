import numpy as np
import pandas as pd

def square(n):
    """
    제곱 함수
    :param n:
    :return:
    """
    return n * n

df = pd.DataFrame(
    [
        [4, 9, 10],
        [5, 38, 11],
        [6, 9, 12],
        [6, 9, 12],
    ], index=[1, 2, 3, 4], columns=['a', 'b', 'c']
)

print(df)
print('====================')
print(df['b'].value_counts())
print('====================')
print(len(df))
print('====================')
print(df['b'])
print('====================')
print(df['b'].nunique())
print('====================')
print(df.describe())
print('====================')
print(df['c'].sum(), df['c'].mean())
print('====================')
df_square = df.apply(square)
print(df_square)