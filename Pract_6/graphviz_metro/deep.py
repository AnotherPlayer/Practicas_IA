import csv
import networkx as nx
import matplotlib.pyplot as plt

def cargar_grafo(archivo_csv):
    """
    Lee el archivo CSV con columnas: Estacion_Origen, Estacion_Destino, Linea, Distancia
    y construye un grafo no dirigido con pesos (ignora la columna 'Linea').
    """
    G = nx.Graph()
    with open(archivo_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            origen = fila['Estacion_Origen'].strip()
            destino = fila['Estacion_Destino'].strip()
            distancia = float(fila['Distancia'])
            # Añadir arista con peso (el grafo es no dirigido)
            G.add_edge(origen, destino, weight=distancia)
    return G

def dibujar_grafo(G):
    """
    Muestra el grafo en una ventana usando matplotlib.
    """
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, k=0.5, iterations=50)  # distribución para visualizar
    nx.draw_networkx_nodes(G, pos, node_size=50, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=6)
    plt.title("Red de Metro de Madrid")
    plt.axis('off')
    plt.show()

def heuristic_zero(u, v):
    """
    Heurística nula para A* (lo convierte en Dijkstra).
    """
    return 0

def main():
    archivo = "MetroMadrid.csv"  # Nombre del archivo proporcionado
    print("Cargando grafo...")
    G = cargar_grafo(archivo)
    print(f"Grafo cargado: {G.number_of_nodes()} estaciones, {G.number_of_edges()} conexiones.")

    # Mostrar el grafo (opcional, puede tardar un poco)
    print("Generando visualización del grafo...")
    dibujar_grafo(G)

    # Lista de estaciones para referencia
    estaciones = list(G.nodes)
    print("\nEstaciones disponibles (primeras 10):")
    for e in estaciones[:10]:
        print(f"  - {e}")
    print("...")

    while True:
        print("\n--- Calculadora de ruta ---")
        origen = input("Estación de origen: ").strip()
        destino = input("Estación de destino: ").strip()

        if origen not in G or destino not in G:
            print("Una o ambas estaciones no existen. Intente de nuevo.")
            continue

        print("Seleccione algoritmo:")
        print("1. Dijkstra")
        print("2. A* (con heurística nula)")
        opcion = input("Opción (1/2): ").strip()

        try:
            if opcion == '1':
                path = nx.dijkstra_path(G, origen, destino, weight='weight')
                distancia = nx.dijkstra_path_length(G, origen, destino, weight='weight')
            elif opcion == '2':
                path = nx.astar_path(G, origen, destino, heuristic=heuristic_zero, weight='weight')
                distancia = nx.astar_path_length(G, origen, destino, heuristic=heuristic_zero, weight='weight')
            else:
                print("Opción no válida.")
                continue

            print(f"\nRuta encontrada ({len(path)} estaciones):")
            print(" -> ".join(path))
            print(f"Distancia total: {distancia:.3f} km")

        except nx.NetworkXNoPath:
            print("No hay ruta entre las estaciones indicadas.")
        except Exception as e:
            print(f"Error: {e}")

        continuar = input("\n¿Calcular otra ruta? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()