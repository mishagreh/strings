# 28. Write a Python program to add prefix text to all of the lines in a string.
import textwrap as tw


def add_prefix(string: str, pref: str) -> str:
    return tw.indent(string, pref, lambda line: True)


if __name__ == '__main__':
    assert add_prefix(' abcd\n dcba', '+') == '+ abcd\n+ dcba'
    assert add_prefix(' abcd\n\n\n dcba', '+') == '+ abcd\n+\n+\n+ dcba'
    assert add_prefix(' abcd\n dcba\n 1234', '>') == '> abcd\n> dcba\n> 1234'
    assert add_prefix(' abcd\n dcba\n qwer\n asdf', '-') == '- abcd\n- dcba\n- qwer\n- asdf'

string, pref = ' abcd\n dcba', '+'
print(add_prefix(string, pref))


# solution
#
# import textwrap
# sample_text ='''
#     Python is a widely used high-level, general-purpose, interpreted,
#     dynamic programming language. Its design philosophy emphasizes
#     code readability, and its syntax allows programmers to express
#     concepts in fewer lines of code than possible in languages such
#     as C++ or Java.
#     '''
# text_without_Indentation = textwrap.dedent(sample_text)
# wrapped = textwrap.fill(text_without_Indentation, width=50)
# #wrapped += '\n\nSecond paragraph after a blank line.'
# final_result = textwrap.indent(wrapped, '> ')
# print()
# print(final_result)
# print()