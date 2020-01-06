Inheritance
##############
To inherit the variables and methods from parent class to child by using child class object.
Inheritance increases reusability of a code. We don’t need to write the same code again and again. 
Inheritance it allows programmers to add more features to the existing a class.

Benefits:
###########
1.  It provides reusability of a code. We don’t have to write the same code again and again. 
    Also, it allows us to add more features to a class without modifying it.
2.  It is transitive in nature, which means that if class B inherits from another class A, 
    then all the subclasses of B would automatically inherit from class A.

Types Of Inheritance
#######################

a) Single Inheritance:
##########################
Single Inheritance means when a derived/sub/child class inherits from only one base/super/parent class.

example:
#########
class Parent():     # Parent class created 
    def parent_method(self):
      print('This is parent method')
      
 class Child(Parent):   # Child class created inherits from Parent class 
    def child_method(self):
      print('this is child method')
      
 obj = Child()            # Object or Reference variable of Child class  
 obj.parent_method ()     # To access Parent class method 
 obj.child_method  ()     # To access Child class method 
 
Output:
##########
 This is parent method 
 this is child method 
 
Explanation
##############
Child class inherit the properties of parent class. 
By using child class object we can call to parent class methods.
The methods present in Parent class are automatically available or inherits to the child class.
By using the reference variable or object of child class, we can call both class methods.

NOTE:
########
If the same method present in both parent and child classes,then Python will always consider the order of execution.
It will checks the methods of the child class, if it present then it will executes.
If method not present in the child class then it will go parent class and executes.

Example:
########
 class Parent():
    def parent_method(self):
      print('This is parent method')
      
 class Child(Parent):
    def child_method(self):
        print('this is child method')
        def parent_method(self):
          print('This is child class and parent method')
          
 obj = Child()
 obj.parent_method ()
 obj.child_method ()
  
output:
#########
 This is child  class and parent method 
 this is child method
 
 
b) Multiple Inheritance
############################
When a child class inherits the properties from multiple parent classes

Example:
###############
class Father():     # Parent1 class
    def  father_method(self):
      print('This is  father method')
      
class Mother():     # parent2 class
    def mother_method(self):
      print('This is mother method')
      
class Child(Father, Mother):      # child class inherits from Father and Mother classes  
    def child_method(self):
      print('this is child method')
      
 obj = Child() 
 obj.child_method()
 obj.father_method()
 obj.mother_method()
 
Output:
##########
 this is child method
 This is father method
 This is mother method
    
Example 2:
#############		
# definition of the class starts here  
class Person:  
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  
    #end of class definition  
  
# defining another class  
class Student: # Person is the  
    def __init__(self, studentId):  
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  
  
  
class Resident(Person, Student): # extends both Person and Student class  
    def __init__(self, name, age, id):  
        Person.__init__(self, name, age)  
        Student.__init__(self, id)  
  
  
# Create an object of the subclass  
resident1 = Resident('John', 30, '102')  
resident1.showName()  
print(resident1.getId())  

Output:
##########
John
102

Explanation:
##############
The classes Person and Student are superclass here and Resident is the subclass.
The class Resident extends both Person and Student to inherit the properties of both classes.

Example 3:
##############
class A:  
    def __init__(self):  
        self.name = 'John'  
        self.age = 23  
  
    def getName(self):  
        return self.name  
  
  
class B:  
    def __init__(self):  
        self.name = 'Richard'  
        self.id = '32'  
  
    def getName(self):  
        return self.name  
  
  
class C(A, B):  
    def __init__(self):  
        A.__init__(self)  
        B.__init__(self)  
  
    def getName(self):  
        return self.name  
  
C1 = C()  
print(C1.getName())  

output: Richard

Explanation:
#############
Class C inherits both A and B. And both of them has an attribute ‘name’. 
In the constructor of C, the first constructor called is the one of A. So, the value of name in C becomes same as the value of name in A.
But after that, when the constructor of B is called, the value of name in C is overwritten by the value of name in B.
So, the name attribute of C retains the value ‘Richard’ when printed. 

Note:
###########
The hierarchy becomes completely depended on the order of __init__() calls inside the subclass. 

