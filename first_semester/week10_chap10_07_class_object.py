class Pokemon:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('getter 안쪽')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('setter 안쪽')
        self.hidden_name = input_name


p1 = Pokemon('피카츄')
print(p1.name)
p1.name = '라이츄'
# p1.hidden_name = '라이츄'
print(p1.name)

# error
# print(p1.get_name())
# p1.set_name('라이츄')
# print(p1.get_name())

# print(p1.get_name())
# p1.hidden_name = '라이츄'
# print(p1.get_name())
