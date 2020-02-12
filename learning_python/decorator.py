Decorator:
#############
Python decorator is a function that helps to add some additional functionalities to an already defined function. 
It is very helpful to add functionality to a function that is implemented before without making any change to the original function.
Decorator is very efficient when want to give an updated code to an existing code.

Python Decorator Basic Structure
#####################################
# example of decorator
# here the 'func' is the actualFunction'
def sampleDecorator(func):
    def addingFunction():
        # some new statments or flow control
        print("This is the added text to the actual function.")
        # calling the function
        func()

    return addingFunction


@sampleDecorator
def actualFunction():
    print("This is the actual function.")

# to call the function
actualFunction()

output:
########## 
This is the added text to the actual function.
This is the actual function.

Explanation:
###############
Whenever we call actualFunction, it will go to the def actualFunction, but before executing the this function it will go the sampleDecorator function.
In sampleDecorator function passes argument as 'actualFunction' function i.e. 'func'
Inside the sampleDecorator function we can declare the declare and call the 'func' inside the 'addinFunction' function.


# Python Decorator Example with single argument
####################################################

def flowerDecorator(vasel):
    def newFlowerVase(n):
        print("We are decorating the flower vase.")
        print("You wanted to keep %d flowers in the vase." % n)

        vasel(n)

        print("Our decoration is done")

    return newFlowerVase


# to call the decorator
@flowerDecorator
def flowerVase(n):
    print("We have a flower vase.")

# to call the function
flowerVase(6)


output:
##############
We are decorating the flower vase.
You wanted to keep 6 flowers in the vase.
We have a flower vase.
Our decoration is done

