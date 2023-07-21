# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python

def before(s: str) -> str:
    return s.partition('-')[0]


s = 'https://www.w3resource.com/python-exercises'
print(before(s))


# solution
#
# str1 = 'https://www.w3resource.com/python-exercises/string'
# print(str1.rsplit('/', 1)[0])
# print(str1.rsplit('-', 1)[0])
#
# Sample Output:
#
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
