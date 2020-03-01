# -*- coding: utf-8 -*-
import serial
ser = serial.Serial('/dev/pts/3')
print(ser.portstr)
ser.write('Olá Mundo\n')
cli = ser.readline()
print cli
ser.close()
