Generator: 
1. If we want any sequence of values
2. If we are using yield keyword in the function, then that function will treat as 'Generator'
3. Produces an item once at a time and when it required. And run along with 'for' loop

Advantage:
1. Easy to implement like by using the methods __iter__() and __next__()
2. Memory utlization will be better than other datatypes(lists) and performance will be improved. 
3. A normal function to return a sequence will create the entire sequence in memory before returning the result.
This is an overkill if the number of items in the sequence is very large.
Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time.

Generator Function: 
A generator-function is same as normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function.
Note: next() ---> use in Python 2.7 and __next__() use in Python 3
Note: eg: next(obj_name) in 2.7 and obj_name.__next__() 
eg: def mygen():
      yield 'A'
      yield 'B'
g = mygen()

print(type(g))  # output -- generator
print(next(g))  # output - get the first value i.e. A
print(next(g)) # output - next value i.e. A B
print(next(g)) # output - next value is not there, so will get error like 'StopIteration'

eg:) def topten():
        n = 1
        while n <=10:
          yield n
          n +=1
          
obj = topten()

for i in obj:
  print(i)
  
Q) Differences between Generator function and a Normal function
--> Generator function contains one or more yield statement.
--> When called, it returns an object (iterator) but does not start execution immediately.
--> Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
--> Once the function yields, the function is paused and the control is transferred to the caller.
--> Local variables and their states are remembered between successive calls.
--> Finally, when the function terminates, StopIteration is raised automatically on further calls.


Eg: A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
    
>>> # It returns an object but does not start execution immediately.
>>> a = my_gen()
>>> # We can iterate through the items using next().
>>> next(a)
This is printed first
1
>>> # Once the function yields, the function is paused and the control is transferred to the caller.
>>> # Local variables and theirs states are remembered between successive calls.
>>> next(a)
This is printed second
2
>>> next(a)
This is printed at last
3
>>> # Finally, when the function terminates, StopIteration is raised automatically on further calls.
>>> next(a)
Traceback (most recent call last):
...
StopIteration
>>> next(a)
Traceback (most recent call last):
...
StopIteration
