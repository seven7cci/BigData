import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

print(titanic.isnull().sum())
print(titanic['age'].fillna(titanic['age'].median(), inplace=True))
print(titanic.isnull().sum())

# print(titanic['deck'].fillna('unknown', inplace=True))  # 범주 항목에 unknown이 없어서 에러
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')  # 카테고리 추가
print(titanic['deck'].fillna('Unknown', inplace=True))

# print(titanic.head())
# print(titanic.describe())
# print(titanic.info())
# print(titanic.tail())

print(titanic['deck'].tail(10))
