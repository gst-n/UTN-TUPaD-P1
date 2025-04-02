#Actividades
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese por favor su edad: "));

if (edad > 18):
    print("Es mayor de edad");

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota_alumno = int(input("Ingrese la nota del alumno: "))

if (nota_alumno > 6):
    print("Aprobado");
else:
    print("Desaprobado");

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero par: "));

if numero%2==0:
    print("Ha ingresado un número par");
else:
    print("Por favor, ingrese un numero par");

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese por favor su edad: "));

if (edad >=0 and edad <= 12):
    print("Niño/a")
elif edad >= 12 and edad<=18:
    print("Adolescente")
elif (edad >= 18 and edad< 30):
    print("Adulto joven")
else:
    print("Adulto")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = (input("Ingrese una contraseña entre 8 y 14 caracteres: "))

if (len(contraseña)>8 and len(contraseña)<14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

from statistics import mode, median, mean;
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)

if (media > mediana and media > moda):
    print("Sesgo positivo")
elif (media < mediana and   mediana < moda):
    print("Sesgo negativo")
else: 
    print("no hay sesgo")

print(f"Los datos fueron:  media: {media}, moda: {moda}, mediana: {mediana}")
print(f"los numeros aleatorio fue: {numeros_aleatorios}")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.


palabra = input("Ingrese una frase o palabra: ")
vocales = "aeiou"

if palabra[-1] in vocales:
    palabra+= '!'
    print(palabra)
else:
    print("no termina en vocal")


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro")
opcion = int(input("Ingrese una de las opciones anteriores: "))

if opcion == 1:
    print(nombre.upper())
elif opcion==2:
    print(nombre.lower())
else:
    print(nombre.capitalize())

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto = int(input("Ingrese la magnitud del terremoto: "))

if (magnitud_terremoto < 3):
    print("Muy leve")
    print( 'imperceptible')
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve")
    print("ligeramente perceptible")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado")
    print("sentido por personas, pero generalmente no causa daños")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte")
    print('puede causar daños en estructuras débiles')
elif magnitud_terremoto >= 6 and magnitud_terremoto <7:
    print("Muy fuerte")
    print("puede causar daños significativos")
elif magnitud_terremoto >= 7:
    print("Extremo")
    print("puede causar graves daños a gran escala")