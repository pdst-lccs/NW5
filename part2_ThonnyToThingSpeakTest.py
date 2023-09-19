#Irene Stone
#Accessing thingSpeak from Thonny
#Sept 2023

import urllib.request

number=input('Enter a number : ')
number = str(number)
b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=BIZPFWPP6YGOAVHR&field1='+number)
print("\nYour number has been sent!")
print(number)