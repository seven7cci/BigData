from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

print(duck, type(duck))
print(f"부리 : {duck.bill}, 꼬리 : {duck.tail}")

# 딕셔너리를 사용
parts = {'bill' : 'wide orange', 'tail' : 'long'}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)