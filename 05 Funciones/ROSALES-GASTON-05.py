#Trabajo practico funciones.

import math

#1--------------------------

mensaje = 'Hola Mundo!'
#def imprimir_hola_mundo(mensaje):
#    print (mensaje)

#imprimir_hola_mundo(mensaje)

#2--------------------------
#def saludar_usuario(nombre):
#    print(f'Hola {nombre}')

#saludar_usuario("Marcos")

#3--------------------------

#def informacion_personal(nombre= input("ingrese su nombre: "), apellido=input('ingrese su apellido: '), edad=input('ingrese su edad: '), residencia=input('ingrese su residencia: ')):
#    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

#informacion_personal()

#4---------------------------

#def calcular_area_circulo(rad):
#    area_circulo = round(math.pi * math.pow(rad, 2))
#    return print(f'El area del circulo es: {area_circulo} unidades cuadradas.')

#calcular_area_circulo(42)

#5---------------------------
#def segundos_a_horas(num):
#    horas = round(num / 60)
#    return print(f'{num} segundos son: {horas} horas')
#segundos_a_horas(920)

#6---------------------------
#tabla = [1,2,3,4,5,6,7,8,9,10]
#def tabla_multiplicar(num):
#    for i in tabla:
#        tabla[i-1] = i*num 
#    return print(tabla)

#tabla_multiplicar(6)

#7----------------------------

#def operaciones_basicas(a,b):
#    suma=a+b
#    resta=a-b
#    mulpli=a*b
#    division=round(a/b)
#    tupla=[f'La suma es: {suma}',f'La resta es: {resta}',f'La mulplicación da: {mulpli}',f'La división da: {division}']
#    return tupla
#print(operaciones_basicas(2,3))

#8----------------------------- 
#def calcular_imc(peso=input("hola!"), altura=input("vamos a pedirte unos datos ->")):
#    peso = int(input("Ingrese el peso en Kilogramos: "))
#    altura = pow((float(input("Ingrese la altura en Metros: "))), 2)
#    imc = peso / altura
#    imc = round(imc, 2)
#    return print(imc)

#calcular_imc()

#9-------------------------------

#def celsius_a_farenheit():
#    celsius=int(input("Ingrese la temperatura en grados Celsius C°: "))
#    farenheit = (celsius * 9/5) + 32
#    return print(f'La temperatura en grados Farenheit es de: {farenheit}')

#celsius_a_farenheit()

#10----------------------------

#def calcular_promedio():
#    a=int(input("Ingrese un numero entero positivo: "))
#    b=int(input("Ingrese otro numero entero positivo: "))
#    c=int(input("Ingrese otro numero entero positivo: "))
#    promedio = round((a+b+c)/3)

#    return print(promedio)
#calcular_promedio()