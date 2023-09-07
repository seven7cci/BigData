class Cat:
    pass


a_cat = Cat()
print(type(a_cat), id(a_cat))

another_cat = Cat()
print(type(another_cat), id(another_cat))

a_cat.age = 3
a_cat.name = "냐옹이"
a_cat.nemesis = another_cat

print(a_cat.age, a_cat.name, a_cat.nemesis)
# print(a_cat.nemesis.name)  # another_cat.name이 없어서 에러
another_cat.name = "야옹이"
print(a_cat.nemesis.name)