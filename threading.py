# Threading with the use of function
# Advantage of threading: a. increase the execution speed of program b. when execution jobs are individual, then we can prefer multithreading 

import threading

print("Current Execution thread: ", threading.current_thread().getName()) # Gives the name of current running Thread
try:
    thread = threading.Thread(target=func_name, args=(func_name_arg1, func_name_arg2))
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
    
      
# 1. Creating thread without using any Class
def display(): # this one take care by child thread
    for i in range(10): 
        print("child Thread: %s" % i)
t = threading.Thread(target=display) # it 't' is the thread object, creating thread object to execute display function
t.start() # when main thready execute this line, after that child thread and main thread both will start simultaneously
                  
# below is the main thread execution
for i in range(5): # this for loop will taken care by main thread
    print("Main thread: %s" % s)
