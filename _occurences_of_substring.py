# 38. Write a Python program to count occurrences of a substring in a string.

def substr_occur(s: str, subs: str) -> int:
    return s.count(subs)


if __name__ == '__main__':
    assert substr_occur('# 38. Write a Python program to count occurrences of a substring in a string.', ' a ') == 3
    assert substr_occur('', 'word') == 0
    assert substr_occur('# 38. Write a Python program to count occurrences of a substring in a string.', '') == 78
    assert substr_occur(' Write a Python function to get a string made of the first three characters '
                        'of a specified string. If the length of the string is less than 3, '
                        'return the original string.', 'string') == 4
    assert substr_occur(' Write a Python function to get a string made of the first three characters '
                        'of a specified string. If the length of the string is less than 3, '
                        'return the original string.', 'of the') == 2

s, subs = '# 38. Write a Python program to count occurrences of a substring in a string.', ''
print(substr_occur(s, subs))
print(len(s))

# solution
#
# str1 = 'The quick brown fox jumps over the lazy dog.'
# print()
# print(str1.count("fox"))
# print()