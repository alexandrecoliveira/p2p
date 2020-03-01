# -*- coding: utf-8 -*-
import serial
ser = serial.Serial('/dev/pts/4')
print(ser.portstr)
r = ser.readline()
dados = r.split(";")
if(dados[2] == '+'):
	r = int(dados[0]) + int(dados[1]) 
elif(dados[2] == '-'):
	r = int(dados[0]) - int(dados[1]) 
elif(dados[2] == '*'):
	r = int(dados[0]) * int(dados[1])
else:
	r = int(dados[0]) / int(dados[1])

print r
ser.write(str(r) + '\n')
ser.write("FIM\n")
ser.close()
