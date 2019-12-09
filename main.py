import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN)
previous = 0
seconds = 0
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
    global previous
    global seconds
    print (seconds)    
    current = time.time()
    seconds = current - previous
    previous = current
    
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
# while 1:
#     ser.write(clear)
#     ser.write(('Write counter:  %d'%(counter)).encode('utf-8'))
#     time.sleep(1)
#     counter += 1
#     print('Write counter:', counter)
