Python: Everything is treated as OBJECT.

Class:
#--------
Class is the blue print or Template.
Class is Plan or Design 

Object:
#---------
Object is instance of Class.
Once the class is ready, we can create multiple objects based on the same class.
The physical existance of class is an Object

eg: Plan of the building is the blue print. So, the Plan is a class. 
    The buliding constructed according to the plan. so the building is object.

Reference Variable:
#---------------------
Reference variable is pointing to the object. By using this we can access properties and methods of class

eg: r1 is r2  #--> checks if both the reference variable are pointing to the same object or not

Self variable:
#---------------
Self is a keyword
Self is a reference variable which is always pointing to current boject
Within python class to refer to the current object we should use self variable.
For every constructor and instance method, first argument should be 'self'
BY using self we can declare and access the instance variable
PVM is responsible to provide value for self argument
The first argument in instance method and constructor will treat as self variable
Instead of 'self' variable we can use any name but its good if we use 'self' only

Constructor(__init__):
#------------------------
The name of the constructor is always be __init__() and We can't change the name of the constructor
Whenever we are creating an object this constructor will execute automatically and we are not required to call explicitly.
Main objective is to declare and initilalize of variables
For every object the constructor will execute once 
Every constructor should take atleast one argument that argument should be self then rest is the arguments
If we are not defining constructor then python will provide the default constructor

eg:
class Test():
    def __init__(self):
        print('constructor execution')
x = Test() 
y = Test()
z = Test()

Output: for every object constructor will execute.
    constructor execution
    constructor execution
    constructor execution
    
    
eg: 
class Demo:
"""This is the docstring which is document string"""
  def __init__(self):     #--> self always points to current object
    print(id(self))
x = Demo()
x1 = Demo()
print(id(x))  #--> Note: 'x' and 'self' both are pointing to the same object, then address of 'self' and 'x' should be same
print(id(x1)) #--> Note: self will points to the current object i.e. where the reference variable('x1') will points

NOTE: By using reference variable('x') we can access the object from outside the class
      By using 'self' variable we can access the object from inside of the class
      For every constructor and instance method, first argument should be 'self'

eg:
class Employee:
  def __init__(self, eno, ename):
    self.eno = eno
    self.ename = ename
    
  def info(self): #--> PVM is responsible to provide value for self argument because we r not passing any arugument while calling function
    print('Emp no: ', self.eno)
    print("Emp name: ', self.ename)

e = Employee()  #--> This will create the reference variable for Class Employee
e.info(10, 'Sita')  #--> calls the method of the class Employee. --> This one gives the value to constructor
