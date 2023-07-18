# 4. Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def occur_change(s):
    new_s = s[0]
    for i in s[1:]:
        if i == s[0]:
            i = i.replace(i, '$')
        new_s += i
    return new_s, new_s == 'resta$t'


# solution
#
# def change_char(str1):
#   char = str1[0]
#   str1 = str1.replace(char, '$')
#   str1 = char + str1[1:]
#
#   return str1


s = 'restart'
print(occur_change(s))
