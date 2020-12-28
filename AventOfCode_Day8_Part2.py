def corroborar(posiciones,instrucciones,instruccion1,instruccion2):
    pasados = [] ; logrado = False
    for index_intruccion in posiciones:  # reocrremos cada jmp
        if (logrado == True): break;

        index = 0;pasados.clear();acumulador = 0
        instrucciones[index_intruccion] = instrucciones[index_intruccion].replace(instruccion1,instruccion2)  # remplazamos el jmp

        while True:
            if (index in pasados):                            break
            if (index == len(instrucciones)): logrado = True; break;  # decimos que se logro llegar al final

            instruccion = instrucciones[index].split(" ")[0]

            if (instruccion == "acc"):
                acumulador += int(instrucciones[index].split(" ")[1])  # sumamos el acumulador
                pasados.append(index)

            elif (instruccion == "jmp"):
                pasos = int(instrucciones[index].split(" ")[1])  # obtenemos los pasos
                if (pasos > 0):  # es positivo
                    index += (pasos - 1)
                else:
                    index += (pasos - 1)
                pasados.append(index)
            index += 1
        instrucciones[index_intruccion] = instrucciones[index_intruccion].replace(instruccion2,instruccion1)  # remplazamos el jmp
    if(logrado == True):
        print("ACUMULADOR: ",acumulador)
        return True


instrucciones = [];
jumps = []          #posiciones donde se encuentran los jumps_negativos
nops =  []           #posiciones donde se encuentras los nops

#el programa tarda un poco porque tiene muchos fors anidados
while True:
    linea = input()
    if(linea == "exit"):
        break
    instrucciones.append(linea)

for index in range(len(instrucciones) - 1):
    instruccion = instrucciones[index].split(" ")[0]
    if (instruccion == "jmp"):
        pasos = int(instrucciones[index].split(" ")[1])  # obtenemos los pasos
        jumps.append(index) #anadimos donde esta el jump
    if(instruccion == "nop"):
        nops.append(index)


pasados = [] #los index en lso que se ha pasado

logrado = corroborar(jumps,instrucciones,"jmp","nop")
if(logrado == False): #si no se pudo llegar al final preobamos cambiando los nops por los jumps
    corroborar(nops,instrucciones,"nop","jump")