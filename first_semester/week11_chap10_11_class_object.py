class Trainer:
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon

    def pokemon_info(self):
        print(f"{self.name}의 소유 포켓몬은 {self.pokemon}입니다")
        print(f"{self.pokemon.name}의 레벨은 {self.pokemon.level}입니다")


class Pokemon:
    pokemon_count = 0  # class variable, class field

    def __init__(self, input_name, input_level):
        self.__name = input_name  # like private
        self.__level = input_level
        Pokemon.pokemon_count = Pokemon.pokemon_count + 1

    @property
    def name(self):
        # print('getter 안쪽')
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

    @staticmethod
    def info():
        print('포켓몬 클래스')

    def __str__(self):
        # return f'포켓몬 객체의 ID값 : {id(self)}'
        return self.__name

    def __add__(self, other):
        """
        포켓몬 객체끼리 + 연산 시 두 포켓몬의 레벨의 합을 리턴하는 magic method
        :param other: + 연산 기호 우측 객체
        :return: 두 객체 레벨의 합
        """
        return self.__level + other.__level


p1 = Pokemon('피카츄', 1)
print(p1)
p2 = Pokemon('리자몽', 36)
print(p2)
t1 = Trainer('한지우', p2)
t1.pokemon_info()
