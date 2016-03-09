from sense_hat import SenseHat
sense=SenseHat()
#import RPI.GPIO as GPIO
import time
import threading
durata_rosso=1
fermati=0

red = [255,255,0]
blue = [0,0,255]


def rosso(): 
           global durata_rosso
           global fermati
           while fermati==0:
             # GPIO.output(LedPin_rosso, GPIO)
             sense.set_pixel(4,4,red) 
             print durata_rosso
             time.sleep(durata_rosso)
             # GPIO.output(pixel_blue, GPIO.LOW)
             sense.set_pixel(4,4,blue)
             time.sleep(1)
              
def durata():
    global durata_rosso
    global fermati
    while fermati==0:
        try:
           durata_rosso= float (raw_input("clicca una lettera per terminare o inserisci la durata dell'accenzione del led"))
        
          #durata_rosso=comodo
           print('LED ACCESO',durata_rosso,'sec.- e spento per un sec.')
        except ValueError:
           print('avvio terminazione acquisizione da tastiera')
           fermati=1

r=threading.Thread(target=rosso)
d=threading.Thread(target=durata)
r.start()
d.start()
r.join()
#sense.clear()
print "GPIO resettato."
print "fine main."
