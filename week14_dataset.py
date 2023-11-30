import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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

# 객실 등급별 생존자 수 구하기
# pclass_survived = titanic.groupby('pclass')['survived'].sum()
pclass_survived = titanic[titanic['survived'] == 1].groupby(['pclass']).size()
print(pclass_survived)

# 나이대별 생존자 수 구하기
age_survived = titanic.groupby(pd.cut(titanic['age'], bins=list(range(0, 81, 10))))['survived'].sum()
print(age_survived)

# 생존자와 사망자의 나이 분포를 시각화
survived_ages = titanic[titanic['survived'] == 1]['age'].dropna()
dead_ages = titanic[titanic['survived'] == 0]['age'].dropna()

plt.hist(survived_ages, bins=20, label='Survived', alpha=0.5)
plt.hist(dead_ages, bins=20, label='Dead', alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.show()
