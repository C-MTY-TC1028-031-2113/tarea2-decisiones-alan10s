import math
from math import sqrt

def main():
    # Escribe tu código abajo de esta línea
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    parentesis = ((b**2)-(4*a*c))

    if a == 0 and b == 0:
        print("No tiene solucion")
    elif a == 0 and b != 0:
        ecua3 = (-c/b)
        print(ecua3)
    elif a != 0 and b != 0:
        parentesis = ((b**2)-(4*a*c))
    if parentesis > 0:
        ecua1 = ((-b)+math.sqrt(b**2-4*a*c))/(2*a)
        ecua2 = ((-b)-math.sqrt(b**2-4*a*c))/(2*a)
        print("discriminante es: ", parentesis)
        print("la primera x es: ", ecua1)
        print("la segunda x es: ", ecua2)
    elif parentesis == 0:
        parentesisneg = -b/(2*a)
        print(parentesisneg)
    if parentesis < 0:
        print("Raices complejas")
    pass


if __name__ == '__main__':
    main()
