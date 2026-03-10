import random

# Estado del jugador
jugador = {
    "pos": "A",
    "vida": 6,
    "oro": 0,
    "inventario": [],
    "durabilidad_espada" :2,
    "EnemigoR": 5,
    "EnemigoG": 5,
    "DialogoL": False,
    "muroJ_roto": False,
    "muroO_roto": False,
    "tesoro": False,
    "DineroH":False,
    "pistaS":False,
    "abierta":False,
    "asesinato" : False

}

# Mapa (grafo)
mapa = {
    "A": ["B","C","X"],
    "B":["A","D","E","F"],
    "C":["A","G","H"],
    "D":["B","I"],
    "E":["B"],
    "F":["B","J"],
    "G":["C","O"],
    "H":["C","R"],
    "I":["D"],
    "J":["K","F"],
    "K":["J","L","M","N"],
    "L":["K"],
    "M":["K"],
    "N":["K","S","U"],
    "O":["G","P","Q"],
    "P":["O"],
    "Q":["O","T"],
    "R":["H"],
    "S":["N"],
    "T":["Q","U"],
    "U":["N"],
    "X":["A","Z"],
    "Z":["X"]
}

def mostrar_estado():
    print("\n====================")
    print("Ubicación:", jugador["pos"])
    print("Vida:", jugador["vida"])
    print("Oro:", jugador["oro"])
    print("Inventario:", jugador["inventario"])
    if "espada" in jugador["inventario"]:
        print("Durabilidad de la espada:", jugador["durabilidad_espada"])
    print("====================")

def mover():
    opciones = mapa[jugador["pos"]]

    print("\nPuedes ir a:")
    for i, lugar in enumerate(opciones):
        print(i + 1, "-", lugar)

    eleccion = int(input("Elegir destino: ")) - 1
    jugador["pos"] = opciones[eleccion]

