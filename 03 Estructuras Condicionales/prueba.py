magnitud_terremoto = int(input("Ingrese la magnitud del terremoto: "))

if (magnitud_terremoto < 3):
    print("Muy leve:")
    print( 'imperceptible')
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve:")
    print("ligeramente perceptible")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado:")
    print("sentido por personas, pero generalmente no causa daños")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte:")
    print('puede causar daños en estructuras débiles')
elif magnitud_terremoto >= 6 and magnitud_terremoto <7:
    print("Muy fuerte:")
    print("puede causar daños significativos")
elif magnitud_terremoto >= 7:
    print("Extremo:")
    print("puede causar graves daños a gran escala")