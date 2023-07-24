# 32. Write a Python program to print the following positive and negative numbers with no decimal places.

def no_decimals(num: float) -> tuple:
    return int(num), f'{num:.0f}'


if __name__ == '__main__':
    assert no_decimals(1.12345) == (1, '1')
    assert no_decimals(10.12345) == (10, '10')
    assert no_decimals(-100.92345) == (-100, '-101')

# solution
#
# x = 3.1415926
# y = -12.9999
# print("\nOriginal Number: ", x)
# print("Formatted Number with no decimal places: "+"{:.0f}".format(x));
# print("Original Number: ", y)
# print("Formatted Number with no decimal places: "+"{:.0f}".format(y));
# print()
