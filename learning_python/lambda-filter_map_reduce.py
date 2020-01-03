Lambda:
##########
Lambda keyword is used to create anonymous functions. An anonymous function means that a function is without a name.

This function can have any number of arguments but only one expression, which is evaluated and returned.

syntax:
#########
lambda arguments : expression

Example:
###########

# Normal function
def cube(y): 
    return y*y*y;
cube(10)

# Lambda function
g = lambda x: x*x*x 
print(g(7)) 

# Without using Lambda :
##########################
while using def, we needed to define a function with a name cube and needed to pass a value to it. 
After execution, we also needed to return the result from where the function was called using the return keyword.

Using Lambda :
################
Lambda definition does not include a “return” statement, it always contains an expression which is returned.
We can also put a lambda definition anywhere a function is expected, and we don’t have to assign it to a variable at all. 


Lambda functions can be used along with built-in functions

a) filter() :
This function is used to filter out the elements according to the condition which we don't need it.
The filter() function takes in a function and a list as arguments. 
This offers an elegant way to filter out all the elements of a sequence “sequence” 
and gives or returns sequence, for which the function returns True. 

syntax: filter(function, list)

Example:
# Here is a small program that returns the odd numbers from an input list:
# Python code to illustrate 
# filter() with lambda() 

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)

Output: [5, 7, 97, 77, 23, 73, 61]


b) map() :
In this function applies some operations to the values, eg: add +2 to all the elements or double the elements
The map() function takes in a function and a list as argument. 
The function is called with a lambda function and a list and a new list is returned 
which contains all the lambda modified items returned by that function for each item.

syntax: map(function, list)

Example:
# Python code to illustrate  
# map() with lambda()  
# to get double of a list. 

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list)

Output: [10, 14, 44, 194, 108, 124, 154, 46, 146, 122]


c) reduce() :
This functions is used to get one value from out of chunk of values, eg: sum or multiple of all the elements, etc
The reduce() function takes in a function and a list as argument. 
The function is called with a lambda function and a list and a new reduced result is returned. 
This performs a repetitive operation over the pairs of the list. This is a part of functools module. 

Example:

# Python code to illustrate  
# reduce() with lambda() 
# to get sum of a list

from functools import reduce

li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 
Output: 193
