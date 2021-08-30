def main():
    # Escribe el código adecuado para completar el programa
    x=int(input('Introduzca el primer número: '))
    y=int(input('Introduzca el segundo número: '))
    z=int(input('Introduzca el tercer número: '))

    if x==y and y==z:
    	print(x)
    	print(y)
    	print(z)
    
    elif x<=y and x<=z:
    	print(x)
    	if y<=z:
    		print(y)
    		print(z)
    	else:
    		print(z)
    		print(y)
    
    elif y<=x and y<=z:
    	print(y)
    	if x<=z:
    		print(x)
    		print(z)
    	else:
    		print(z)
    		print(x)
    
    elif z<=y and z<=x:
    	print(z)
    	if x<=y:
    		print(x)
    		print(y)
    	else:
    		print(y)
    		print(x)

if __name__=='__main__':
    main()
