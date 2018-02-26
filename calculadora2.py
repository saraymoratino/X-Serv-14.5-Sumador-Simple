#Saray Moratino Sousa
#!/usr/bin/python3

import sys
import socket

def suma(n1, n2):
	return n1 + n2
def resta(n1,n2):
	return n1 - n2
def mult(n1,n2):
	return n1 * n2
def div(n1,n2):
	try:
		return n1 / n2
	except ZeroDivisionError:
		print ("Division no valida.")
 
	
if __name__ == "__main__":
	

	NUM_ARGS = 4

	if len(sys.argv) != NUM_ARGS:
		print("Numero de argumentos erroneos")
		sis.exit

	operacion = sys.argv[1]
	try:
		num1 = int(sys.argv[2])
		num2 = int(sys.argv[3])
	except ValueError:
		print("Algun operando incorrecto.")
		sys.exit
		
	if operacion == 'suma':
		resultado = suma(num1, num2)
		print (str(num1) + " + " + str(num2) + " = " + str(resultado))
	elif operacion == 'resta':
		resultado = resta(num1, num2)
		print (str(num1) + " - " + str(num2) + " = " + str(resultado))
	elif operacion == 'mult':
		resultado = mult(num1, num2)
		print (str(num1) + " * " + str(num2) + " = " + str(resultado))	
	elif operacion == 'div':
		resultado = div(num1, num2)
		print (str(num1) + " / " + str(num2) + " = " + str(resultado))
	else:
		print ("Operador incorrecto")
		sys.exit
