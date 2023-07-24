# 30. Write a Python program to print the following numbers up to 2 decimal places.

def two_decimals(num: float) -> float:
    return float(f'{num:.2f}')


if __name__ == '__main__':
    assert two_decimals(1.99999999) == 2.00
    assert two_decimals(0.123) == 0.12
    assert two_decimals(500.4321) == 500.43

num = 1.99999999
print(two_decimals(num))

# solution
#
# x = 3.1415926
# y = 12.9999
# print("\nOriginal Number: ", x)
# print("Formatted Number: "+"{:.2f}".format(x));
# print("Original Number: ", y)
# print("Formatted Number: "+"{:.2f}".format(y));
# print()
