def pedir_respuesta(pregunta):
    while True:
        # Convierte la respuesta a minúsculas y quita espacios
        texto = input(pregunta).lower().strip()
        if texto == "si" or texto == "no":
            return texto
        else:
            print("Error: solo es valida la respuesta 'si' o 'no'")


opcion = "1"

while opcion == "1":
    print("Bienvenido al Akinator de Rick y Morty ... by David y Diego")
    print("Piensa en uno de los 15 personajes de la lista vista en clase")
    print("Responde con 'si' o 'no'")
    print("-" * 30)

    # Pregunta 1: División principal (Familia y Otros) 
    respuesta = pedir_respuesta("¿Tu personaje es un Sánchez o un Smith? (incluyendo todas las versiones)")

   
    if respuesta == "si": #acepto que si es de los Sanchez

        # Rama de la Familia (Rick, Morty, Summer, Beth, Jerry y todos esos)
        respuesta = pedir_respuesta("¿Eres alguno de los 2 protagonistas?")  # Ricks y Mortys

        if respuesta == "si":
            respuesta = pedir_respuesta("¿Tu personaje es un adolescente de 14 años que uso o usa playeras amarillas???") #Es morti o evil morty?


            if respuesta == "si":
                respuesta = pedir_respuesta("Es enano, pero ¿es el NO lloron?") #vamos al evil morty

                if respuesta == "si":
                    print("Tu personaje es: Evil Morty") #EVIL MORTY
                else:
                    print("Tu personaje es: Morty") #MORTY


            else:
                # Es Rick??
                respuesta = pedir_respuesta("¿Es un pepinillo?") #aposte por la rapida (pepinillo rick)
                if respuesta == "si":
                    print("Tu personaje es: Pepinillo Rick")


                else:
                    respuesta = pedir_respuesta("Mato a Diane Sanchez?")

                    if respuesta == "si":
                        print("Tu personaje es: Rick Prime")
                    else:
                        print("Tu personaje es: Rick")
        
        else:
            # Summer, Beths, Jerry, Diane Sanchesz (esposa de rick)
            respuesta = pedir_respuesta("¿Tu personaje es mujer?")



            if respuesta == "si":
                respuesta = pedir_respuesta("¿Su adn la identifica como hija de Rick??")

                if respuesta == "si":
                    respuesta = pedir_respuesta("¿Es una aventurera espacial?")

                    if respuesta == "si":
                        print("Tu personaje es: Clon Beth")
                    else:
                        print("Tu personaje es: Beth")
                        
                else:
                    respuesta = pedir_respuesta("¿Suele usar playera rosa de mangas cortas?")
                    if respuesta == "si":
                        print("Tu personaje es: Summer")
                    else:
                        print("Tu personaje es: Diane Sanchez (esposa rick)")


            else:
                # Es el unico otro hombre jerry
                print("Tu personaje es: Jerry")

    else:
        # Rama de Birdperson, Meeseeks, Poopybutthole, Jesús, Presidente
        respuesta = pedir_respuesta("¿Tu personaje parece completamente humano?")
        

        if respuesta == "si":
            # Jesús y Presidente
            respuesta = pedir_respuesta("¿Es una figura religiosa?")

            if respuesta == "si":
                print("Tu personaje es: Jesús")
            else:
                print("Tu personaje es: El Presidente de Estados Unidos")


        else:
            # Birdperson, Meeseeks, Poopybutthole
            respuesta = pedir_respuesta("¿Es de color azul? ")
            if respuesta == "si":
                print("Tu personaje es: Mr. Meeseeks")
            else:
                respuesta = pedir_respuesta("¿Tiene alas? ")
                if respuesta == "si":
                    print("Tu personaje es: Hombre Pájaro")
                else:
                    print("Tu personaje es: Mr. Poopybutthole \n casi nadie se acuerda de el")

    print("-" * 30)
    print("Fin del juego :P")
    print("-" * 30)
    
    # Bucle para validar la opción de repetir o salir
    while True:
        temp = input("Presiona 1 para volver a jugar o 0 para salir: ").strip()
        if temp == "1" or temp == "0":
            opcion = temp
            break
        print("Error: presiona 1 o 0.")