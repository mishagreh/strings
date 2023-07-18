# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def ing_or_ly(s):
    if len(s) > 2:
        if s[-3:] != 'ing':
            s += 'ing'
        else:
            s += 'ly'
    return s


s = 'stting'
print(ing_or_ly(s))

# solution
#
# def add_string(str1):
#   length = len(str1)
#
#   if length > 2:
#     if str1[-3:] == 'ing':
#       str1 += 'ly'
#     else:
#       str1 += 'ing'
#   return str1