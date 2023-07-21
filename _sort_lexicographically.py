# 22.Write a Python program to sort a string lexicographically.

def sort_lg(s: str) -> str:
    """ returns a lexicographically sorted string """

    return ''.join(sorted(s))


s = 'python'
print(sort_lg(s))

# solution
#
# def lexicographi_sort(s):
#     return sorted(sorted(s), key=str.upper)
