# 12. Write a Python program to count the occurrences of each word in a given sentence.
import collections


def count_each_word(s: str) -> dict:
    return dict(collections.Counter(s.split()))


s = 'the quick brown fox jumps over the lazy dog.'
print(count_each_word(s))


# solution
#
# def word_count(str):
#     counts = dict()
#     words = str.split()
#
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     return counts



