

acumulador = 0
instrucciones = []
#el programa tarda un poco porque tiene muchos fors anidados
while True:
    linea = input()
    if(linea == "exit"):
        break
    instrucciones.append(linea)

pasados = [] #los index en lso que se ha pasado

index = 0
while True:
    print(index)
    if (index in pasados): break  # si ya pasamos por aqui

    instruccion = instrucciones[index].split(" ")[0]


    if(instruccion == "acc"):
        acumulador += int(instrucciones[index].split(" ")[1] ) #sumamos el acumulador
        pasados.append(index)

    elif(instruccion == "jmp"):
        pasos =       int(instrucciones[index].split(" ")[1] )#obtenemos los pasos
        if(pasos>0): #es positivo
            index += (pasos - 1)
        else:
            index += (pasos - 1)
        pasados.append(index)
    index+=1


print("ACUMULADOR",acumulador)

