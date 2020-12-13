map = [] #el mapa
pendientes = []
pendientes.append(  [1,1]  ) #derecha abajo
pendientes.append(  [3,1]   )
pendientes.append(  [5,1]   )
pendientes.append(  [7,1]   )
pendientes.append(  [1,2]   )



column = 0
arboles = []

while True:
    linea = input()
    if(linea == "exit"):
        break;
    map.append(linea)

for i in range(len(map)):  # para ir bajando de uno en uno
    map[i] = map[i] * 100  # rrelenamos mucho hacia la derecha

for pendiente in pendientes:
    contador_arbol = 0
    for i in range(   0,len(map),pendiente[1] )     :
        if(map[i][column]  == "#"):
            contador_arbol += 1
        column += pendiente[0]
    print("arboles : ",contador_arbol)
    arboles.append(contador_arbol)

    column=0


multiplicacion = 1
for num in arboles:
    multiplicacion *= num
print("La multiplicacion da: ",multiplicacion)



