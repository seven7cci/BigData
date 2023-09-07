import numpy as np
import pandas as pd

df = pd.DataFrame(
    [
        [4, 9, 10],
        [5, 38, 11],
        [6, 9, 12],
        [6, 9, 12],
    ], index=[1, 2, 3, 4], columns=['a', 'b', 'c']
)
print(df)
df_square = df.apply(lambda x: x * x)
print(df_square)
