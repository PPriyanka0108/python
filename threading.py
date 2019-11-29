# Threading with the use of function

import threading
import 
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
    
      
