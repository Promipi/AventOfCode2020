ranges = [   ] #desde hasta debe ir el maximo de claves('una letra') en la contrasena
passwords = [] #las claves
correctas = 0
lineas = 0

while True:
    linea = str(input() ) #obtenemos la inea
    if(linea == "exit"):
        break; #poara cuando ya no digitemos mas claves
    separado = linea.split(sep=" ") #separamos el string cuando encontamos un espacio
    desde_hasta = separado[0].split(sep="-")
    ranges.append(  [  desde_hasta[0],desde_hasta[1],  separado[1].split(sep=":")[0] ]  ) #anadimos el rango que se debe cumplir para la la letra especifica
    passwords.append(  linea.split(sep=":")[1]  ) #anade la contrasena de la derecha

for i in range(len(passwords) ):
    veces = 0
    for letra in passwords[i]:  # recorremos la clave de donde estamos
        if (letra == ranges[i][2]):  # si la letra donde estamos es la letra que debe contenter
            veces += 1  # sumnamos la veces que aparecen
    if (veces >= int(ranges[i][0]) and veces <= int(ranges[i][1])):
        correctas += 1  # sumamos que esta dcorecta la clave

print("Numero de claves correctas: ",correctas)
