vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word)
                if letter in vowels}
vowel_counts
print(vowel_counts)

empty_dict = {}
print(empty_dict)
empty_set = set()
print(empty_set)

mobile_phone = {0, 1, 0, 9, 5, 5, 6, 3, 8, 5, 2}
print(mobile_phone)

a = {1, 2}
b = {2, 3}
print(a <= b)
print(b <= a)
print(a.issubset(b))

