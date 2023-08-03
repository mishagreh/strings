# 44. Write a Python program to print the index of a character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9

import collections


def print_index(s: str, char: str) -> tuple:

    return tuple([s.count(char)] + [i[0] for i in enumerate(s) if i[1] == char])


if __name__ == '__main__':
    assert print_index('w3resource', 'r') == (2, 2, 7)
    assert print_index('w3resource', 'w') == (1, 0)
    assert print_index('w3resource', '3') == (1, 1)
    assert print_index('w3resource', 'c') == (1, 8)
    assert print_index('w3resource', 'e') == (2, 3, 9)


s, char = 'w3resource', 'e'
print(print_index(s, char))

# solution
#
# str1 = "w3resource"
# for index, char in enumerate(str1):
#     print("Current character", char, "position at", index )