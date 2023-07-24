# 34. Write a Python program to print the following integers with '*' to the right of the specified width.

def add_asterisks(num: int, symbol: str, symbols_num: int) -> str:
    return f'{num:{symbol}<{symbols_num + len(str(num))}}'


if __name__ == '__main__':
    assert add_asterisks(10, '*', 10) == '10**********'
    assert add_asterisks(3, '/', 3) == '3///'
    assert add_asterisks(1, '?', 2) == '1??'

# solution
#
# x = 3
# y = 123
# print("\nOriginal Number: ", x)
# print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x));
# print("Original Number: ", y)
# print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y));
# print()
