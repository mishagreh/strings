# 40. Write a Python program to reverse words in a string.

def reverse_words(s: str) -> str:
    # return ' '.join((i[::-1] for i in s.split()))
    return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    # assert reverse_words('# 40. Write a Python program') == '# .04 etirW a nohtyP margorp'
    assert reverse_words('# 40. Write a Python program') == 'program Python a Write 40. #'

s = '# 40. Write a Python program'
print(reverse_words(s))

# solution
#
# def reverse_string_words(text):
#     for line in text.split('\n'):
#         return(' '.join(line.split()[::-1]))
# print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
# print(reverse_string_words("Python Exercises."))
