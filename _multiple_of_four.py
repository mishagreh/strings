# 20. Write a Python function to reverse a string if its length is a multiple of 4.

def multiple(s: str) -> str:
    """ returns a reverse a string if its length is a multiple of 4 """
    return s[::-1] if len(s) % 4 == 0 else s


s = 'qwertyuiopas'
print(multiple(s))


# solution
#
# def reverse_string(str1):
#     if len(str1) % 4 == 0:
#        return ''.join(reversed(str1))
#     return str1