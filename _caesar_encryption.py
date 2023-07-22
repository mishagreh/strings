# 25. Write a Python program to create a Caesar encryption.
#
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
# is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each
# letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a
# left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar,
# who used it in his private correspondence.

def caesar(string: str, shift: int) -> str:
    alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = alphabet1[shift:] + alphabet1[:shift]
    return string.translate(string.maketrans(alphabet1, alphabet2))


string, shift = 'abcd', 1
print(caesar(string, shift))


# solution
#
#
# # https://gist.github.com/nchitalov/2f2b03e5cf1e19da1525
# def caesar_encrypt(realText, step):
#     outText = []
#     cryptText = []
#
#     uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#                  'U', 'V', 'W', 'X', 'Y', 'Z']
#     lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                  'u', 'v', 'w', 'x', 'y', 'z']
#
#     for eachLetter in realText:
#         if eachLetter in uppercase:
#             index = uppercase.index(eachLetter)
#             crypting = (index + step) % 26
#             cryptText.append(crypting)
#             newLetter = uppercase[crypting]
#             outText.append(newLetter)
#         elif eachLetter in lowercase:
#             index = lowercase.index(eachLetter)
#             crypting = (index + step) % 26
#             cryptText.append(crypting)
#             newLetter = lowercase[crypting]
#             outText.append(newLetter)
#     return outText