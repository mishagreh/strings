# 11. Write a Python program to remove characters that have odd index values in a given string.


def odd_index_values(s: str):
    return ''.join([j for i, j in enumerate(s) if i % 2 == 0])


s = 'python'
print(odd_index_values(s))


# solution
#
# def odd_values_string(str):
#   result = ""
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result