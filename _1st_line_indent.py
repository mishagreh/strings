# 29. Write a Python program to set the indentation of the first line.
import textwrap as tw


def first_line_indent(s: str, width: int, indent: int) -> str:
    s1 = ' ' * indent + s
    return ' ' * indent + '\n'.join((i.lstrip() for i in s1.split('\n')))


s, width, indent = """\
                   Note : In cryptography, 
                   a Caesar's cipher, also
                    known as Caesar's cipher, 
                   the shift cipher, Caesar's
                    code or Caesar shift
                   """, 20, 5
print(first_line_indent(s, width, indent))

# solution
#
# sample_text ='''
# Python is a widely used high-level, general-purpose, interpreted, dynamic
# programming language. Its design philosophy emphasizes code readability,
# and its syntax allows programmers to express concepts in fewer lines of
# code than possible in languages such as C++ or Java.
#     '''
#
# text1 =  textwrap.dedent(sample_text).strip()
# print()
# print(textwrap.fill(text1,
#                     initial_indent='',
#                     subsequent_indent=' ' * 4,
#                     width=80,
#                     ))
# print()