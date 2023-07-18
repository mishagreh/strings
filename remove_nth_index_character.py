# 9. Write a Python program to remove the nth index character from a nonempty string.


def remove_nth(s, n):
    return s.replace(s[n], '')


s = '# 9. Write a Python program to remove the nth index character from a nonempty string.'
n = 13
print(remove_nth(s, n))

# solution
#
# def remove_char(str, n):
#     first_part = str[:n]
#     last_part = str[n + 1:]
#     return first_part + last_part
