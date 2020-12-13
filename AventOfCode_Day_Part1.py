map = [] #el mapa

while True:
    linea = input()
    if(linea == "exit"):
        break;
    map.append(linea)

column = 0
arboles = 0 #contador de arboles
print("FILAS TOTALES: ",len(map))

for i in range(len(map) ): #para ir bajando de uno en uno
    map[i] = map[i] * 100 #rrelenamos mucho hacia la derecha

for i in range(  len(map)  ):
    if(map[i][column] == "#"):
        arboles += 1
    column+=3 #aumentamos la columna
print("Arboles: ", arboles)