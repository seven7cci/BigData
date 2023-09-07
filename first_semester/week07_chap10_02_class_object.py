class Car:
    def __init__(self, kind):
        self.kind = kind

    def exclain(self):
        print("나는 차")


class Hyundai(Car):
    def __init__(self, kind, level):
        # self.kind = kind
        super().__init__(kind)  # 부모 클래스의 필드 사용
        self.level = level  # 자식 클래스 자체 필드

    def exclain(self):  # override
        print("나는 현대차")

    def need_a_push(self):
        print("도움")


print(issubclass(Hyundai, Car))
give_me_a_car = Car("화물차")
give_me_a_Hyundai = Hyundai("승용차", "중형")

print(give_me_a_Hyundai.kind)
print(give_me_a_Hyundai.level)

# give_me_a_Hyundai.exclain()  # 부모 클래스의 메서드를 자식이 사용
give_me_a_Hyundai.exclain()  # 오버라이드 된 자식 클래스의 메서드를 사용
give_me_a_car.exclain()

give_me_a_Hyundai.need_a_push()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#
# cat1 = Cat('나비')
# cat2 = Cat('콩순이')
