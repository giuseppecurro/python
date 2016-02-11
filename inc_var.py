# Tre threads gestiscono ciascuno un contatore che si incrementa di volta in volta
# con valori casuali.
# Chi arrivera' per primo a 100?
# per avere il pid: ps aux | grep inc_var.py 
# per avere i threads attivi: ps -T <pid>
# top -H
import threading
import random
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        self.gareggia();
        print "Exiting " + self.name
    def gareggia(self):
        global exitFlag
        while self.counter<=100 and exitFlag==1:
                inc_var=random.randrange(1, 7, 1)    
        	self.counter = self.counter+inc_var
                print self.name, self.counter, "     (",inc_var,")"
                time.sleep(1)
        print self.name+" Ha finito!!!"
        exitFlag = 1

# Create new threads
thread1 = myThread(1, "Thread-1", 0)
thread2 = myThread(2, "Thread-2", 0)
thread3 = myThread(3, "Thread-3", 0)
# Start new Threads
thread1.start()
thread2.start()
thread3.start()
print "Exiting Main Thread"
