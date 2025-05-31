###
###
#1.----------------------------
# def func_factorial(num):
#     if num ==0:
#         return 1
#     else:
#         return num * func_factorial(num-1)

# def factorial_entre(num):
#     for i in range(1, num+1):
#         print(f'Func_fact de i: {i} ---> { func_factorial(i)}')

# factorial_entre(4)

#2.-----------------------------

# def func_fibonacci(num):
#     if num==1 or num==0:
#         return num
#     else:
#         return func_fibonacci(num-1) + func_fibonacci(num-2)

# print(func_fibonacci(6))

#3.-----------------------------

# def potencia(n,m):
#     if m==0:
#         return 1
#     elif (m==1):
#         return n
#     else:
#         return n*(n**(m-1))

# print(potencia(5,6))

#4.-----------------------------

# def binario(num): #10 -----> 5 ---> 2
#     if num == 1:#
#         return "1"#
#     else:#entra aca
#         cociente = num//2 #10//2=5 ---- 5//2=2 ------ 2//2= 1
#         resto = num%2 #10%2 = 0 ------- 5%2=1 -------- 2%2=0
#         return str(binario(cociente)) + str(resto)#binario(5) + 0 ------ binario(2)+1 ----- binario(1)+0
#-----------------------------------------------------1010----------------------101--------------10


#5.-----------------------------
# def es_palindromo(palabra):

#     if len(palabra)<=1:
#         return True
#     if (palabra[0] == palabra[-1]):
#         return es_palindromo(palabra[1:-1])
#     else:
#         return False
    
# print(es_palindromo("neuquen"))

#6-----------------------------------

def suma_digitos(n):
    if n < 0:
        return "Ingrese un numero mayor que 0"
    if len(str(n)) == 1:
        return n
    else:
        ultimoDigito = n % 10 #Arroja la ultima cifra de n
        restoNum = n//10 #elimina la ultima cifra y deja el resto del numero
        return suma_digitos(restoNum) + ultimoDigito  
    
print(suma_digitos(36511213))