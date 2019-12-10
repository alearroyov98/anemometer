import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN)
counter = 0
previous = 0
seconds = 0
flag = 0
# ser = serial.Serial(
#   
#     port='/dev/ttyS0',
#     baudrate = 9600,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=1
# )
def falling_edge(channel):
    global flag
    global current
    flag = 1
#     print (seconds)    
    current = time.time()
#     seconds = current - previous
#     previous = current
    
# when a falling edge is detected on port 5, regardless of whatever   
# else is happening in the program, the function falling_edge will be run  
GPIO.add_event_detect(5, GPIO.FALLING, callback=falling_edge, bouncetime=300) 
# while a < 200:
#     if GPIO.input(5):
#         print("HIGH")
#     else:
#         print("LOW")
#     time.sleep(0.025)
#     a=a+1

# counter=0
# clear=b'\xFE\x01'
# ser.write(clear)
while 1:
    if flag == 1:
        seconds = seconds + (current - previous)
        previous = current
        counter = counter + 1
        flag = 0
    if counter == 10:
        seconds = seconds/counter
        speed = (1/seconds)*2.5*0.44704
        print("%4.2f m/s" % speed)
        seconds = 0
        counter = 0
#     ser.write(clear)
#     ser.write(('Write counter:  %d'%(counter)).encode('utf-8'))
#     time.sleep(1)
#     counter += 1
#     print('Write counter:', counter)
