# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
import textwrap as tw


# removes COMMON for all the strings leading whitespaces
# def no_indent(s):
#     return tw.dedent(s)


# removes ALL the leading whitespaces in each string
def no_indent(s):
    return '\n'.join((i.lstrip() for i in s.split('\n')))


s = """\
     1Note :    In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code 
      2Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substit
       3 cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down
        tab   alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B
    """
print(no_indent(s))

# solution
#
# import textwrap
# sample_text = '''
#     Python is a widely used high-level, general-purpose, interpreted,
#     dynamic programming language. Its design philosophy emphasizes
#     code readability, and its syntax allows programmers to express
#     concepts in fewer lines of code than possible in languages such
#     as C++ or Java.
#     '''
# text_without_Indentation = textwrap.dedent(sample_text)
# print()
# print(text_without_Indentation )