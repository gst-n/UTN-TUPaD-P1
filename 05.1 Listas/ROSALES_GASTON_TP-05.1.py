#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.

#lista =[]
#for i in range(1, 101):
#    i+=1
#    lista.append(4*i)
#print(lista)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

#mis_juegos = ['Red dead redemption', 'PUBG', 'GTA V', 'Elder Ring', 'Howarts Legacy']
#print(mis_juegos[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo:

#lista_vacia = []

#while len(lista_vacia)<3:
#    palabra = input('ingrese una palabra para la lista de palabras: ')
#    lista_vacia.append(palabra)
#    print(len(lista_vacia))
#print(lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!

#animales = ["perro", "gato", "conejo", "pez"]
#animales[1] = "Loro"
#animales[-1] = "Oso"
#print(animales)



#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
#numeros = [8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print(numeros)
#Al ejecutar este algoritmo, primero se define una lista con numeros aleatorios
#el metodo remove se utiliza para eliminar un objeto de la lista
#el metodo max, elimina el maximo numero de la lista, al ser ingresado
#como argumento.
#al imprimir por pantalla veremos la lista [8,15,3,7] sin el numero 22

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros

#lista=[]
#for i in range(10, 31,5):
#    lista.append(i)
#print(lista[:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.

#autos = ["sedan", "polo", "suran", "gol"]
#autos[1]="BMW"
#autos[2]='Hyundai'
#print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

#dobles = []
#for i in range(5,16,5):
#    dobles.append(2*i)
#print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
#["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a)
#compras[2].append('jugo')
#b)
#compras[1][1]= 'Tallarines'
#c)
#compras[0].remove('pan')
#d)
#print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_enteros=[]
lista_flotantes=[]
lista_booleanos=[]
lista_anidada = [lista_booleanos, lista_enteros, lista_flotantes]

lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada[1]= 15
lista_anidada[0]= True
lista_anidada[0]= False


print(lista_anidada)