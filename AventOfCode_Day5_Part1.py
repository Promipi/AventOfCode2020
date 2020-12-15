def mitad_inferior(desde,hasta): #intruccion F y L
    inferior = int( (hasta-desde ) / 2)
    return hasta-inferior-1

def mitad_superior(desde,hasta): #instrucction B y R
    superior = int( (hasta - desde) / 2)
    return hasta - superior

def buscar_separacion(asiento):
    for i in range(len(asiento) ):
        if(asiento[i] != "F" and asiento[i] != "B"):
            return  str(asiento[i:len(asiento)] )

def realizar(instrucciones ):
    for caracter in asiento:
        if (caracter == instrucciones[0]):  # mitad inferior
            rango[1] = mitad_inferior(rango[0], rango[1])
        if (caracter == instrucciones[1]):  # mitad superior
            rango[0] = mitad_superior(rango[0], rango[1])
    return rango[0] #retoranmos cuanto nos dio al hacer la media


rango = [0,127] #para ir descubbrinedo el asiento
asientos = []

while True:
    linea = input()
    if(linea == "exit"):
        break
    asientos.append(linea)

fila = 0;columna =0;mayor_id = 0

for asiento in asientos:
    rango =[0,127]
    fila = realizar(["F", "B"])
    #
    ultimo = buscar_separacion(asiento)  # para recorrer la ultiuma intruccion
    rango = [0, 7]
    #
    columna = realizar(["L", "R"])
    id = ( (fila * 8) + columna)
    if(id > mayor_id):
        mayor_id = id#establecesmo el nuevo mayor


print("Mayor id: ",mayor_id)
