# 35. Write a Python program to display a number with a comma separator.

def add_separator(num: int, separ: str):
    return f'{num:{separ}}'


if __name__ == '__main__':
    assert add_separator(1000000, ',') == '1,000,000'
    assert add_separator(1000000, '_') == '1_000_000'

num, separ = 100000000, ' '
print(add_separator(num, separ))

# solution
#
# x = 3000000
# y = 30000000
# print("\nOriginal Number: ", x)
# print("Formatted Number with comma separator: "+"{:,}".format(x));
# print("Original Number: ", y)
# print("Formatted Number with comma separator: "+"{:,}".format(y));
# print()
