import csv
import heapq
import math
import os
import subprocess
import sys
from collections import defaultdict
from PIL import Image  # Necesario para mostrar la imagen (instalar con pip install pillow)

def cargar_grafo(archivo_csv):
    grafo = defaultdict(list)
    with open(archivo_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            origen = fila['Estacion_Origen'].strip()
            destino = fila['Estacion_Destino'].strip()
            distancia = float(fila['Distancia'])
            # Grafo no dirigido: añadir ambas direcciones
            grafo[origen].append((destino, distancia))
            grafo[destino].append((origen, distancia))
    return grafo

def obtener_estaciones(grafo):
    return list(grafo.keys())

def dijkstra(grafo, inicio, fin):
    """
    Implementación del algoritmo de Dijkstra.
    Devuelve (ruta, distancia) o (None, inf) si no hay camino.
    """
    dist = {nodo: math.inf for nodo in grafo}
    prev = {nodo: None for nodo in grafo}
    dist[inicio] = 0
    pq = [(0, inicio)]  # (distancia, nodo)

    while pq:
        d_actual, nodo = heapq.heappop(pq)
        if nodo == fin:
            break
        if d_actual > dist[nodo]:
            continue
        for vecino, peso in grafo[nodo]:
            nueva_dist = d_actual + peso
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                prev[vecino] = nodo
                heapq.heappush(pq, (nueva_dist, vecino))

    # Reconstruir camino
    if dist[fin] == math.inf:
        return None, math.inf
    camino = []
    nodo = fin
    while nodo is not None:
        camino.append(nodo)
        nodo = prev[nodo]
    camino.reverse()
    return camino, dist[fin]

def a_star(grafo, inicio, fin, heuristica=None):
    """
    Implementación del algoritmo A*.
    Por defecto usa heurística nula (equivalente a Dijkstra).
    Devuelve (ruta, distancia) o (None, inf) si no hay camino.
    """
    if heuristica is None:
        heuristica = lambda u, v: 0  # heurística nula

    dist = {nodo: math.inf for nodo in grafo}
    prev = {nodo: None for nodo in grafo}
    dist[inicio] = 0
    # Cola de prioridad con (f = dist_real + heuristica, nodo)
    pq = [(heuristica(inicio, fin), inicio)]

    while pq:
        f_actual, nodo = heapq.heappop(pq)
        if nodo == fin:
            break
        # Calcular el costo real hasta el nodo (g)
        g_actual = dist[nodo]
        for vecino, peso in grafo[nodo]:
            nueva_g = g_actual + peso
            if nueva_g < dist[vecino]:
                dist[vecino] = nueva_g
                prev[vecino] = nodo
                nueva_f = nueva_g + heuristica(vecino, fin)
                heapq.heappush(pq, (nueva_f, vecino))

    if dist[fin] == math.inf:
        return None, math.inf
    camino = []
    nodo = fin
    while nodo is not None:
        camino.append(nodo)
        nodo = prev[nodo]
    camino.reverse()
    return camino, dist[fin]

def dibujar_grafo(grafo, nombre_archivo='MetrobusMexico'):
    """
    Genera una representación gráfica del grafo usando Graphviz.
    Guarda la imagen como PNG y la abre con el visor predeterminado.
    """
    try:
        from graphviz import Graph
    except ImportError:
        print("Error: No está instalada la librería graphviz. Instálala con: pip install graphviz")
        sys.exit(1)

    # Crear un grafo no dirigido
    dot = Graph(comment='Metrobus de México', engine='sfdp', format='png')  # sfdp es mejor para grafos grandes
    dot.attr(overlap='false', splines='true', nodesep='0.3', ranksep='0.2')

    # Añadir nodos (sin atributos especiales)
    for nodo in grafo:
        dot.node(nodo, nodo, fontsize='8', shape='circle', width='0.3', height='0.3')

    # Añadir aristas (sin peso, solo conexión)
    # Usamos un conjunto para evitar duplicar aristas (porque el grafo es no dirigido)
    aristas_vistas = set()
    for origen, vecinos in grafo.items():
        for destino, peso in vecinos:
            if (origen, destino) not in aristas_vistas and (destino, origen) not in aristas_vistas:
                dot.edge(origen, destino, label=f'{peso:.2f} km', fontsize='6')
                aristas_vistas.add((origen, destino))

    # Renderizar a archivo PNG
    output_path = dot.render(filename=nombre_archivo, cleanup=True)
    print(f"Grafo guardado en: {output_path}")

    # Mostrar la imagen con PIL
    try:
        img = Image.open(output_path)
        img.show()
    except Exception as e:
        print(f"No se pudo mostrar la imagen automáticamente: {e}")
        print(f"Puedes abrir manualmente el archivo: {output_path}")

def main():
    archivo = "MetrobusMexico.csv"
    print("Cargando grafo...")
    grafo = cargar_grafo(archivo)
    estaciones = obtener_estaciones(grafo)
    print(f"Grafo cargado: {len(estaciones)} estaciones, {sum(len(v) for v in grafo.values()) // 2} conexiones.")

    # Visualizar el grafo (opcional, puede tardar)
    print("Generando visualización del grafo con Graphviz...")
    dibujar_grafo(grafo)

    # Mostrar algunas estaciones de ejemplo
    print("\nEstaciones disponibles (primeras 10):")
    for e in estaciones[:10]:
        print(f"  - {e}")
    print("...")

    while True:
        print("\n--- Calculadora de ruta ---")
        origen = input("Estación de origen: ").strip()
        destino = input("Estación de destino: ").strip()

        if origen not in grafo or destino not in grafo:
            print("Una o ambas estaciones no existen. Intente de nuevo.")
            continue

        print("Seleccione algoritmo:")
        print("1. Dijkstra")
        print("2. A* (con heurística nula)")
        opcion = input("Opción (1/2): ").strip()

        try:
            if opcion == '1':
                camino, distancia = dijkstra(grafo, origen, destino)
            elif opcion == '2':
                camino, distancia = a_star(grafo, origen, destino)
            else:
                print("Opción no válida.")
                continue

            if camino is None:
                print("No hay ruta entre las estaciones indicadas.")
            else:
                print(f"\nRuta encontrada ({len(camino)} estaciones):")
                print(" -> ".join(camino))
                print(f"Distancia total: {distancia:.3f} km")
        except Exception as e:
            print(f"Error: {e}")

        continuar = input("\n¿Calcular otra ruta? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()