import time
import network
from machine import Pin
import BlynkLib
from BlynkTimer import BlynkTimer
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Galaxy A12BF51","hbjf4876")
 
BLYNK_AUTH = '2iZiaYD7GZWpS-_kVw9YAfQuhAPyRcbg'
 
timer=BlynkTimer() 
 
# Wait for network connection
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    ip = wlan.ifconfig()[0]
    print('IP: ', ip)
 
# Connect to Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
 
# Initialize the relay and button pins
relay1_pin = Pin(19, Pin.OUT)
relay2_pin = Pin(18, Pin.OUT)
relay3_pin = Pin(17, Pin.OUT)
relay4_pin = Pin(16, Pin.OUT)
relay5_pin = Pin(20, Pin.OUT)
relay6_pin = Pin(21, Pin.OUT)
relay7_pin = Pin(22, Pin.OUT)
relay8_pin = Pin(26, Pin.OUT)
relay9_pin = Pin(27, Pin.OUT)
relay10_pin = Pin(28, Pin.OUT)
relay11_pin = Pin(15, Pin.OUT)
button1_pin = Pin(1, Pin.IN,Pin.PULL_UP)
button2_pin = Pin(2, Pin.IN,Pin.PULL_UP)
button3_pin = Pin(3, Pin.IN,Pin.PULL_UP)
button4_pin = Pin(4, Pin.IN,Pin.PULL_UP)
button5_pin = Pin(5, Pin.IN,Pin.PULL_UP)
button6_pin = Pin(6, Pin.IN,Pin.PULL_UP)
button7_pin = Pin(7, Pin.IN,Pin.PULL_UP)
button8_pin = Pin(8, Pin.IN,Pin.PULL_UP)
button9_pin = Pin(9, Pin.IN,Pin.PULL_UP)
button10_pin = Pin(10, Pin.IN,Pin.PULL_UP)
button11_pin = Pin(11, Pin.IN,Pin.PULL_UP)

 
# Variables State
relay1_state = False
relay2_state = False
relay3_state = False
relay4_state = False
relay5_state = False
relay6_state = False
relay7_state = False
relay8_state = False
relay9_state = False
relay10_state = False
relay11_state = False
button1_state = True
button2_state = True
button3_state = True
button4_state = True
button5_state = True
button6_state = True
button7_state = True
button8_state = True
button9_state = True
button10_state = True
button11_state = True
 
# Register virtual pin handler
@blynk.on("V1") #virtual pin V1
def v1_write_handler(value): #read the value
    global relay1_state
    relay1_state=int(value[0])
    relay1_pin.value(relay1_state)
    print('Virtual Switch 1 = ',relay1_state)

@blynk.on("V2") #virtual pin V2
def v2_write_handler(value): #read the value
    global relay2_state
    relay2_state=int(value[0])
    relay2_pin.value(relay2_state)
    print('Virtual Switch 2 = ',relay2_state)

@blynk.on("V3") #virtual pin V3
def v3_write_handler(value): #read the value
    global relay3_state
    relay3_state=int(value[0])
    relay3_pin.value(relay3_state)
    print('Virtual Switch 3 = ',relay3_state)

@blynk.on("V4") #virtual pin V4
def v4_write_handler(value): #read the value
    global relay4_state
    relay4_state=int(value[0])
    relay4_pin.value(relay4_state)
    print('Virtual Switch 4 = ',relay4_state)

@blynk.on("V5") #virtual pin V5
def v5_write_handler(value): #read the value
    global relay5_state
    relay5_state=int(value[0])
    relay5_pin.value(relay5_state)
    print('Virtual Switch 5 = ',relay5_state)
    
@blynk.on("V6") #virtual pin V6
def v6_write_handler(value): #read the value
    global relay6_state
    relay6_state=int(value[0])
    relay6_pin.value(relay6_state)
    print('Virtual Switch 6 = ',relay6_state)
    
@blynk.on("V7") #virtual pin V7
def v7_write_handler(value): #read the value
    global relay7_state
    relay7_state=int(value[0])
    relay7_pin.value(relay7_state)
    print('Virtual Switch 7 = ',relay7_state)
    
@blynk.on("V8") #virtual pin V8
def v8_write_handler(value): #read the value
    global relay8_state
    relay8_state=int(value[0])
    relay8_pin.value(relay8_state)
    print('Virtual Switch 8 = ',relay8_state)

@blynk.on("V9") #virtual pin V9
def v9_write_handler(value): #read the value
    global relay9_state
    relay9_state=int(value[0])
    relay9_pin.value(relay9_state)
    print('Virtual Switch 9 = ',relay9_state)

