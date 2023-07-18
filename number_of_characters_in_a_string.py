# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

import collections


def freq(string):
    return collections.Counter(string)


def test_freq(string):
    return freq(string) == {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


string = 'google.com'
print(dict(freq(string)))
print(test_freq(string))
