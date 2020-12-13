pasaportes = []
pasaporte = ""

necesarios = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"] #los campos necesearios para validar el pasaporte cid opcional

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
    presentes = 0#cuantos campos estan presentes

    datos = pasaporte.split(sep=" ")


    for dato in datos: #recorremos cada dato
        dato = dato.strip() #liminamos espacios en blanco
        campo = dato.split(sep=":")[0] #obtenemos el nombre
        if (campo == "cid"):
            existCid = True  # decimos que existe
            print("HAY CID")

        if campo in necesarios:
            presentes+=1

    if(presentes==8):
        validos += 1
    elif(presentes == 7 and existCid == False): #si es qe cid es opcional
        validos += 1

print("pasaportes validos : ",validos)

print(pasaportes,end="\n")