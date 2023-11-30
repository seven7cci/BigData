import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')


# 생존자 수와 사망자 수 구하기
survived_human = titanic[titanic['survived'] == 1]['survived'].count()
dead_human = titanic[titanic['survived'] == 0]['survived'].count()
print(f"생존자 수 :", survived_human)
print(f"사망자 수 :", dead_human)

