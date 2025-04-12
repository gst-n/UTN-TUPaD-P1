#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#for i in range (0,100+1,1):
#    print(i, end=' ')

##############################################

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene

#numero = int(input('Ingrese un numero entero a continuación: '))
#print(f'El numero ingresado contiene  {len(str(numero))} digitos')

##############################################

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#numero1 = int(input('Ingrese un numero entero mayor que 0: '))
#numero2 = int(input('Ingrese otro numero entero mayor que 0: '))
#suma=0
#for i in range(numero1+1, numero2):
#    print(f'el valor de index es {i}')
#    suma +=i
#    #print(f'La suma total entre los valores {i} y {i} = {suma}')    
#print(f'La suma total de los numeros entre los valores {numero1+1} y {numero2} es = {suma}')

##############################################

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

#numero = int(input('Ingrese un numero entero positivo o presione 0 para finalizar: '))
#suma=0
#while numero != 0:
#    suma += numero
#    numero = int(input('Ingrese otro numero entero positivo o presione 0 para finalizar: '))
#print(f'La suma total de los numeros ingresados en secuencia es {suma}')

##############################################

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#import random
#intentos = 0
#numero_incog = random.randint(0,9)
#numero = int(input('Ingrese un numero entero positivo: '))

#while numero_incog != numero:
#    intentos = intentos+1
#    numero = int(input('Ingrese otro numero entero positivo: '))
#    #print(f'El numero ingresado es incorrecto. Llevas {intentos} intentos')
#print(f'FELICITACIONES. Te tomo {intentos} intentos adivinarlo')

##############################################

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

#for i in range(0,100+1, 2):
#    print(i, end=' ')

##############################################

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

#numero = int(input('Ingrese un numero entero mayor que 0: '))
#suma=0

#for i in range(0, numero+1):
#    suma+=i
#print(f'La suma total de los numeros entre 0 y {numero} es {suma}')

##############################################

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#definimos primero las variables a utilizar
#contador = 0
#esPar=0
#esImpar=0
#en este caso el contador se prueba con 10 variables
#while contador <= 100 :
#    numero = int(input('Ingrese un numero entero: '))
#    #si el numero es par, la variable esPar aucumulara +1
#    if numero % 2 == 0:
#        esPar+=1
#    else:
#        esImpar+=1
#    contador+=1
#print(f'La cantidad de numeros pares fueron: {esPar}. Y la cantidad de impares fueron: {esImpar}')

##############################################

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor)

#contador=0
#numeros_ingresados=0
#suma=0
#while contador < 10 :
#    numero = int(input('Ingrese un numero entero: '))
#    suma+=numero
#    numeros_ingresados+=1
#    contador+=1
#print(f'La suma total de los numeros ingresados fue {suma}, y la cantidad {numeros_ingresados}.')
#print(f'La media es de {suma/numeros_ingresados}')

##############################################

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#numero = int(input('Ingrese un numero entero positivo: '))
#cadena = str(numero)
#longitud = len(cadena)
#inversa = ''
#Manera alternativa de revertir un string
#print(cadena[::-1])
#while longitud>0:
#    inversa += cadena[longitud-1]
#    longitud-=1
#print(f'El numero original ingresado es {numero}. Y la cadena inversa es {inversa}')
