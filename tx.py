# -*- coding: utf-8 -*-
import serial
ser = serial.Serial('/dev/pts/3')
print(ser.portstr)
print "'*** CALCULADORA ***"
n1 = raw_input("Digite o primeiro número: ")
n2 = raw_input("Digite o segundo número: ")
oper = raw_input("Digite o operador (+, -, *, /): ")
ser.write(n1 + ";" + n2 + ";" + oper + ";" + "\n")
print "Dados Enviados"
cli = ser.readline()
print "Reposta: " + cli
ser.close()
