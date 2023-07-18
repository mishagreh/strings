# 10. Write a Python program to change a given string to a newly string
# where the first and last chars have been exchanged.

def first_last_exchanged(s: str):
    a = s.partition(s[1:-1])
    return a[2] + a[1] + a[0]


s = 'Write a Python program to change a given string to a newly string'
print(first_last_exchanged(s))


# solution
#
# def change_string(str1):
#     return str1[-1:] + str1[1:-1] + str1[:1]
