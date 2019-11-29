" DEAMON THREAD '
# Deamon_threads : Background execution threads are considered as Deamon Threads. 
# The main purpose of Deamon threads to provides the support for non-deamon threads
""" eg: Garbage Collector (for memory relates issues) --> it run in the background.
Assume, main thread executing, suddendly main thread is facing Memory problem then PVM executes Garbage collector
Garbage Collector destroies some useless objects and it free the space. Now main thread will execute smoothly 
If main Thread facing any problem then immediately garbage Collector will provide the same free space to the main thread """

'Advantage: Whenever last non-deamon terminates automatically all deamon threads will be terminated, we not required to terminate explicitly'
# Check whether the thread is deamon or not
t.isDeamon() 'or' t.deamon

# program1
from threading import *
mt = current_thread() # this is main thread which runs in the foreground, so it not a deamon thread
print(mt.isDeamon()) # output: false
print(mt.deamon) # output: false

'''main thread already started, now we can't change the deamon nature.
Below: Trying to Change the main thread to deamon thread, so through error like runtimeError ''' 
mt.setDeamon(True) 

# Change the deamon nature of thread by using below command 
t.setDeamon(True) # so 't' will become the deamon thread i.e. runs in the background
t.setDeamon(false) # 't' will become non-deamon thread 

""" NOTE: If we want to change the deamon nature, before starting of the thread we have to change.
Once thread started we can't change deamon nature of active thread.
If want to change the deamon nature of running thread then it will through the RuntimeError 'cannot set Deamon status of active thread'"""

''' NOTE: Deamon nature of child thread is inherts from the parent thread ie. if Parent is Deamon then child will become deamon ''' 

# proram 2 to check for Deamon nature of child Thread
def job1():
  print("execution completed of job1")
  t2 = Thread(target=job2)
  print('t2 is deamon:', t2.isDeamon()) # output: True. SetDeamon as True in 't1', if t1 is deamon then t2 also deamon
  t2.start()
  t3 = thread(target=job3)
  t3.setDeamon(False)
  print('t3 is deamon:', t3.isDeamon()) # output: False. making setDeamon as False. 't3' is non-Deamon
  
  t3.start()
  
def job2():
  print("execution completed of job2")
def job3():
  print("execution completed of job 3")
t1 = Thread(target=job1)
t1.setDeamon(True) # # Once we set t1 as True so t1 become deamon
print('t1 is deamon', t1.isDeamon()) # output: True
t1.start()
