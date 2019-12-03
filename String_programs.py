# Write a program to reverse the string
x = 'python' and output = 'nohtyp'

Way1: by using slicing method
y = x[::-1]
print(y) --> output : 'nohtyp'

Way2: by using reversed function
y = reveresed(x)  --> y is the object
output = ''.join(y) 
print(output) --> output : 'nohtyp'

Way3: using while loop
length = len(x) - 1
output = ''
while x >= 0:
  output = output + s[length]
  i -=1
print(output) --> output : 'nohtyp'

""" write a program to reverse the words in the statement """
x = 'python is easy languague'
output = 'languague easy is python'

# convert the string to list in split method
y = x.split() --> output: y = ['python', 'is', 'easy', 'language']

# now have to reverse the list by using slicing menthod
z = y[::-1] --> output: z = ['language', 'easy', 'is', 'python']

# now to convert the list to string by using join method
output = ' '.join(z) --> output: output = 'language easy is python'

"""write a program to reverse in letter of words in the statement"
x = 'python is easy languague'
output = 'nohtyp si ysae eugaugnal'

# convert the string to list in split method
y = x.split() --> output: y = ['python', 'is', 'easy', 'language']

# now reverse the letter of the word
l2 = []
for each in y:
  c = each[::-1]
  l2.append(c)
print(l2) --> output: l2 = ['nohtyp', 'si', 'ysae', 'egaugnal']

# now to convert the list to string by using join method
output = ' '.join(z) --> output: output = 'nohtyp si ysae eugaugnal'



