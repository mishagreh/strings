# 43. Write a Python program to print the square and cube symbols in the area of a rectangle
# and the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
import math


def area_volume(rect: tuple, cyl: tuple) -> str:
    # return f'{a * b:.2f} {c}{chr(178)}\n{h * math.pi * r ** 2:.2f} {d}{chr(179)}'
    return f'{a * b:.2f} {c}\u00b2\n{h * math.pi * r ** 2:.2f} {d}\u00b3'


rect = a, b, c = 3, 4, 'cm'
cyl = r, h, d = 2, 7, 'm'
print(area_volume(rect, cyl))

# solution
#
# area = 1256.66
# volume = 1254.725
# decimals = 2
# print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
# decimals = 3
# print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))
