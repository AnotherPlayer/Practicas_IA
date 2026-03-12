import os

pos_x = 0
acompañante = False
cambio_mapa = False
objetos = [0, 0, 0, 0, 0, 0, 0]
eventos = [False, False, False, False]
accion = ""
eleccion = 0


inicio = {
    0: [2, 3],
    1: [2],
    2: [0, 1],
    3: [0, 5, 4],
    4: [3,6, 7],
    5: [3, 10],
    6: [4],
    7: [4, 8, 9],
    8: [7],
    9: [7],
    10: [5]
}

templo_agua = {
    0: [1],
    1: [2, 4],
    2: [1, 3],
    3: [2, 6],
    4: [1, 5, 7],
    5: [4],
    6: [3],
    7: [4, 8, 9],
    8: [7],
    9: [7]
}

templo_viento = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5, 6],
    5: [4],
    6: [4, 7, 8],
    7: [6],
    8: [6]
}

def intro():
    print("Estas en tu casa, ubicada en la gran ciudad de un reino tranquilo")
    print("sentado en tu cama cierras los ojos, entras en lo que parece ser un sueño")
    input("")
    

    print("Voz misteriosa: Tu... tu eres mi elegido")
    input("")
    print("preguntas: ¿quien eres?, ¿elegido para que?")
    print("voz misteriosa: Soy el ser que controla el universo, y tengo una tarea para ti")
    print("tu seras quien libere a este mundo del peor mal, las tres bestias del catastrofe")
    input("")

    print("voz misteriosa: Enfrentate a las tres bestias legendarias y seras el heroe de este mundo")
    print("por mi parte seras recompensado, te dire el mayor secreto de este mundo")
    input("")

    print("voz misteriosa: Ahora ve a la iglesia, ahi te daran lo que necesitas, lo demas depende de ti")
    print("pero te advierto....")
    input("")
    print("voz misteriosa: debes hacerlo solo, nadie puede acompañarte, si aceptas ayuda ya no cuentas conmigo...")
    input()

