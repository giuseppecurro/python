#!/usr/bin/env python
import json
import gspread
import time
import datetime
from oauth2client.client import SignedJwtAssertionCredentials
json_key = json.load(open('../temper-6c9aee0dfa88.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
wks = gc.open("w1").sheet1
val = wks.acell('A1').value
print val,"in A1"
val = input('Immetti un valore da porre in A2: ')
wks.update_acell('A2', val)
print "=========================================="
cell_list = wks.range('A1:A3')
for cell in cell_list:
      print cell.value
print "Ultimo valore e' quello in A3 dove nel foglio viene calcolata la somma dei precedenti."
