# Threading with the use of function
# Threading is module and Thread is class name
# Threading : Divide the program into multiple tasks, and run tasks (threads) at the same time
""" Advantage of threading: a. increase the execution speed of program 
b. when execution jobs are individual, then we can prefer multithreading 
c. Performance of the program will increase """

# import Thread class from threading module
from threading import Thread

print("Current Execution thread: ", threading.current_thread().getName()) # Gives the name of current running Thread
print("Current Execution thread: ", threading.current_thread().setName('Priyanka') # Sets the name of current running Thread
      
# To get the name of the thread
t.getName() # t is thread obj
'or'
t.name

# To set the name of the Thread 
t.setName("Priyanka") 
'or' 
t.name = 'Priyanka' 
    
try:
    thread = Thread(target=func_name, args=(func_name_arg1, func_name_arg2)) # args always be in tuple
    thread.start()
    thread.join()
    for each_thread in thread_list:
        if each_thread.is_alive():
            print("INFO: Exhausted the defined timeout value, "hence terminating the process which is still alive")
            thread.kill()
            logging.info("Execution of all the commands in  " + ip + " is completed \n")
except thread.ThreadError as thread_err:
    logging.error("Encountered issue while closing child thread(s): %s" % thread_err)
except threading.RuntimeError as run_thread_err:
    logging.error("Cannot join thread before it is started: %s" % run_thread_err)
except Exception as mthread_err:
    logging.error("Encountered new issue while closing child thread(s): %s" % mthread_err)
    
      
""" 1. Creating thread without using any Class (Functional oriented Way) """
def display(): # this one take care by child thread
    for i in range(10): 
        print("child Thread: %s" % i)
                  
# Gives the active Thread count
print("The no of active Threads: ", active_count())
                  
# Enemurate: list out all active threads current running and gives the information of that particular thread for Child Thread
l = enumerate()
for x in l:
    print("Thread Name: ", x.name) 
    print("Thread Identification no: ", x.ident)
                  
t = Thread(target=display) # it 't' is the thread object, creating thread object to execute display function
t.start() # when main thready execute this line, after that child thread and main thread both will start simultaneously
                  
# below is the main thread execution
for i in range(5): # this for loop will taken care by main thread
    print("Main thread: %s" % s)

# Enemurate Method: list out all active threads current running and gives the information of that particular thread for Main thread
l = enumerate()
for x in l:
    print("Thread Name: ", x.name) 
    print("Thread Identification no: ", x.ident)
                  

""" 2. Creating thread with using any class (By Extending Thread Class) """
class MyThread(Thread):
# pre-defined method run is instance method, the name of method is always fixed because we have to override. 
# It is predefined func present in Thread class
    def run(self):                 
        for i in range(10):
            print("child thread")
t = MyThread()
t.start() # whenever start method get called, internally start method will call the run method

# below main thread
for i in range(5):
    print("Main Thread")
                  
""" 3. Without using Extending Class """
class Test(): # Normal Test
    def m1(self):
        for i in range(10):
            print("Child Thread")
obj = Test()                  
t = Thread(target=obj.m1)
t.start()

# Below is the Main Thread
for i in range(5):
    print("main Thread")                  
               
             
# Python program to illustrate the concept of threading 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = Thread(target=print_square, args=(10,)) # args always be in tuple
    t2 = Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # Main Thread will wait until thread 1 is completely executed 
    t1.join() # Main thread will execute this line
    # main Thread wait until thread 2 is completely executed 
    t2.join() # main thread will execute this line
  # if we won't use join method then main thread will execute first which is print("Done!") then it will start for child thread.
  # The purpose of use join methods is main thread will wait until child thread completes execution
                  
    # both threads completely executed 
    print("Done!") 
    
    # To check the Thread Indentification Number
    print("Main Thread indentification No: %s" % current_thread().ident)
    print("Child Thread identification no: %s" % t.ident)
                  
                  
                  
                  
  
