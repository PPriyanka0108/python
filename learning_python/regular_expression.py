import re

# 1. Compile: It will return the object when we do re.compile()
# 2. finditer(): return an iterator. It will check the pattern in the given string
    # group() --> returned matched string
# Example:
# s1 = 'Blue Berries Blue Sky Blue Water'
# pattern = 'Blue'
# for match in re.finditer(pattern, s1):
#     s = match.start()
#     e = match.end()
#     print('\nString match "%s" at %d:%d' % (match.group(), s, e))
#     print('String match "%s" at %d:%d' % (s1[s:e], s, e))

# 4. Character Classes:
# -------------------------
    # a. [abc] ---> either a or b or c
    # b. [^abc] ---> expect a or b or c
    # c. [a-z] --> lower case alphabets
    # d. [A-Z] --> Upper case alphabets
    # e. [a-zA-Z] --> both lower and upper case alphabets
    # f. [0-9] --> Only digits
    # g. [0-9a-zA-Z] --> Alphanumeric
    # h. [^0-9a-zA-Z] --> Expect Alphanumeric
# # Example:
# for match in re.finditer('[^abc]', 'ashdkudbuhcskn'):
#     s = match.start()
#     e = match.end()
#     print('String match "%s" at %d:%d' % (match.group(), s, e))

# 5. Predefined Characters:
# --------------------------
    # \s --> space character
    # \S --> Expect space character
    # \d --> any digit
    # \D --> Except Digits
    # \w --> any word character i.e. alpha numeric character)
    # \W --> any character(special character) except word
    # . --> Every character

# 6. Quantifiers: The no.of occurences
# -------------------
    # a --> exactly one 'a'
    # a+ --> at least one 'a'
    # a* --> any no.of a's including zero number also
    # a? --> at most one 'a' or zero no. of 'a'
    # a{n} --> Exactly n no. of a's
    # a{m, n} --> Minimun m no.of a's and maximum n no. of a's
    # ^a --> Checks whether a starts with 'a' or not
    # a$ --> End the staring with 'a'

# # Example:
# for match in re.finditer('a', 'abaabaaab'):
#     s = match.start()
#     print('String match  will give exactly "a" %s at %d' % (match.group(), s))
# for match in re.finditer('a+', 'abaabaaab'):
#     s = match.start()
#     print('String match "a+" %s at %d' % (match.group(), s))
# for match in re.finditer('a*', 'abaabaaab'):
#     s = match.start()
#     print('String match "a*" %s at %d' % (match.group(), s))
# for match in re.finditer('a?', 'abaabaaab'):
#     s = match.start()
#     print('String match "a?" %s at %d' % (match.group(), s))
# for match in re.finditer('a{3}', 'abaabaaab'):
#     s = match.start()
#     print('String match "a{3}" %s at %d' % (match.group(), s))
# for match in re.finditer('a{2, 3}', 'abaabaaab'):
#     s = match.start()
#     print('String match "a{2, 3}" %s at %d' % (match.group(), s))
# for match in re.finditer('^a', 'abaabaaab'):
#     s = match.start()
#     print('String match "^a" %s at %d' % (match.group(), s))


# 6. RE functions:
# --------------------
# 1. match() :
# To check the given pattern is at the beginning of the string. if matches the it will return the object otherwise None
# # Example:
# m = re.match('abc', 'abcdefgh')
# if m != None:
#     print('Matching starting at begging of the string {}:{}'.format(m.start(), m.end()))
# else:
#     print('Patterns is not starting at beginning of the string')

# 2. fullmatch() :
# Total pattern with whole string. if matches the it will return the object otherwise None
# # Example:
# m = re.fullmatch('abc', 'abc')
# if m != None:
#     print('Matched full string {}:{}'.format(m.start(), m.end()))
# else:
#     print('Patterns is not fully matched string')


# 3. search(): Match object of the first occurence
# # Example:
# m = re.search('ab', 'abaabaaab')
# if m != None:
#     print('Matched first occurence of string {}:{}'.format(m.start(), m.end()))
# else:
#     print('Patterns is not matched string')

# 4. findall(): find all the elements and return as list
# # Example
# x = re.findall('[7-9]', '987872813shkfm')
# print(x)