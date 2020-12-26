
respuestas = []

while True:
    linea = input()
    if(linea == "exit"):
        break
    respuestas.append(linea)

respondidas = {" ": 0 } #para ver cuantas personas respondieron que pregunta en un determinado grupo
recuentos = [] ; preguntas = []

contador = 0;
ultimo_grupo = 0
index = 0
for linea in respuestas:

    if(linea != ""):#si estamos en el mismo grupoo

        for letra in linea:
            if(letra in respondidas.keys() ): #si ya alguien respondio que si
                respondidas[letra]+=1 #aumentamso su contador
            else: #si no
                respondidas[letra] = 1 #agregamos el registro
                preguntas.append(letra)
                
    else: #si ya cmabiaremos de grupo
        print(preguntas)
        n_personas = 0
        for linea in range(ultimo_grupo,index):  # para saber cuantas personas tiene el grupo
            if (respuestas[linea] == ""):
                break;
            n_personas += 1

        for pregun in preguntas:#recorremos la lista de preguntas del grupo
            if(respondidas[pregun] == n_personas): #si todos respondieron esa pregunta
                contador +=1 #aumentamos el contador de respondidos por grupo

        recuentos.append(contador) #
        ultimo_grupo = index + 1 #marcamos deonde quedo el ultimo grupo
        preguntas.clear(); respondidas.clear() #y reiniciamos los arreglos
        contador = 0

    index += 1

recuentos.append(contador)

suma = 0
for recuento in recuentos:
    suma += recuento
print("LA SUMA DE LOS RECUENTOTS ES: ",suma)
