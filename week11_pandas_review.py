import pandas as pd

df = pd.DataFrame(
    [
        [99, 89, 100],
        [91, 98, 90],
        [100, 97, 85],
        [83, 100, 94],
    ], index=[1, 2, 3, 4], columns=["KOR", "ENG", "MAT"]
)
print(df)

# 국어 성적과 영어 성적이 둘 다 95점 이상인 행을 추출
print(df.query('KOR >= 95 and ENG >= 95'))

# 국어, 수학 컬럼을 추출
# 조건은 국어 성적이 95점 이상인 경우
df_copy = df.loc[df['KOR'] >= 95, ['KOR', 'MAT']]

# 1번 학생의 수학 성적(100) 출력
print(df.at[1, 'MAT'])  # value by label
print(df.iat[0, 2])  # value by index

print(df_copy)
