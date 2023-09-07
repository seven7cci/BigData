def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')  # expect ['b']


def work(arg):
    result = []
    result.append(arg)
    print(result)


work('a')
work('b')


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nonbuggy('a')
nonbuggy('b')
nonbuggy('c', ['d'])