def mapa1(eleccion):
    global acompañante 
    global cambio_mapa 
    global objetos 
    global eventos 
    global accion 

    match eleccion:
        case "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estas en la ciudad")
            input()
            
            return 0

        case "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            if acompañante == True:
                print("Estas en la biblioteca oculta")
                print("Hombre misterioso: esta es la biblioteca oculta de la iglesia")
                print("El hombre abre un libro")
                input()

                print("Hombre misterioso: aqui esta, este libro habla sobre ese ser que te habla en sueños")
                print("el no es lo que aparenta, el quiere apoderarse del mundo, y lounico que se lo impide...")
                input()

                print("Hombre misterioso: son las bestias, ellas protegen al mundo y controlan los climas")
                print("toma esa espada y ven conmigo")
                print("¡obtienes espada oscura!")
                input()

                print("El hombre misterioso abre un portal con el libro")
                print("Hombre misterioso: sigueme, es nuestra oportunidad para acabarlo")
                input()

                print("Entras al portal y te encuentras en un espacio blanco")
                print("El hombre misterioso abre un portal con el libro")
                print("ahi se encuentra un hombre, sonriendo a ustedes")
                input()
                print("Ser maligno: al final escogiste no hacerme caso, que mal")
                print("No importa, alguien mas hara tu trabajo")
                print("El ser maligno levanta su mano, una luz sale disparada hacia ti")
                input()
                print("el hombre misterioso logra cubrirte")
                print("hombre misterioso: ataca, ahora!")
                input()
                print("Tu movimiento rapido da en el blanco, pero el ser maligno no parece sentir dolor")
                print("en cambio ves esa sonrisa en su rostro")
                input()
                print("Ser maligno: Esa espada no es suficiente, fin del juego...")
                print("Despues de una luz brillante todo acaba")
                input()

                os.system('cls' if os.name == 'nt' else 'clear')
                print("has desbloqueado final malo: Desafiando lo imposible")
                input()
                return 0
            else:
                print("aun no puedes entrar ahi")
                print("Estas en la iglesia")
                input()
                return 2
                
        case "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estas en la iglesia")
            if eventos[0] == False:
                print("Estas en la iglesia")
                input()

                print("Monje: bienvenido, tu debes ser el elegido")
                print("toma esto y comienza tu aventura en el bosque")
                input()

                print("!recibes espada de agua¡")
                objetos[0] = 1
                eventos[0] = True
            input()
                
            return 2
        
        case "3":
            print("Estas en la entrada del bosque")
            if eventos[1] == False:
                print("Llegas a la entrada del bosque, donde un hombre parece estar esperando")
                input()
                print("Hombre misterioso: al fin llegas, estaba esperandote")
                print("Tienes una tarea, yo puedo ayudarte y ver la verdad")
                input()
                print("hombre misterioso: Te unes a mi?  si/no")
                accion = input("Accion: ")

                if accion == "si":
                    print("Hombre misterioso: entonces sigueme a la iglesia, hay algo que debes ver")
                    print("El hombre camina hacia la iglesia")
                    
                    acompañante = True
                    accion = ""
                else:
                    print("Hombre misterioso: espero que no te arrepientas")
                    
                    accion = ""
                eventos[1] = True
            input()

            return 3
                
        case "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("vas por un camino del bosque")
            input()

            return 4
        case "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estas en el lago")
            if objetos[1] == 1:
                print("Junto al lago ves una gran montaña")
                print("el ambiente pacifico invita a tocar un poco de musica")
                accion = input("accion: ")

                if accion == "tocar":
                    print("Tocas la melodia que el viejo musico te enseño")
                    print("en la montaña se escucha resonar cada nota de la melodia")
                    input()
                    print("con un fuerte estruendo la montaña abre una entrada, la primer prueba esta delante")
                    input()
                    accion = ""
                else:
                    print("eso no funcino, vuelve a la entrada del bosque (3)")
            else:
                print("Por el momento no hay nada que hacer aqui")
            input()
            
            return 5
        
        case "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encuentras un lugar pacifico, aprovecha y descansa")
            input()

            return 6
        
        case "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("vas por un camino del bosque")
            input()
            
            return 7
        
        case "8":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fin del camino, sera mejor volver")
            input()
            
            return 8
    
        case "9":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estas frente a una cabaña")
            if eventos[2] == False:
                print("Te recibe un viejo musico con varios instrumentos en su mesa")
                print("musico: La musica puede abrir puertas que no podemos ver")
                input()
                print("El musico toca una melodia que queda gravada en tu mente")
                print("Te gusta eh!, toma, llevate esta flauta y lleva la musica en tu viaje")
                input()
                print("¡reibes una flauta!")
                objetos[1] = 1
                eventos[2] = True
            input()

            return 9
        
        case "10":
            os.system('cls' if os.name == 'nt' else 'clear')
            if objetos[1 == 1]:
                print("Al entrar te encuentras cara a cara con la primer bestia")
                print("Un gran leon con una melena que esta formada por llamas ardientes")
                input()
                print("Tu espada de agua comienza a brillar, tomas coraje y atacas")
                input()
                print("despues de una intensa batalla te alzas con la victoria")
                print("encuentras un cofre, lo abres y obtienes tu primer recompensa")
                input()

                print("¡obtienes espada de viento!")
                objetos[2] = 1
                input()

                print("escuchas una voz en tu mente")
                print("voz misteriosa: bien, estas probando tu valentia, continua asi")
                input()
                print("Frente a ti se abre un portal")
                print("voz misteriosa: adelante, ese portal te llevara al templo de agua")
                input()

                print(" al entrar eres transportado al templo del agua")
                cambio_mapa = True
                input()
            else:
                print("aun no puedes entrar aqui")
                input()
                return 10
           
        case _:
            print("Opción no válida")
            input()
            return 0

