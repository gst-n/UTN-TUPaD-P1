
hemisferio = input("Ingrese el hemisferio donde se encuentra (N/S) : ").capitalize();
mes =  input("Ingrese el mes del año: ").capitalize()
dia = int(input("Ingrese el día: "))
#calendario = (20,21,22,23,24,25,26,27,28,29,30,31,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)

verano_sur = ('Enero', 'Febrero')
otoño_sur = ('Abril', 'Mayo')
invierno_sur = ('Julio', 'Agosto')
primavera_sur = ('Octubre','Noviembre')

if hemisferio == 'S':
    if (mes == 'Diciembre' and dia >= 21 ) or ((mes in verano_sur and dia >= 1 and dia <= 30) or (mes == 'Marzo' and dia <= 20)):
        print ('Estas en Verano')
    if (mes == 'Marzo' and dia >= 21) or ((mes in otoño_sur and dia >= 1 and dia <= 30) or (mes == 'Junio' and dia <=20)):
        print('Estas en Otoño')
    if (mes == 'Junio' and dia >= 21) or ((mes in invierno_sur and dia >= 1 and dia <= 30) or (mes == 'Septiembre' and dia <=20)):
        print('Estas en Invierno')
    if (mes == 'Septiembre' and dia >=21) or ((mes in primavera_sur and dia >= 1 and dia <= 30) or (mes == 'Diciembre' and dia <=20)):
        print('Estas en Primavera')
elif hemisferio == 'N':
    if (mes == 'Diciembre' and dia >= 21 ) or ((mes in verano_sur and dia >= 1 and dia <= 30) or (mes == 'Marzo' and dia <= 20)):
        print ('Estas en Inverno')
    if (mes == 'Marzo' and dia >= 21) or ((mes in otoño_sur and dia >= 1 and dia <= 30) or (mes == 'Junio' and dia <=20)):
        print('Estas en Primavera')
    if (mes == 'Junio' and dia >= 21) or ((mes in invierno_sur and dia >= 1 and dia <= 30) or (mes == 'Septiembre' and dia <=20)):
        print('Estas en Verano')
    if (mes == 'Septiembre' and dia >=21) or ((mes in primavera_sur and dia >= 1 and dia <= 30) or (mes == 'Diciembre' and dia <=20)):
        print('Estas en Otoño')


print(f'los valores ingresados fueron ({hemisferio} - hemisferio), ({mes} - mes), ({dia} - dia)')