# -*- coding: utf-8 -*-
import serial
ser = serial.Serial('/dev/pts/3')
print(ser.portstr)
print "'*** CALCULADORA ***\n"
n1 = raw_input("Digite o primeiro número: ")
while True:
	n2 = int(raw_input("Digite o segundo número: "))
	if(n2 != 0):
		break
while True:
	oper = raw_input("Digite o operador (+, -, *, /): ")
	if(oper == '+' or oper == '-' or oper == '*' or oper == '/'):
		break
ser.write(n1 + ";" + str(n2) + ";" + oper + ";" + "\n")
print "Dados Enviados\n"
cli = ser.readline()
print "Reposta: " + cli
ser.close()
