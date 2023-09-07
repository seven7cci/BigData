class Pokemon:
    def __init__(self, level, hp):
        self.level = level
        self.hp = hp

    def attack(self):
        print('기본 공격을 합니다.')

    def fly(self):
        pass


class Pikachu(Pokemon):
    def fly(self):
        import flyable
        flyable.with_jetpack()


class Charizard(Pokemon):
    def fly(self):
        import flyable
        flyable.with_wings()


p1 = Pikachu(1, 100)
c1 = Charizard(1, 120)
p1.fly()
c1.fly()
