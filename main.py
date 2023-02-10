
from os import system
from random import randint

limiteIntentos = 8
salir = False
ganaste = False
numAdivinar = randint(0, 100)   # Incluye el segundo parametro tambien, (otros lo excluyen)

nombre = input("Ingrese su nombre: ");
intentos = 0;


while salir != True:
    print("\t\t\tJugando: ", nombre)
    print("\t\t\tIntentos ", intentos, " de ", limiteIntentos)
    numero = int(input("Ingrese un numero: "))
    if(numero == numAdivinar):
        salir = True
        ganaste = True
    elif(numero < 0 or numero > 100):
        print("El numero marcado no esta entre 0 y 100")
    elif(numero < numAdivinar):
        print("El numero marcado es menor al buscado")
    elif(numero > numAdivinar):
        print("El numero marcado es mayor al buscado")
    intentos += 1
    if(intentos == limiteIntentos):
        salir = True
    input()
    system("cls") # Para limpiar la consola

if(ganaste):
    print("Adivinaste el numero ", numAdivinar, " en ", intentos, " intentos")
else:
    print("Perdiste el numero era ", numAdivinar)