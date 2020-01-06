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
 obj.father_method()
 obj.mother_method()
 obj.child_method()
 
Output:
##########
 this is child method
 This is father method
 This is mother method
 
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
         
output:
########
properties of Father, child class
properties of Father, father class
properties of grandfather, grand Father class

