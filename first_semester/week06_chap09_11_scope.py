animal = '과일박쥐'


def print_animal():
    global animal  # 전역변수 animal을 말함. 지역변수 X
    plants = '장미'
    animal = '웜뱃'
    print(animal, id(animal))  # UnboundLocalError: cannot access local variable 'animal' where it is not associated with a value
    print(locals())
    print(globals())


print(abs.__doc__)

print_animal()
print(animal, id(animal))
print(globals())

animal = '과일박쥐'
#
#
# def print_animal():
#     animal = '웜뱃'
#     print(animal, id(animal))  # UnboundLocalError: cannot access local variable 'animal' where it is not associated with a value
#
#
# print_animal()
# print(animal, id(animal))

# animal = '과일박쥐'
#
#
# def print_animal():
#     print(animal)  # UnboundLocalError: cannot access local variable 'animal' where it is not associated with a value
#     animal = '웜뱃'
#
#
# print_animal()


# animal = '과일박쥐'
#
#
# def print_animal():
#     print(animal)
#
#
# print_animal()
