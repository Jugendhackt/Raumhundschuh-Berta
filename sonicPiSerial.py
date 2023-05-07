
from pythonosc import osc_message_builder
from pythonosc import udp_client
import serial
import sys
import time

comport = input("Calliope COM?\n")
#select the correct port and baud rate 
ser = serial.Serial('COM'+comport, 115200)

sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

while True:
    try:
        ser_bytes = ser.readline()
        serialVal = str(ser_bytes, 'ascii').strip()
        print(serialVal)
        if serialVal=='ente':
            sender.send_message('/Handschuh/Ente', [1])
        else:
            list=serialVal.split(',')
            message=[int(item) for item in list]
            sender.send_message('/Handschuh/beschleunigung/h', message)

        
    except:
        print(sys.exc_info()[0])
        break