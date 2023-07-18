# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

def first_last(s):
    return s[:2] + s[-2:] if len(s) > 1 else ''


def test_first_last(s):
    assert first_last('w3resource') == 'w3ce'
    assert first_last('w3') == 'w3w3'
    assert first_last('w') == ''
    assert first_last('') == ''


# solution
#
# def string_both_ends(str):
#   if len(str) < 2:
#     return ''
#
#   return str[0:2] + str[-2:]


s = 'w3resource'
print(first_last(s))
test_first_last(s)
