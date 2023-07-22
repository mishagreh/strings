# 26. Write a Python program to display formatted text (width=50) as output.
import textwrap as tw


def form_text(s: str, n: int) -> str:
    return '\n'.join([s[i:i + n] for i in range(0, len(s), n + 1)])


s = "Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or " \
    "Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution" \
    " cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the" \
    " alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B"
n = 10
print(form_text(s, n))


# solution
#
# import textwrap
# sample_text = '''
#   Python is a widely used high-level, general-purpose, interpreted,
#   dynamic programming language. Its design philosophy emphasizes
#   code readability, and its syntax allows programmers to express
#   concepts in fewer lines of code than possible in languages such
#   as C++ or Java.
#   '''
# print()
# print(textwrap.fill(sample_text, width=50))
