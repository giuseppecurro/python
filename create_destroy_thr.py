# Code to execute in an independent thread
import time
def countdown(n):
   while n > 0:
       print('T-minus', n)
       n -= 1
       time.sleep(1)
#
# Create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()
# Main wants to know if thread is working
if t.is_alive():
    print('\n1. thread still running')
else:
    print('Completed')
#
t.join(7) #main has to wate threads (7 sec max)
#
# Main wants to know if thread is working
if t.is_alive():
    print('\n2. thread still running')
else:
    print('\nThread Completed')
print ('\nMain Completed')
