# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>{{}}', 'Python') -> [[Python]]<<Python>>{{Python}}


def insert_string(*s):
    x = '[]', '<>', '{}'
    y = [s1.find(i) for i in x]
    return f'{s1[:2]}{s2}{s1[y[0]+1:y[1]+1]}{s2}{s1[y[1]+1:y[2]+1]}{s2}{s1[-2:]}'


s = s1, s2 = '[[]]<<>>{{}}', 'Python'
print(insert_string(*s))


# solution
#
# def insert_sting_middle(str, word):
# 	return str[:2] + word + str[2:]
#
# print(insert_sting_middle('[[]]', 'Python'))
# print(insert_sting_middle('{{}}', 'PHP'))
# print(insert_sting_middle('<<>>', 'HTML'))