c) Hierarchical Inheritance:
#############################
Inheriting properties from one parent class to multiple child classes.

Example:
###########

 class Parent:    # parent class
     father_name="father_name"
     mother_name="mother_name"
     def show_parent(self):
         print(self.father_name,self.mother_name)
         
 #Son class inherits Parent class
 class Son(Parent):     # child 1 class
     son_name="son"
     def show_child(self):
         print(self.son_name)
         
 #Daughter class inherits Parent class
 class Daughter(Parent):      #Child 2 class
     daughter_name="daughter_name"
     def show_daughter(self):
         print(self.daughter_name)
         
 son=Son()  # Object of Son class
 son.show_child()
 son.show_parent()
 
 daughter=Daughter()    # object to create daughter class
 daughter.show_daughter()
 daughter.show_parent()
 
 Output:
 #########
 output of the son:
 son
 father_name
 mother name
 
 output of daughter:
 daughter_name
 father_name
 mother_name
 
d) Multi-level Inheritance :
###############################
Inherits properties from Grandfather class to Father class and from Father class to sub child class.

Example:
###########
class Grandfather:
     def Grand_father(self):
         print("properties of Grand_father, grand Father class")
 class Father(Grandfather):
     # class Father inheriting property of class Grandfather
     def father(self):
         print("properties of garndFather, father class")
 class Child(Father):
     # class Child inheriting property of class Father
     def child(self):
         print("properties of Father, child class")
obj = Child()
obj.child()
obj.father()
obj.Grand_father()

output:
########
properties of Father, child class
properties of Father, father class
properties of grandfather, grand Father class


Method Resolution Order(MRO):
###############################
Programs that support multiple inheritance method resolution order plays a very crucial role.
The order in which the base classes are searched when executing a method. 
First, the method or attribute is searched within a class and then it follows the order we specified while inheriting. 
This order is also called Linearization of a class and set of rules are called MRO(Method Resolution Order). 
While inheriting from another class, the interpreter needs a way to resolve the methods that are being called via an instance. 
 
Example:
##########
# Python program showing 
# how MRO works 
  
class A: 
    def rk(self): 
        print(" In class A") 
class B(A): 
    def rk(self): 
        print(" In class B") 
  
r = B() 
r.rk() 

Output:
#############
in class B
order:- Class B --> Class A


Example2:
##############
class A: 
    def rk(self): 
        print(" In class A") 
class B(A): 
    def rk(self): 
        print(" In class B") 
class C(A): 
    def rk(self): 
        print("In class C") 
  
# classes ordering 
class D(B, C): 
    pass
     
r = D() 
r.rk() 

Output:
########
In class B
Order:- class D --> class B --> class c --> class A

	
Methods for Method Resolution Order(MRO) of a class:
######################################################
To get the method resolution order of a class we can use either __mro__ attribute or mro() method. 
By using these methods we can display the order in which methods are resolved. 

Example
#########
# Python program to show the order 
# in which methods are resolved 
  
class A: 
    def rk(self): 
        print(" In class A") 
class B: 
    def rk(self): 
        print(" In class B") 
  
# classes ordering 
class C(A, B): 
    def __init__(self): 
        print("Constructor C") 
  
r = C() 
  
# it prints the lookup order  
print(C.__mro__) 
print(C.mro())

Output:
#############
Constructor C
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

Example 2:
##############
class A:
    def process(self):
        print('A process()')


class B:
    pass


class C(A, B):
    pass


obj = C()  
obj.process()    
print(C.mro())   # print MRO for class C

output:
##########
A process()
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

Explanation:
#############
From MRO of class C, we get to know that Python looks for a method first in class C. Then it goes to A and then to B. 
So, first it goes to super class given first in the list then second super class, from left to right order. 
Then finally Object class, which is a super class for all classes.

Example 3:
###########
class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')

class C(A, B):
    pass

obj = C()
obj.process()


Output: A process()

Example 4:
#############
class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')


class C(A, B):
    def process(self):
        print('C process()')


class D(C,B):
    pass


obj = D()
obj.process()

print(D.mro())

Output:
#########
C process
[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


