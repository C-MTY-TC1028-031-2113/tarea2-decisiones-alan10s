
def main():
    pass

edad = int(input("Ingresa tu edad: "))
if edad<18:
    	print('No cumples con los requisitos')
	
elif edad>=18:
	INE=str(input('¿Tienes identificación? '))
	
	if INE=='s': 
		print('Trámite de licencia concedido')
	
	elif INE=='n':
		print('No cumples con los requisitos')
		
	else:
		print('Respuesta incorrecta')
		
else:
	print('Respuesta incorrecta')


if __name__ == '__main__':
    main()
