# Tre threads gestiscono ciascuno un contatore che si incrementa di volta in volta
# con valori casuali.
# Chi arrivera' per primo a 100?
# per avere il pid: ps aux | grep inc_var.py 
# per avere i threads attivi: ps -T <pid>
# top -H
#
# threads_inc.py
#
import threading
import random
import time
fineGara = False # consente un output finale piu pulito
class myThread (threading.Thread):
    def __init__(self, threadID, lock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.counter = 0
        self.lock = lock 
    def run(self):
        print "Starting thread: " , self.threadID
        self.gareggia();
    def gareggia(self):
             global fineGara
             while self.counter<=100:
                inc_var=random.randint(1, 6) #num.cas.da 1 a 6 compresi
                self.counter += inc_var
                self.lock.acquire() #completa una stampa
                if not fineGara:    #niente piu stampe per il secondo ed il terzo arrivato
                     print "Thread ", self.threadID, "\t=",self.counter,"\t\t[",inc_var,"]"
                self.lock.release()
                time.sleep(0.5)
             self.lock.acquire() 
             if not fineGara:          
                  print "Il thread ",self.threadID," ha vinto!\n"
             fineGara=True
             self.lock.release()
# Create new threads
lock = threading.Lock() #la risorsa stampa dovra essere bloccata per non avere output mischiati dei thread
t1 = myThread(1,lock)
t2 = myThread(2,lock)
t3 = myThread(3,lock)
print "threads starts..."
# Start new Threads
t1.start()
t2.start()
t3.start()
#
t1.join() #il main...
t2.join()
t3.join() #...non e' il caso che finisca prima dei thread secondari
print "Exiting Main Thread after all others threads"
