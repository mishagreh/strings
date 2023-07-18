# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: function
# Length of the longest word: 8

def longest_word_length(words):
    longest = max(words, key=len)
    return longest, len(longest)


s = 'Write a Python function that takes a list of words and return the longest word and the length of the longest one.'
words = s.split(' ')
print(longest_word_length(words))

# solution
#
# def find_longest_word(words_list):
#     word_len = []
#     for n in words_list:
#         word_len.append((len(n), n))
#     word_len.sort()
#     return word_len[-1][0], word_len[-1][1]
