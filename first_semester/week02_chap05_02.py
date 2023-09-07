print('%e' % 7.03)
print(7.03e-2)
print(7.03e+2)


blurt = "What the.$...!!?"
print(blurt.strip('.?!'))

numbers = input().split()
for number in range(int(numbers[0]), int(numbers[1])+1):
    print(number, end=' ')
