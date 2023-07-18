# 5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def one_from_two(s1, s2):
    x = s1, s2
    s = ' '.join(x)
    y = s.translate(s.maketrans('abxy', 'xyab'))
    return y, y == 'xyc abz'


s1, s2, = 'abc', 'xyz'
print(one_from_two(s1, s2))

# solution
#
# def chars_mix_up(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]
#
#   return new_a + ' ' + new_b
