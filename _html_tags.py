# 15. Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def html_tags(tag, word: str) -> tuple:
    return f'<{tag}>{word} </{tag}>', '<{0}>{1} </{0}>'.format(tag, word), "<%s>%s</%s>" % (tag, word, tag)


tag, word = 'b', 'Python Tutorial'
print(html_tags(tag, word))


# solution
#
# def add_tags(tag, word):
# 	return "<%s>%s</%s>" % (tag, word, tag)
# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python Tutorial'))
