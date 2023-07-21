# 17. Write a Python function to get a string made of 4 copies of the last two
# characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

def four_copies(s: str) -> str:
    return s[-2:] * 4


s = 'Exercises'
print(four_copies(s))


# solution
#
# def insert_end(str):
# 	sub_str = str[-2:]
# 	return sub_str * 4