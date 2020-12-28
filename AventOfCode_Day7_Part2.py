def contador(reglas):
    for linea in reglas:
        separacion = linea.split("contain") #obtenemos lo que contiene
        contenido = separacion[1].split(",") #obtenemos los que contiene la bolsa

        for index in range(len(contenido)):
            for letra in contenido[index]:  # recorremos el conjunto
                if (letra.isdigit()):
                    bolsa = (contenido[index].split(letra)[1]).replace(".", "").replace("s","")  # liminamos la s para que no haya plurales

                    if (bolsa.strip() in colores):  # si la bolsa que contiene ya hereda de un shiny love
                        bolsa_color = separacion[0]  # asignamos la bolsa padre


reglas = []
#el programa tarda un poco porque tiene muchos fors anidados
while True:
    linea = input()
    if(linea == "exit"):
        break
    reglas.append(linea)










