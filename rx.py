# -*- coding: utf-8 -*-
import serial
ser = serial.Serial('/dev/pts/4')
print(ser.portstr)
r = ser.readline()
dados = r.split(";")
print dados
ser.write("FIM\n")
ser.close()
