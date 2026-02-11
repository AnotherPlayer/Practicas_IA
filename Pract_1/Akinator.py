
def akinator_rick_y_morty():
    
    print("-------------------------------------------------")
    print("🤖 BIENVENIDO AL AKINATOR DE RICK Y MORTY 🤖")
    print("Piensa en uno de los siguientes 15 personajes:")
    print("Rick, Morty, Pepinillo Rick, Evil Morty, Jerry, Summer,")
    print("Beth, Beth clon, Rick prime, H. pájaro, Mr. Mysix,")
    print("Sr. Pantalones de popo, Jesús, Presidente, Esposa de Rick")
    print("-------------------------------------------------\n")
    
    input("Presiona ENTER cuando estés listo...")

    # PREGUNTA 1: La gran división (Familia vs Externos)
    # Dividimos el grupo en 10 (Familia/Variantes) vs 5 (Externos)
    res = input("¿El personaje pertenece biológicamente a la familia Smith/Sanchez (incluyendo variantes de otras dimensiones)? (si/no): ").lower()

    if res == "si":
        # Rama FAMILIA (10 personajes)
        # Rick, Morty, Pepinillo, Evil Morty, Jerry, Summer, Beth, Beth clon, Prime, Esposa
        
        # PREGUNTA 2 (Rama Familia): Género
        res = input("¿El personaje es mujer? (si/no): ").lower()
        
        if res == "si":
            # Sub-rama MUJERES (4 personajes): Summer, Beth, Beth clon, Esposa de Rick
            
            # PREGUNTA 3: Generación/Edad
            res = input("¿Es una adolescente? (si/no): ").lower()
            if res == "si":
                print("\n>>> ¡Tu personaje es SUMMER!")
            else:
                # Quedan: Beth, Beth clon, Esposa de Rick
                res = input("¿El personaje está vivo actualmente en la serie principal (C-137/Actualidad)? (si/no): ").lower()
                if res == "no":
                     print("\n>>> ¡Tu personaje es la ESPOSA DE RICK (Diane)!")
                else:
                    # Quedan: Beth y Beth clon
                    res = input("¿Es la versión que se cree que es un clon o 'Space Beth'? (si/no): ").lower()
                    if res == "si":
                        print("\n>>> ¡Tu personaje es BETH CLON!")
                    else:
                        print("\n>>> ¡Tu personaje es BETH!")
        
        else:
            # Sub-rama HOMBRES DE FAMILIA (6 personajes): 
            # Rick, Morty, Pepinillo, Evil Morty, Jerry, Rick Prime
            
            # PREGUNTA 3: ¿Es un Rick o variante directa de Rick?
            res = input("¿El personaje es una versión de Rick Sanchez (o se convirtió en una)? (si/no): ").lower()
            
            if res == "si":
                # Quedan: Rick, Pepinillo Rick, Rick Prime
                res = input("¿Es literalmente un vegetal encurtido? (si/no): ").lower()
                if res == "si":
                    print("\n>>> ¡Tu personaje es PEPINILLO RICK!")
                else:
                    res = input("¿Es el villano principal que mató a la familia del Rick original? (si/no): ").lower()
                    if res == "si":
                        print("\n>>> ¡Tu personaje es RICK PRIME!")
                    else:
                        print("\n>>> ¡Tu personaje es RICK (C-137)!")
            else:
                # Quedan: Morty, Evil Morty, Jerry
                res = input("¿El personaje es el padre de familia (o figura paterna desempleada)? (si/no): ").lower()
                if res == "si":
                    print("\n>>> ¡Tu personaje es JERRY!")
                else:
                    # Quedan: Morty y Evil Morty
                    res = input("¿Usa un parche en el ojo o es presidente de la Ciudadela? (si/no): ").lower()
                    if res == "si":
                        print("\n>>> ¡Tu personaje es EVIL MORTY!")
                    else:
                        print("\n>>> ¡Tu personaje es MORTY!")

    else:
        # Rama EXTERNOS (5 personajes)
        # H. Pájaro, Mr. Mysix, Sr. Pantalones de popo, Jesús, Presidente
        
        # PREGUNTA 2 (Rama Externos): Humanidad/Apariencia
        res = input("¿El personaje tiene apariencia completamente humana normal? (si/no): ").lower()
        
        if res == "si":
            # Quedan: Jesús, Presidente
            res = input("¿Es una figura religiosa bíblica? (si/no): ").lower()
            if res == "si":
                print("\n>>> ¡Tu personaje es JESÚS!")
            else:
                print("\n>>> ¡Tu personaje es el PRESIDENTE!")
        else:
            # Quedan: H. Pájaro, Mr. Mysix, Sr. Pantalones de popo
            res = input("¿El personaje es de color azul? (si/no): ").lower()
            if res == "si":
                print("\n>>> ¡Tu personaje es MR. MYSIX!")
            else:
                res = input("¿Tiene alas y características de ave? (si/no): ").lower()
                if res == "si":
                    print("\n>>> ¡Tu personaje es HOMBRE PÁJARO!")
                else:
                    print("\n>>> ¡Tu personaje es EL SEÑOR PANTALONES DE POPO!")

# Ejecutar el juego
if __name__ == "__main__":
    akinator_rick_y_morty()