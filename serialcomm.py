import serial
import time
import tkinter as tk

with serial.Serial('COM4', 9600) as ser:   
    #x = ser.readline().decode('utf-8') 
    #print(x)
    #ser.write('1'.encode())
    #y = ser.readline().decode('utf-8')
    #print(y)
    while True:
        meep = ser.in_waiting
        time.sleep(.5)
        hello = ser.in_waiting
        if hello > meep:
            print('data')
            time.sleep(.5)
        
            
    ser.close()

