respuestas = []

while True:
    linea = input()
    if(linea == "exit"):
        break
    respuestas.append(linea)


recuentos = []; contador = 0;usadas = []
for linea in respuestas:
    if(linea != ""):
        for letra in linea:

            if(not(letra in usadas) ): #si la letra no existe
                contador += 1; usadas.append(letra) #sumamos el contador y ya anadimos la usada
    else:
        recuentos.append(contador); contador = 0; usadas.clear()

recuentos.append(contador) #anadimos el ultimo contador

suma = 0
for recuento in recuentos:
    suma += recuento
print("LA SUMA DE LOS RECUENTOTS ES: ",suma)
                
                
                
                
                
                
                
                