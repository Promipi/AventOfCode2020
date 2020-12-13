ranges = []
passwords = []
correctas = 0


while True:
    linea = str(input())  # obtenemos la inea
    if (linea == "exit"):
        break;  # poara cuando ya no digitemos mas claves

    separado = linea.split(sep=" ")  # separamos el string cuando encontamos un espacio
    desde_hasta = separado[0].split(sep="-")
    ranges.append([desde_hasta[0], desde_hasta[1],separado[1].split(sep=":")[0]])  # anadimos el rango que se debe cumplir para la la letra especifica
    passwords.append(linea.split(sep=":")[1])  # anade la contrasena de la derecha


for i in range(len(passwords)): #recorremos las veces del largo de nuestra lista
    conta = 0;
    if(passwords[i][    int(ranges[i][0])     ]  == ranges[i][2]): #si en la posicion 1 de nuestro rango
        conta+=1
    if(passwords[i][   int(ranges[i][1])     ] == ranges[i][2] ): #lo mismo pero en la psoicion 2 de nuestro rango
        conta+=1
    print("----")

    if(conta == 1):
        correctas+=1




print("Hay : ",correctas,"  claves correctas ")







