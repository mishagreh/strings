# 41. Write a Python program to strip a set of characters from a string.

def strip_chars(s: str) -> tuple:
    for i in s:
        return s.lstrip(), s.strip(), s.rstrip()


if __name__ == '__main__':
    assert strip_chars('       Write       qq         ') == ('Write       qq         ', 'Write       qq',
                                                             '       Write       qq')

s = '       Write       qq         '
print(strip_chars(s))

solution

