#!/usr/bin/python

import socket
import calculadora2

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

try:
	while True:
		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
		print('HTTP request received:')
		peticion = str(recvSocket.recv(1024))
		
		operacion = peticion.split()[1]
		operacion = operacion.split("/")
		try:
			numero1 = int(operacion[1])
			numero2 = int(operacion[3])
		except ValueError:
			recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" + "Lo introducido no es un numero", 'utf-8'))
			mySocket.close()	
			
		operador = operacion[2]
		if operador == 'suma':
			resultado = calculadora2.suma(numero1, numero2)
		elif operador == 'resta':
			resultado = calculadora2.resta(numero1, numero2)
		elif operador == 'mult':
			resultado = calculadora2.mult(numero1, numero2)
		elif operador == 'div':
			resultado = calculadora2.div(numero1, numero2)
			if resultado == None:
				recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" + "<h1>Imposible dividir entre cero</h1>" + "\r\n", 'utf-8'))
				recvSocket.close()

		if resultado != None:
			html_answer = '<html><body><h1>'
			html_answer += (str(numero1) + " " + str(operador) + " " +  str(numero2) + " = " + str(resultado))
			html_answer += '</h1></body></html>'
			recvSocket.send(bytes("HTTP/1.1 200 OK \r\n\r\n" + html_answer + "\r\n", 'utf-8'))
			recvSocket.close()
		
except KeyboardInterrupt:
	print('\nClosing binded socket')
	mySocket.close()
