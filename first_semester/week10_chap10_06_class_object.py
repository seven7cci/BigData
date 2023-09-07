class Pokemon:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('getter 안쪽')
        return self.hidden_name

    def set_name(self, input_name):
        print('setter 안쪽')
        self.hidden_name = input_name

    name = property(get_name, set_name)  # name 프로퍼티 생성, 게터 세터 등록


p1 = Pokemon('피카츄')
print(p1.name)
p1.name = '라이츄'
print(p1.name)

# print(p1.get_name())
# p1.set_name('라이츄')
# print(p1.get_name())

# print(p1.get_name())
# p1.hidden_name = '라이츄'
# print(p1.get_name())
