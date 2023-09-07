class Pokemon:
    pokemon_count = 0  # class variable, class field

    def __init__(self, input_name, input_level):
        self.__name = input_name  # like private
        self.__level = input_level
        Pokemon.pokemon_count = Pokemon.pokemon_count + 1

    @property
    def name(self):
        print('getter 안쪽')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('setter 안쪽')
        self.__name = input_name

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, input_level):
        self.__level = input_level

    @classmethod
    def get_pokemon_count(cls):
        # return Pokemon.pokemon_count
        # return cls.pokemon_count
        print(f'포켓몬 인구 수 : {cls.pokemon_count}')


#print(Pokemon.get_pokemon_count())
#print(Pokemon.pokemon_count)
Pokemon.get_pokemon_count()
p1 = Pokemon('피카츄', 1)
p2 = Pokemon('리자몽', 36)
Pokemon.pokemon_count = 9
print(Pokemon.pokemon_count)
p3 = Pokemon('리자몽', 8)
print(Pokemon.pokemon_count)
print(p1.pokemon_count)
print(p2.pokemon_count)
print(p3.pokemon_count)


# p1 = Pokemon('피카츄')
print(p1.name)
# p1.name = '라이츄'
# p1.hidden_name = '라이츄'  # real private는 아님
# p1.__name = '라이츄'  # 적용되지 않음
print(p1.name)
# print(p1.__name)  # AttributeError
# print(p1._Pokemon__name)  # real private는 아님, _클래스명__name으로 접근

# error
# print(p1.get_name())
# p1.set_name('라이츄')
# print(p1.get_name())

# print(p1.get_name())
# p1.hidden_name = '라이츄'
# print(p1.get_name())
