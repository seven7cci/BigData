import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')


# 생존자 수와 사망자 수 구하기
survived_human = titanic[titanic['survived'] == 1]['survived'].count()
dead_human = titanic[titanic['survived'] == 0]['survived'].count()
print(f"생존자 수 : {survived_human}")
print(f"사망자 수 : {dead_human}")

# 남성과 여성의 생존율 구하기
male_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'male')]['survived'].count()
female_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'female')]['survived'].count()
male_count = titanic[titanic['sex'] == 'male']['sex'].count()
female_count = titanic[titanic['sex'] == 'female']['sex'].count()
print(f"남성 탑승자 : {male_count}")
print(f"여성 탑승자 : {female_count}")
print(f"남성 생존율 : {male_survived/male_count}")
print(f"여성 생존율 : {female_survived/female_count}")