def mapa2(eleccion):
    global acompañante 
    global cambio_mapa 
    global objetos 
    global eventos 
    global accion

    match eleccion:
        case "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estas en la entrada del templo del agua")
            input()

            return 0
        case "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Vas por el camino del templo")
            input()

            return 1
        case "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encuentras la biblioteca del templo, hay libros por todos lados")
            print("Los libros hablan sobre antiguas civilizaciones")
            print("Una de ellas fue arruinada por un consejo de alguien desconocido")
            input()

            return 2
        case "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Vas por el camino del templo")
            input()

            return 3
        case "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Vas por el camino del templo")
            input()

            return 4
        case "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fin del camino, sera mejor volver")
            input()

            return 5
        case "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            if objetos[3] == 1:
                print("Entraste al almacen del templo")
                print("obtienes un escudo, te sera util")
                objetos[4] = 1
                input()

                return 6
            else:
                print("necesitas la llave del almacen")
                input()
                return 3

        case "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            if eventos[3] == False:
                print("Te encuentras con un explorador perdido")
                input()
                print("Explorador: Ni si quiera yo se como llegue aqui, y se ve muy peligroso") 
                print("toma esta llave, espero te sirva, yo buscare la salida")
                input()

                print("¡obtienes la llave del almacen!")
                objetos[3] = 1
                print("el explorador se va")         
                eventos[3] = True
                input()

            return 7
        case "8":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encuentras un lugar tranquilo, aprovecha y descansa")
            input()

            return 8
        case "9":
            os.system('cls' if os.name == 'nt' else 'clear')
            if objetos[4] == 0:
                print("Frente a ti esta la bestia de agua")
                print("la cual no pierde tiempo y te lanza ataques de agua a distancia")
                input()
                print("no logras acercarte, necesitas algo para cubrirte, vuelve despues")
                input()

            else:
                print("Frente a ti esta la bestia de agua")
                print("la cual no pierde tiempo y te lanza ataques de agua a distancia")
                input()
                print("El escudo te cubre de todos sus ataques, te acercas lo suficiente")
                print("logras llevarte la victoria, frente a ti esta un cofre contu recompensa")
                input()
                print("¡Obtienes espada de fuego!")
                objetos[5] = 1
                input()

                print("Voz misteriosa: Solouno mas, no te detengas ahora")
                print("Se abre el portal de tu siguiente destino")
                cambio_mapa = True
                input()
            return 9

        case _:
            print("Opción no válida")
            input()
            return 0

def mapa3(eleccion):
    global acompañante 
    global cambio_mapa 
    global objetos 
    global eventos 
    global accion

    match eleccion:
        case "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estas en la entrada del templo del viento")
            input()

            return 0
        
        case "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("vas por un camino del templo")
            input()

            return 1
        
        case "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encuentras una advertencia en la pared que dice:")
            print("Nunca debes dudar, o no podraas superar el desafio")
            input()

            return 2
        
        case "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("vas por un camino del templo")
            input()

            return 3
        
        case "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encuentras una advertencia en la pared que dice:")
            print("Solo puedes creer en tu propio criterio")
            input()

            return 4
        
        case "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Encuentras un lugar seguro, aprovecha y descansa...")
            print("Encuentras las alas de icaro, podras volar con ellas")
            objetos[6] = 1
            input()

            return 5
        
        case "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            if objetos[6] == 0:
                print("Entras y encuentras a la bestia de viento, la cual reacciona de inmediato")
                print("Vuela alrededor de la sala fuera de tu alcance")
                print("quiza sea mejor buscar algo, vuelve")
                input()
            else:
                print("Entras y encuentras a la bestia de viento, la cual reacciona de inmediato")
                print("Vuela alrededor de la sala fuera de tu alcance")
                print("Usas las alas para acercarte")
                input()

                print("Tu espada de fuego se alimenta del viento de la bestia")
                print("Lo que la hace mas poderosa, con lo que logras llevarte la victoria")
                input()

                print("Voz misteriosa: lo lograste, acercate al ultimo portal, cumplire mi promesa")
                input()

                print("justo al lado del portal esta el hombre misterioso")
                print("Hombre misterioso: Asi que... al finallolograste, te dare una ultima oportunidad")
                print("ven conmigo, conoce la verdad de lo que haz hecho")
                input()

                cambio_mapa = True
            return 6
        
        case "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Entras al portal, llegas a un lugar donde solo ves paredes blancas alrededor")
            print("La figura de un hombre se acerca a ti, con una sonrisa horrorosa")
            input()

            print("Ser maligno: lo hiciste, no puedo creer que de verdad lo hiciste jajaja")
            print("aqui esta el secreto, yo vine a adueñarme del poder de esta tierra")
            input()

            print("Ser maligno: El poder de esas bestias era lo unico que me impedia entrar")
            print("pero gracias a ti, ahora nada me impide tomar este mundo... y tu ya no me sirves mas...")
            input()

            print("De pronto tu vista se nubla, no hay nada que hacer...")
            input()

            cambio_mapa = True

            return 7
        
        case "8":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("El hombre misterioso te lleva cerca del portal")
            print("Hombre misterioso: Ese ser que te contacto ha sido el causante de desastres")
            print("pasa poder apoderarse del mundo necesitaba que las bestias fueran derrotadas")
            input()

            print("Hombre misterioso: pero tenemos una ventaja, contigo tienes las tres espadas legendarias")
            print("damelas un momento")
            input()
            print("Le entregas las espadas, el las toma y las pone juntas")
            print("Con un gran brillo, las espadas se unen en una sola")
            print("Hombre misterioso: Tomala, es hora de la verdad")
            input()

            print("Tomas la espada y entran ambos al portal")
            input()

            print("Ser maligno: que veo aqui, me estas traicionando?")
            print("El hombre misterioso no espera para atacar, logrando detener al ser")
            print("Hombre misterioso: Ahora!")
            input()

            print("Sin perder tiempo atacas, la espada te guia al punto vital del ser")
            print("El cual se desvanece en el aire")
            input()

            print("Despues de un destello te hayas en la ciudad de nuevo, el hombre misterioso a tu lado")
            print("Hombre misterioso: Lo hicimos, hiciste lo correcto...")
            input()

            print("Cuenta la leyende que fue asi como el mundo prospero, la vida fue protegida")
            print("y las catastrofes no volvieron a azotar al mundo")
            input()

            cambio_mapa = True

            return 8
        
        case _:
            print("Opción no válida")
            input()
            return 0