@blynk.on("V10") #virtual pin V10
def v10_write_handler(value): #read the value
    global relay10_state
    relay10_state=int(value[0])
    relay10_pin.value(relay10_state)
    print('Virtual Switch 10 = ',relay10_state)

@blynk.on("V11") #virtual pin V11
def v11_write_handler(value): #read the value
    global relay11_state
    relay11_state=int(value[0])
    relay11_pin.value(relay11_state)
    print('Virtual Switch 11 = ',relay11_state)
    
def physical_switch():
    global relay1_state,button1_state,relay2_state,button2_state,relay3_state,button3_state,relay4_state,button4_state,relay5_state,button5_state,relay6_state,button6_state,relay7_state,button7_state,relay8_state,button8_state,relay9_state,button9_state,relay10_state,button10_state,relay11_state,button11_state
    if button1_pin.value()==0: #physical pin P1
        if button1_state is not False:
            relay1_state = not relay1_state
            relay1_pin.value(relay1_state)
            blynk.virtual_write(1, relay1_pin.value())
            print('Physical Switch 1 = ',relay1_state)
        button1_state = False
    else:
        button1_state = True
    
    if button2_pin.value()==0: #physical pin P2
        if button2_state is not False:
            relay2_state = not relay2_state
            relay2_pin.value(relay2_state)
            blynk.virtual_write(2, relay2_pin.value())
            print('Physical Switch 2 = ',relay2_state)
        button2_state = False
    else:
        button2_state = True
    
    if button3_pin.value()==0: #physical pin P3
        if button3_state is not False:
            relay3_state = not relay3_state
            relay3_pin.value(relay3_state)
            blynk.virtual_write(3, relay3_pin.value())
            print('Physical Switch 3 = ',relay3_state)
        button3_state = False
    else:
        button3_state = True
    
    if button4_pin.value()==0: #physical pin P4
        if button4_state is not False:
            relay4_state = not relay4_state
            relay4_pin.value(relay4_state)
            blynk.virtual_write(4, relay4_pin.value())
            print('Physical Switch 4 = ',relay4_state)
        button4_state = False
    else:
        button4_state = True
    
    if button5_pin.value()==0: #physical pin P5
        if button5_state is not False:
            relay5_state = not relay5_state
            relay5_pin.value(relay5_state)
            blynk.virtual_write(5, relay5_pin.value())
            print('Physical Switch 5 = ',relay5_state)
        button5_state = False
    else:
        button5_state = True
        
    if button6_pin.value()==0: #physical pin P6
        if button6_state is not False:
            relay6_state = not relay6_state
            relay6_pin.value(relay6_state)
            blynk.virtual_write(6, relay6_pin.value())
            print('Physical Switch 6 = ',relay6_state)
        button6_state = False
    else:
        button6_state = True
        
    if button7_pin.value()==0: #physical pin P7
        if button7_state is not False:
            relay7_state = not relay7_state
            relay7_pin.value(relay7_state)
            blynk.virtual_write(7, relay7_pin.value())
            print('Physical Switch 7 = ',relay7_state)
        button7_state = False
    else:
        button7_state = True
        
    if button8_pin.value()==0: #physical pin P8
        if button8_state is not False:
            relay8_state = not relay8_state
            relay8_pin.value(relay8_state)
            blynk.virtual_write(8, relay8_pin.value())
            print('Physical Switch 8 = ',relay8_state)
        button8_state = False
    else:
        button8_state = True
        
    if button9_pin.value()==0: #physical pin P9
        if button9_state is not False:
            relay9_state = not relay9_state
            relay9_pin.value(relay9_state)
            blynk.virtual_write(9, relay9_pin.value())
            print('Physical Switch 9 = ',relay9_state)
        button9_state = False
    else:
        button9_state = True
        
    if button10_pin.value()==0: #physical pin P10
        if button10_state is not False:
            relay10_state = not relay10_state
            relay10_pin.value(relay10_state)
            blynk.virtual_write(10, relay10_pin.value())
            print('Physical Switch 10 = ',relay10_state)
        button10_state = False
    else:
        button10_state = True
        
    if button11_pin.value()==0: #physical pin P11
        if button11_state is not False:
            relay11_state = not relay11_state
            relay11_pin.value(relay11_state)
            blynk.virtual_write(11, relay11_pin.value())
            print('Physical Switch 11 = ',relay11_state)
        button11_state = False
    else:
        button11_state = True

timer.set_interval(1, physical_switch)
 
while True:
    blynk.run()
    timer.run()
