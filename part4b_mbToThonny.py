#Irene Stone
#Micro:bit to Thonny
#Sept 2023

import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"   #change the COM port
ser.open()
while True:
    data1 = str(ser.readline())
    data1 = data1.replace("b","")
    data1 = data1.replace("'","")
    data1 = data1.replace("\\r\\n","")
    time.sleep(5)
    print(data1)

ser.close()
