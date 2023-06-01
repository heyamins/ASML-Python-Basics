
s = r"""Python was conceived in the late 1980s[43] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[45] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life", a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[46] In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[47][48]

Python 2.0 was released on 16 October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 3.0, released on 3 December 2008, with many of its major features backported to Python 2.6.x[50] and 2.7.x. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[51]

Python 2.7's end-of-life was initially set for 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[52][53] No further security patches or other improvements will be released for it.[54][55] Currently only 3.7 and later are supported. In 2021, Python 3.9.2 and 3.8.8 were expedited[56] as all versions of Python (including 2.7[57]) had security issues leading to possible remote code execution[58] and web cache poisoning.[59]

In 2022, Python 3.10.4 and 3.9.12 were expedited[60] and 3.8.13, and 3.7.13, because of many security issues.[61] When Python 3.9.13 was released in May 2022, it was announced that the 3.9 series (joining the older series 3.8 and 3.7) would only receive security fixes in the future.[62] On September 7, 2022, four new releases were made due to a potential denial-of-service attack: 3.10.7, 3.9.14, 3.8.14, and 3.7.14.[63][64]

As of November 2022, Python 3.11 is the stable release. Notable changes from 3.10 include increased program execution speed and improved error reporting.[65]"""


# clean up

# s = s.lower().replace('.', '').replace(',', '').replace('(', '').replace(')', '')
#
# or
# s = s.lower().translate(str.maketrans('', '', '.,(){}[]/\|#&'))
#
# or
import string
s = s.lower().translate(str.maketrans('', '', string.punctuation + string.digits))

# or
# import re
# s = re.sub(r'[^a-zA-Z ]', '', s.lower())





words = s.split()

unique_words = set(words)

d = dict()
for word in unique_words:
    d[word] = words.count(word)


for word, n in sorted(d.items(), key = lambda item: item[1], reverse = True):

    print(f'{word:20}: {n:3} {"*" * n}')




# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#    print(f'{word:20}: {n:3} {"*" * n}')








# # or with a dict comprehension
# d = {word: words.count(word) for word in set(words)}

# for word, n in sorted(d.items()):
#     print(f'{word:20}: {n:3} {"*" * n}')

# from operator import itemgetter
# for word, n in sorted(d.items(), key = itemgetter(1, 0), reverse = True):
#    print(f'{word:20}: {n:3}')

# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#    print(f'{word:20}: {n:3} {"*" * n}')

# def get_values(item):
#     return item[1]
#
# for word, n in sorted(d.items(), key=get_values, reverse=True):
#     # print(word, n)
#     # print('%-25s: %3d' % (word, n))
#     print(f'{word:<25}: {n:3}')
#     # or
#     print('%-15s: %3d %s' % (word, n, '*' * n))



# # or with collection.Counter
# from collections import Counter
# d = Counter(s.lower().translate(str.maketrans('', '', string.punctuation)).split())
# print(d)