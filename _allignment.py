# 37. Write a Python program to display a number in left, right, and center aligned with a width of 10.

def allingment(word: str, width: int) -> str:
    types = '<', '>', '^'
    for i in types:
        print(f'[{i} within {width}]{word:{i}{width}}')


word, width = 'four', 6
allingment(word, width)

# solution
#
# x = 22
# print("\nOriginal Number: ", x)
# print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
# print("Right aligned (width 10)  :"+"{:10d}".format(x));
# print("Center aligned (width 10) :"+"{:^10d}".format(x));
# print()
