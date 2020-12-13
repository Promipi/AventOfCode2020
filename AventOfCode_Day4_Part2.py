def isValid(dato):
    incorrecto = 0
    for letra in dato:
        if(letra == "#"): #si es el inicio
            continue
        elif(letra.isalpha() ):
            if(letra > "f" or letra < "a"):
                incorrecto += 1
        elif(str(letra).isdigit() ): #si es un digito
            continue
        else: #si no es un caracter valido
            incorrecto +=1
            break

    if(incorrecto > 0):
        return False
    else:
        return True


pasaportes = []
pasaporte = ""

necesarios = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"] #los campos necesearios para validar el pasaporte cid opcional
colores_ojo=["amb","blu","brn","gry","grn","hzl","oth"]

while True:

    introducir = input()

    if(len(introducir) == 0 ):
        pasaportes.append(pasaporte) #metemos el pasapotte
        pasaporte =""
    if(introducir == "exit"):
        pasaportes.append(pasaporte)
        break
    pasaporte += " " + introducir

validos= 0

for pasaporte in pasaportes:

    existCid = False #para saber si existe
    contador = 0     #cuantos campos son validoss

    datos = pasaporte.split(sep=" ")

    for dato in datos: #recorremos cada dato
        campo = dato.split(sep=":") #sepearmos para campo con su valor
        if(campo[0] == "byr"):
            valor = int(campo[1])
            if(valor>=1920 and  valor<=2002):
                contador += 1

        if(campo[0] == "iyr"):
            valor = int(campo[1])
            if (valor >= 2010 and valor <= 2020):
                contador += 1

        if (campo[0] == "eyr"):
            valor = int(campo[1])
            if (valor >= 2020 and valor <= 2030):
                contador += 1

        if (campo[0] == "hgt"):
            unidadMedida = "";valor = ""
            for i in range(len(campo[1]) ): #recorremos la medida
                if(campo[1][i].isalpha() ):
                    unidadMedida = campo[1][i] + campo[1][i+1] #obtenemos a nidad de medida
                    break; #rompemos el ciclo al encontrar
                else:
                    valor += campo[1][i]  # para ir obteniendo el valor
            if(unidadMedida == "cm"):
                valor_medida = int(valor)  # convertimos a int

                if(valor_medida >= 150 and valor_medida <= 193):
                    contador+=1
            if(unidadMedida == "in"):

                valor_medida = int(valor)#convertimos a int
                if (valor_medida >= 59 and valor_medida <= 76 ):
                    contador += 1

        if(campo[0] == "hcl"):
            if(len(campo[1]) == 7 ):
                if(isValid( campo[1]) ): #si el dato es valido
                    contador+=1

        if(campo[0] == "ecl"):
            if(campo[1] in colores_ojo): #si es valido el color de pelo
                contador+=1
        if(campo[0] == "pid"):
            if(len(campo[1]) == 9):
                contador+=1

        if(campo[0] in necesarios and campo[0] == "cid"):
            contador+=1
            existCid = True

    if (contador == 8):
        validos += 1
    elif (contador == 7 and existCid == False):  # si es qe cid es opcional
        validos += 1


print("Pasaportes validos",validos)



