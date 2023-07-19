# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

def lower_upper(s: str) -> tuple:
    return s.lower(), s.upper(), s.casefold(), s.swapcase()


s = input('Enter a word: ')
print(lower_upper(s))


# solution
#
# user_input = input("What's your favourite language? ")
# print("My favourite language is ", user_input.upper())
# print("My favourite language is ", user_input.lower())