def evento():

    pos = jugador["pos"]

    # Herrero
    if pos == "I":
        print("\nLlegaste al herrero.")

        if "martillo" in jugador["inventario"]:

            print("1 Desoxidar espada ($8)")
            print("No se vuelve a romper")
            print("2 Comprar nueva espada oxidada ($5)")
            print("3 Salir")

            op = input("> ")

            if op == "1":

                if "espada" in jugador["inventario"]:

                    if jugador["oro"] >= 8:
                        jugador["oro"] -= 8
                        print("Espada sin oxido")
                        jugador["durabilidad_espada"] += 997
                        print("Durabilidad actual:", jugador["durabilidad_espada"])

                    else:
                        print("No cuentas con el oro suficiente")

                else:
                    print("No tienes la espada en el inventario")

   
            elif op == "2":

                if "espada" not in jugador["inventario"]:

                    if jugador["oro"] >= 5:
                        jugador["oro"] -= 5
                        print("Espada adquirida")
                        jugador["inventario"].append("espada")
                        jugador["durabilidad_espada"]+=2
                        print("Durabilidad actual:", jugador["durabilidad_espada"])

                    else:
                        print("No cuentas con el oro suficiente")

                else:
                    print("Ya tienes la espada en el inventario")

            elif op == "3":
                jugador["pos"] = "D"     

        else:
            print("No puedo trabajar sin mi martillo")


    #MURO J
    
    elif pos == "J":

        if jugador["muroJ_roto"]:
            print("El muro ya está destruido. Puedes pasar.")
            return

        print("\nTe has encontrado con un muro")
        print("Nota: Puedes romper el muro con 1 de durabilidad")

        print("1 Romper muro")
        print("2 Salir")

        op = input("> ")

        if op == "1":

            if "espada" in jugador["inventario"]:

                print("Rompes el muro y puedes avanzar")
                jugador["durabilidad_espada"] -= 1
                jugador["muroJ_roto"] = True

                if jugador["durabilidad_espada"] <= 0:
                    print("Tu espada se rompió")
                    jugador["inventario"].remove("espada")

            else:
                print("No tienes herramienta para romper el muro")
                jugador["pos"] = "F"

        elif op == "2":
            jugador["pos"] = "F"

    #MURO O
        
    elif pos == "O":

        if jugador["muroO_roto"]:
            print("El muro ya está destruido. Puedes pasar.")
            return

        print("\nTe has encontrado con un muro")
        print("Nota: Puedes romper el muro con 1 de durabilidad")

        print("1 Romper muro")
        print("2 Salir")

        op = input("> ")

        if op == "1":

            if "espada" in jugador["inventario"]:

                print("Rompes el muro y puedes avanzar")
                jugador["durabilidad_espada"] -= 1
                jugador["muroO_roto"] = True

                if jugador["durabilidad_espada"] <= 0:
                    print("Tu espada se rompió")
                    jugador["inventario"].remove("espada")

            else:
                print("No tienes herramienta para romper el muro")
                jugador["pos"] = "G"

        elif op == "2":
            jugador["pos"] = "G"        
           

    #Espada oxidada
    elif pos == "E" :

        if "espada" in jugador["inventario"]:
            return

        print("\nHas encontrado una espada")
        print("\nNota: Se encuentra en mal estado, solo soportara 2 golpes más")

        print("1 Recoger espada")
        print("2 Salir")

        op = input("> ")

        if op == "1":
            jugador["inventario"].append("espada")
            print("Espada adquirida")

        elif op == "2":
            jugador["pos"] = "B"

    #Dinero en H

    elif pos == "H":

        if jugador["DineroH"]:
            return

        print("\nHas encontrado $5")

        print("1 Recoger oro")
        print("2 Salir")

        op = input("> ")

        if op == "1":
            jugador["oro"] +=5
            jugador["DineroH"] = True

        elif op == "2":
              jugador["pos"] = "C"   


    # Enemigo en R
    elif pos == "R":

        if "Llave E" in jugador["inventario"]:
            print("El enemigo ya ha sido derrotado. Fin del camino")
            return

        print("\nCuidado, un enemigo aparece!")
       
        print("1 Atacar al enemigo")
        print("2 Escapar (Recibes -0.5HP)")

        op = input("> ")

        if op == "1":

            while jugador["EnemigoR"]>0:

                if jugador["durabilidad_espada"] > 0 and "espada" in jugador["inventario"]:

                    if "escudo" in jugador["inventario"]:
                        print("\nEl enemigo te inflinje -0.5HP")
                        jugador["vida"] -=0.5
                        if jugador["vida"] <= 0:
                                print("Has muerto")
                                exit()

                    else:
                        print("\nEl enemigo te inflinje -1HP")
                        jugador["vida"] -=1
                        if jugador["vida"] <= 0:
                                print("Has muerto")
                                exit()

                  
                    print("Tu vida actual: ",jugador["vida"])
                    print("Le inflinjes al enemigo -1HP")
                    jugador["EnemigoR"]-=1
                    jugador["durabilidad_espada"]-=1
                    print("Vida actual del enemigo: ",jugador["EnemigoR"])
                    print("Durabilidad de tu espada: ",jugador["durabilidad_espada"])
                

                    if jugador["durabilidad_espada"] <= 0:
                        print("Tu espada se rompió")
                        if "espada" in jugador["inventario"]:
                            jugador["inventario"].remove("espada")
               

                    if jugador["EnemigoR"] <=0:
                        print("\nFelicidades, enemigo derrotado")
                        print("Recibes el siguiente botín:")
                        print("+ 1 Llave E")
                        print("+ $10")
                        jugador["oro"]+=10
                        jugador["inventario"].append("Llave E")
                        break

                    if jugador["EnemigoR"] >0:
                        print("\nDeseas atacar nuevamente?")
                        print("1 Si")
                        print("2 No")
                        op2 = input("> ")

                        if (op2 == 2):
                            break
                
                else:
                    print("No cuentas con el equipamiento necesario, regresas a H y recibes -0.5HP")
                    jugador["pos"] = "H"
                    jugador["vida"] -=0.5
                    if jugador["vida"] <= 0:
                        print("Has muerto")
                        exit()
                    break

        if op == "2":
            print("Recibes penalización por escapar")
            jugador["pos"] = "H"
            jugador["vida"] -=0.5
            if jugador["vida"] <= 0:
                print("Has muerto")
                exit()

    #Persona

    elif pos == "L":

        if jugador["DialogoL"]:
            print("No hay nadie por aquí, debe ser el final")
            return

        print("\nVes a una mujer a lo lejos, ¿Que decides hacer?")
        print("1 Hablar con ella")
        print("2 Salir")

        op = input("> ")

        if op == "1":
            print("\nDecide darte un sobre, con el mensaje: La muerte contiene la llave del tesoro")
            print("Ademas contiene +$5 para ayudarte en la travesía")
            jugador["oro"] +=5
            jugador["DialogoL"] = True

        if op == "2":
              jugador["pos"] = "K"  
            

