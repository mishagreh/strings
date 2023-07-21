# 18. Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

def first_three(s: str) -> str:
    """ returns first three chars of a string or the string itself """

    return s[:3] if len(s) > 3 else s


s = 'python'
print(first_three(s))


# solution
#
# def first_three(str):
# 	return str[:3] if len(str) > 3 else str
