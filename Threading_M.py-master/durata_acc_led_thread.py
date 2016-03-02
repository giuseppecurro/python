#!/usr/bin/env python
#nel componente "two color":  G=ground    R=red   Y=green
# Gestire in thread separati l'accensione del led e l'acquisizione da tastiera del valore durata dell'accensione.
# Si vuole che l'acquisione del nuovo valore consenta comunque il completamento precedentemente in corso.
# Sempre da tastiera si decida quando terminare i due thread.
# Finite le esecuzioni dei due thread venga garantito/ultimato il thread principale (main).
import RPi.GPIO as GPIO
import time
import threading
 
LedPin_rosso = 13    
GPIO.setmode(GPIO.BOARD)       # valga la disposizione fisica piedini Raspberry
GPIO.setup( LedPin_rosso, GPIO.OUT)   # piedino 13 in output
GPIO.output(LedPin_rosso, GPIO.LOW) # spento
durata_rosso = 0                      #secondi
fermati=0                            #acquisizione sara' consentita

def rosso():
    global durata_rosso              #global=comuni (main e thread)
    global fermati
    while fermati==0:   #0: il thread acquisizione "durata" funziona regolarmente
        GPIO.setup (LedPin_rosso, GPIO.OUT)   # uscita x led
        GPIO.output(LedPin_rosso, GPIO.HIGH)  # si accende led
        time.sleep (durata_rosso)           
        GPIO.output(LedPin_rosso, GPIO.LOW)
        time.sleep(1)                         # spento per un sec.

def durata():
        global durata_rosso
        global fermati
	while fermati==0:
	   try:
                comodo = float(raw_input("Una lettera per terminare oppure Durata rosso in secondi: "))
                durata_rosso = comodo
                print ('LED ACCESO ',durata_rosso,' sec. - e spento per un sec.')
           except ValueError:  # Se non  numero finisce il thread.
               print("Avvio terminazione acquisizione da tastiera.")
               fermati=1 #questo valore condiziona anche l'altro thread

r=threading.Thread(target=rosso)
d=threading.Thread(target=durata)
r.start()
d.start()
r.join() #Una volta terminato il  thread proseguire... 
GPIO.cleanup()     # Release resource
print "GPIO resettato."
print "Fine main." 
