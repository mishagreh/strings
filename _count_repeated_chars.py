# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
import collections


def repeated_chars(s: str) -> str:
    d = collections.Counter(s)
    return '\n'.join([f'{i[1]} {i[0]}' for i in sorted([(d[i], i) for i in d if d[i] >= 2])[::-1]])


s = 'thequickbrownfoxjumpsoverthelazydog'
print(repeated_chars(s))

# solution
#
# import collections
# str1 = 'thequickbrownfoxjumpsoverthelazydog'
# d = collections.defaultdict(int)
# for c in str1:
#     d[c] += 1
#
# for c in sorted(d, key=d.get, reverse=True):
#   if d[c] > 1:
#       print('%s %d' % (c, d[c]))
