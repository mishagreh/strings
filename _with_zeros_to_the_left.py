# 33. Write a Python program to print the following integers with zeros to the left of the specified width.

def add_zeros(num: int, zeros: int) -> str:
    return str(num).zfill(zeros + len(str(num)))


if __name__ == '__main__':
    assert add_zeros(1, 1) == '01'
    assert add_zeros(5, 5) == '000005'
    assert add_zeros(60, 3) == '00060'
    assert add_zeros(600, 3) == '000600'

# solution
#
# x = 3
# y = 123
# print("\nOriginal Number: ", x)
# print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x));
# print("Original Number: ", y)
# print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y));
