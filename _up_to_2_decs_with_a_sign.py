# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.

def two_with_sign(num: float) -> str:
    # return {num < 0: f'{num:.2f}', num > 0: f'+{num:.2f}'}.get(True)
    return f'{num:+.2f}'


if __name__ == '__main__':
    assert two_with_sign(-1.141) == '-1.14'
    assert two_with_sign(-22.5566) == '-22.56'
    assert two_with_sign(-500.1234) == '-500.12'
    assert two_with_sign(500.1234) == '+500.12'

num = 500.1234
print(two_with_sign(num))

# solution
#
# x = 3.1415926
# y = 12.9999
# print("\nOriginal Number: ", x)
# print("Formatted Number: "+"{:.2f}".format(x));
# print("Original Number: ", y)
# print("Formatted Number: "+"{:.2f}".format(y));