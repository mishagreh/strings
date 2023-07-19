# 14. Write a Python program that accepts a comma-separated sequence of words as
# input and prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

def sorted_order(s: str) -> str:
    z = set(s.split(', '))
    return ', '.join(sorted(z))


s = 'red, white, black, red, green, black'
print(sorted_order(s))


# solution
#
# items = input("Input comma separated sequence of words")
# words = [word for word in items.split(",")]
# print(",".join(sorted(list(set(words)))))
