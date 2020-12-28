reglas = []
#el programa tarda un poco porque tiene muchos fors anidados
while True:
    linea = input()
    if(linea == "exit"):
        break
    reglas.append(linea)

colores = ["hiny gold bag","hiny gold bags"] #colore squ heredan a shiny gold

for i in range(len(reglas)):
    for linea in reglas:
        separacion = linea.split("contain") #obtenemos lo que contiene
        contenido = separacion[1].split(",") #obtenemos los ue contiene la bolsa

        bolsa_color = ""
        for index in range(len(contenido)):

            for letra in contenido[index]: #recorremos el conjunto
                if(letra.isdigit() ):
                    bolsa = (contenido[index].split(letra)[1]).replace(".","").replace("s","") #liminamos la s para que no haya plurales
                    if(bolsa.strip() in colores):   #si la bolsa que contiene ya hereda de un shiny love
                        bolsa_color = separacion[0] #asignamos la bolsa padre


        if(bolsa_color != "" ):
            bolsa_color = bolsa_color.replace("s","").strip() #eliminamos la s
            if(not(bolsa_color in colores) ): #si no existe esa bolsa de color ya
                colores.append(bolsa_color) #nadimos la nueva bolsa que puede almacenar un shiny love

print("CANTIDAD DE BOLSAS: ",len(colores) - 2) #mostramos la cantidad de bolsas que alamacenen o hereden shiny gold