#Tienda

    elif pos == "P":
        
        while True:

            print("\n===== TIENDA =====")
            print("Oro actual:", jugador["oro"])
            print("Inventario:", jugador["inventario"])
            print("------------------")

            if "diamante" in jugador["inventario"] :
                print("Disculpa, no pude evitar notar ese brillo que emana de tu bolsillo")
                print("Deseas cambiar tu gema por $10 de oro")
                print("1 Canjear")
                print("2 Salir")


                op = input("> ")

                if op == "1":
                    jugador["oro"]+=10
                    jugador["inventario"].remove("diamante")

                else:
                    break



            print("1 Comprar escudo ($4)")
            print("2 Comprar aceite ($3)")
            print("3 Comprar Llave T por $10")
            print("4 Salir")

            op = input("> ")

        # -----------------------------
        # COMPRAR ESCUDO
        # -----------------------------
            if op == "1":

                if "escudo" in jugador["inventario"]:
                    print("Ya compraste el escudo.")

                elif jugador["oro"] >= 4:
                    jugador["oro"] -= 4
                    jugador["inventario"].append("escudo")
                   

                    print("Compraste un escudo.")

                else:
                    print("No tienes suficiente oro.")

        # -----------------------------
        # COMPRAR ACEITE
        # -----------------------------
            elif op == "2":

                if "aceite" in jugador["inventario"]:
                    print("Ya compraste el aceite.")

                elif jugador["oro"] >= 3:
                    jugador["oro"] -= 3
                    jugador["inventario"].append("aceite")
                    

                    print("Compraste el aceite.")

                else:
                    print("No tienes suficiente oro.")

        # -----------------------------
        # COMPRAR LA LLAVE T
        # -----------------------------
            elif op == "3":

                if "Llave T" in jugador["inventario"]:
                    print("Ya tienes esta llave.")

                elif jugador["oro"] >= 10:
                    jugador["oro"] -= 10
                    jugador["inventario"].append("Llave T")
                    print("Compraste la llave T.")
               
                else:
                    print("No tienes suficiente oro.")

        # -----------------------------
        # SALIR
        # -----------------------------
            elif op == "4":
                print("Sales de la tienda.")
                break


    #Portal
    elif pos == "T":
        print("Entras en un portal secreto sin regreso que te lleva a U")

    #Martillo

    elif pos == "M":

        if "martillo" in jugador["inventario"]:
            print("Nada por aquí")
            return
        
        print("\nHas encontrado un martillo")
        print("Deseas recogerlo?")
        print("1 Regoger Martillo")
        print("2 Salir")

        op = input("> ")

        if op == "1":
            jugador["inventario"].append("martillo")
            print("El martillo ha sido agregado a tu inventario")

        elif op == "2":
            jugador["pos"] = "K"  


    #Nota secreta S

    elif pos == "S":
        if jugador["pistaS"] == True:
            print("\nCreo que debo buscar al guardia")

        print("\nHas encontrado una nota misteriosa, quieres leerla?")

        print("1 Leer nota")
        print("2 Salir")

        op = input("> ")

        if op == "1":
            print("Un masaje no me vendria mal, att:Guardia")
            jugador["pistaS"] = True

        elif op == "2":
            jugador["pos"] = "N" 

        

    #PUERTA EN X
    
    elif pos == "X":
        

        if jugador["abierta"] == True:
            print("La puerta ya ha sido abierta, puedes pasar")
            return

        if "Llave T" in jugador["inventario"]:
            print("Te has topado con una puerta, deseas usar la Llave T?") 

            print("1 Abrir puerta")
            print("2 Salir")

            op = input("> ")

            if op == "1":
                print("La puerta ha sido abierta")  
                jugador["inventario"].remove("Llave T")
                jugador["abierta"] = True


                print("Cuidado, te has topado con un guardia!")

                if "aceite" in jugador["inventario"]:
                    print("Es el momento de usar el aceite para calmar al guardia con un masaje")
                    print("El guardia te deja pasar tranquilamente, avanzas a Z")  
                    
                    
                else :
                    print("Tienes que asesinar al guardia en sigilo para poder pasar (consume 1 de durabilidad) o regresar ")
                    
                    print("1 Asesinar")
                    print("2 Salir")
                    op = input("> ")

                    if op == "1":
                        print("Has eliminado al guardia, puedes avanzar")
                        jugador["durabilidad_espada"] -=1
                        jugador["asesinato"] = True

                    if op == "2":
                        jugador["pos"] = "A"


            elif op == "2":
                jugador["pos"] = "A" 

        else:
            print("Encuentras una puerta, pero no tienes la llave para pasar")
            jugador["pos"] = "A"


        if jugador["asesinato"] and jugador["abierta"]:

            print("\nCuidado, un enemigo aparece, es el esquelto del guardia!")
       
            print("1 Atacar al enemigo")

            op = input("> ")

            if op == "1":

                while jugador["EnemigoG"]>0:

                    if jugador["durabilidad_espada"] > 0 and "espada" in jugador["inventario"]:

                        if "escudo" in jugador["inventario"]:
                            print("\nEl enemigo te inflinje -0.5HP")
                            jugador["vida"] -=0.5
                            if jugador["vida"] <= 0:
                                print("Has muerto")
                                exit()

                        else:
                            print("\nEl enemigo te inflinje -1HP")
                            jugador["vida"] -=1
                            if jugador["vida"] <= 0:
                                print("Has muerto")
                                exit()

                  
                        print("Tu vida actual: ",jugador["vida"])
                        print("Le inflinjes al enemigo -1HP")
                        jugador["EnemigoG"]-=1
                        jugador["durabilidad_espada"]-=1
                        print("Vida actual del enemigo: ",jugador["EnemigoG"])
                        print("Durabilidad de tu espada: ",jugador["durabilidad_espada"])
                

                        if jugador["durabilidad_espada"] <= 0:
                            print("Tu espada se rompió")
                            if "espada" in jugador["inventario"]:
                                jugador["inventario"].remove("espada")
               

                        if jugador["EnemigoG"] <=0:
                            print("\nFelicidades, enemigo derrotado, puedes pasar")
                            jugador["pos"] = "A"
                            break
                            

                        if jugador["EnemigoG"] >0:
                            print("\nDeseas atacar nuevamente?")
                            print("1 Si")
                            print("2 No")
                            op2 = input("> ")

                            if op2 == "2":
                                break
                
                    else:
                        print("No cuentas con el equipamiento necesario, regresas a H")
                        jugador["pos"] = "H"
                        break
 

    #DIAMANTE

    elif pos == "U":

        print("Has encontrado un Diamante")
        jugador["inventario"].append("diamante")
        print("Diamante agregado al inventario")



    #TESORO    
    elif pos == "Z":

        if "Llave E" in jugador["inventario"]:
            print("\nLlegas y ves un cofre, deseas abrir el cofre con el objeto: Llave E?")

            print("1 Abrir cofre")
       
            print("2 Regresar")

            op = input("> ")

            if op == "1":
                print("Felicidades, encontraste el tesoro")
                jugador["inventario"].remove("Llave E")
                jugador["tesoro"]= True


        else:
            print("\nLlegas y ves un cofre, pero no cuentas con la llave necesaria para abrirlo ")        

            


def juego():

    print("RPG de Exploración")
    print("Encuentra el tesoro y vuelve al inicio (A)")

    while True:

        mostrar_estado()

        if jugador["pos"] == "A" and jugador["tesoro"]:
            print("\n¡¡GANASTE!! Regresaste con el tesoro.")
            break
            
        op ="1"

        if op == "1":
            mover()
            evento()

   
juego()