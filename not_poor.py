# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def not_poor(s):
    words = ['not', 'poor']
    nums = [s.find(i) for i in words]
    if nums[0] < nums[1]:
        return s[:nums[0]] + 'good!'
    return s


s = 'The lyrics is not that poor!'
print(not_poor(s))

# solution
#
# def not_poor(str1):
#     snot = str1.find('not')
#     spoor = str1.find('poor')
#
#     if spoor > snot and snot > 0 and spoor > 0:
#         str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
#         return str1
#     else:
#         return str1
