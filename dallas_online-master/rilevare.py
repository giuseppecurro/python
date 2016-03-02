import os, glob, time
import json
import gspread
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                return temp_c
from oauth2client.client import SignedJwtAssertionCredentials
json_key = json.load(open('../temper-6c9aee0dfa88.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
wks = gc.open("w1").sheet1
wks.resize(3)
try:
      while True:
            t=read_temp()
            print(t)
            time.sleep(7.0)
            #wks.update_acell('C2', t)
            wks.append_row(['t=',t])
except KeyboardInterrupt:
     print "Fine esecuzione!!!"



