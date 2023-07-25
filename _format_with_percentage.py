# 36. Write a Python program to format a number with a percentage.

def percentage(num: float, prec: int) -> str:
    return f'{num:.{prec}%}'


if __name__ == '__main__':
    assert percentage(0.28, 0) == '28%'
    assert percentage(0.66666, 2) == '66.67%'
    assert percentage(1.0512345, 3) == '105.123%'
    assert percentage(0.28282828, 5) == '28.28283%'

num, prec = 0.66666, 2
print(percentage(num, prec))

# solution
#
# x = 0.25
# y = -0.25
# print("\nOriginal Number: ", x)
# print("Formatted Number with percentage: "+"{:.2%}".format(x));
# print("Original Number: ", y)
# print("Formatted Number with percentage: "+"{:.2%}".format(y));
