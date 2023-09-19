#Irene Stone
#Accessing thingSpeak from Thonny
#15th Sept 2023

import time
import serial
import urllib.request
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()
while True:
    data1 = str(ser.readline())
    data1 = data1.replace("b","")
    data1 = data1.replace("'","")
#    data1 = data1.replace("\\r\\n","")
    data1 = data1.replace("\\r", "").replace("\\n", "")  # Remove \r and \n
#    data1 = data1.replace("celsius:","")  #when using radio
    time.sleep(5)
    print(data1)
    msg = data1
      
    b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=BIZPFWPP6YGOAVHR&field1='+msg)

ser.close()