def main():

    global acompañante 
    global cambio_mapa 
    global objetos 
    global eventos 
    global accion

    pos_x = 0

    intro()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Escribe caminar y despues enter, seguido del numero de camino que quieres tomar")
    print("la iglesia esta por el camino 2")
    print("Estas en la ciudad")
    input()
    cambio_mapa = False
    while cambio_mapa == False:
        print(f"Estas en {pos_x}")
        print(f"caminos disponibles: {inicio[pos_x]}")
        accion = input("Accion: ")

        if accion == "caminar":
            eleccion = input("a donde?: ")
            pos_x = mapa1(eleccion)
            accion = ""
        else:
            print("eleccion no valida")
            os.system('cls' if os.name == 'nt' else 'clear')
            accion = ""
        
        os.system('cls' if os.name == 'nt' else 'clear')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Te encuentras en la entrada del templo de agua")
    input()
    cambio_mapa = False
    pos_x = 0
    while cambio_mapa == False:
        print(f"Estas en {pos_x}")
        print(f"caminos disponibles: {templo_agua[pos_x]}")
        accion = input("Accion: ")

        if accion == "caminar":
            eleccion = input("a donde?: ")
            pos_x = mapa2(eleccion)
            accion = ""
        else:
            print("eleccion no valida")
            os.system('cls' if os.name == 'nt' else 'clear')
            accion = ""
        os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Te encuentras en la entrada del templo de viento")
    input()
    cambio_mapa = False
    pos_x = 0
    while cambio_mapa == False:
        print(f"Estas en {pos_x}")
        print(f"caminos disponibles: {templo_viento[pos_x]}")
        accion = input("Accion: ")

        if accion == "caminar":
            eleccion = input("a donde?: ")
            pos_x = mapa3(eleccion)
            accion = ""
        else:
            print("eleccion no valida")
            os.system('cls' if os.name == 'nt' else 'clear')
            accion = ""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Entrar al portal (7)")
    print("Seguir al hombre misterioso (8)")
    input()
    cambio_mapa = False
    while cambio_mapa == False:
        print(f"Estas en {pos_x}")
        print(f"caminos disponibles: {templo_viento[pos_x]}")
        accion = input("Accion: ")

        if accion == "caminar":
            eleccion = input("a donde?: ")
            pos_x = mapa3(eleccion)
            accion = ""
        else:
            print("eleccion no valida")
            os.system('cls' if os.name == 'nt' else 'clear')
            accion = ""
        os.system('cls' if os.name == 'nt' else 'clear')

    print("FIN")
    input()
    
if __name__ == "__main__":
    main()