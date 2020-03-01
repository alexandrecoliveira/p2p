import serial
ser = serial.Serial('/dev/pts/4')
print(ser.portstr)
r = ser.readline()
print r
ser.write('Rx diz: Ola\n')
ser.close()
