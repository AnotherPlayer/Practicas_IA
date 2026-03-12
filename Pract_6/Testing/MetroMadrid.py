import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np

# ------------------------------------------------------------
# 1. Cargar el archivo de distancias
# ------------------------------------------------------------
# Ruta al archivo (ajústala según tu necesidad)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'distancias_metro_madrid.csv')

if not os.path.exists(csv_path):
    print(f"❌ No se encuentra el archivo: {csv_path}")
    exit(1)

df = pd.read_csv(csv_path)

# ------------------------------------------------------------
# 2. Construir el grafo
# ------------------------------------------------------------
G = nx.Graph()

# Diccionario opcional para llevar control de aristas ya procesadas
# (aunque NetworkX ya maneja esto internamente, lo usamos para almacenar líneas)
for _, row in df.iterrows():
    u = row['Estacion1']
    v = row['Estacion2']
    linea = row['Linea']
    dist = row['Distancia_km']

    if G.has_edge(u, v):
        # La arista ya existe: añadimos la línea a la lista
        G.edges[u, v]['lineas'].append(linea)
        # Opcional: comprobar que la distancia coincide
        if abs(G.edges[u, v]['distancia_km'] - dist) > 1e-6:
            print(f"⚠️  Discrepancia en distancia para {u}-{v}: {G.edges[u,v]['distancia_km']} vs {dist}")
    else:
        # Nueva arista: creamos con atributos
        G.add_edge(u, v, distancia_km=dist, lineas=[linea])

# ------------------------------------------------------------
# 3. Estadísticas básicas
# ------------------------------------------------------------
num_estaciones = G.number_of_nodes()
num_tramos = G.number_of_edges()
distancias = [data['distancia_km'] for u, v, data in G.edges(data=True)]
total_km = sum(distancias)
media_km = np.mean(distancias)
max_km = max(distancias)
min_km = min(distancias)

print("✅ Grafo construido correctamente")
print(f"   Estaciones únicas: {num_estaciones}")
print(f"   Tramos físicos (pares de estaciones conectadas): {num_tramos}")
print(f"\n📏 Estadísticas de longitudes (km):")
print(f"   Longitud total de la red: {total_km:.2f} km")
print(f"   Longitud media por tramo: {media_km:.3f} km")
print(f"   Tramo más largo: {max_km:.3f} km")
print(f"   Tramo más corto: {min_km:.3f} km")

# Mostrar algunos ejemplos de aristas con sus líneas
print("\n🔍 Ejemplos de tramos (con líneas que los usan):")
for i, (u, v, data) in enumerate(G.edges(data=True)):
    if i >= 5: break
    lineas_str = ', '.join(map(str, data['lineas']))
    print(f"   {u} - {v} : {data['distancia_km']} km (líneas: {lineas_str})")

# ------------------------------------------------------------
# 4. Visualización mejorada con Kamada-Kawai (basado en distancias)
# ------------------------------------------------------------
plt.figure(figsize=(16, 14))

# Usar Kamada-Kawai con los pesos de distancia para un layout más realista
pos = nx.kamada_kawai_layout(G, weight='distancia_km')

# Dibujar nodos más pequeños y con borde para distinguirlos
nx.draw_networkx_nodes(G, pos, node_size=20, node_color='skyblue', edgecolors='black', linewidths=0.5)

# Dibujar aristas con transparencia y grosor fino
nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.4, edge_color='gray')

# Etiquetar solo estaciones con grado > 2 (como antes) pero con fuente más pequeña
etiquetas = {n: n for n in G.nodes() if G.degree(n) > 2}
nx.draw_networkx_labels(G, pos, labels=etiquetas, font_size=7)

plt.title("Red de Metro de Madrid (layout basado en distancias)", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 5. (Opcional) Guardar el grafo en formato GML para usarlo después
# ------------------------------------------------------------
nx.write_gml(G, "metro_madrid.gml")
print("\n💾 Grafo guardado en 'metro_madrid.gml'")