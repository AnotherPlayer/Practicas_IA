import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
import numpy as np
from collections import defaultdict

# ------------------------------------------------------------
# 1. Cargar el archivo de distancias
# ------------------------------------------------------------
csv_path = '/home/tetuan/Documentos/Personal/ESCOM/IA/Pract_6/Testing/distancias_metro_madrid.csv'

if not os.path.exists(csv_path):
    print(f"❌ No se encuentra el archivo: {csv_path}")
    exit(1)

df = pd.read_csv(csv_path)
print(f"✅ CSV cargado: {len(df)} tramos")

# ------------------------------------------------------------
# 2. Construir el grafo
# ------------------------------------------------------------
G = nx.Graph()

for _, row in df.iterrows():
    u = str(row['Estacion1']).strip()
    v = str(row['Estacion2']).strip()
    linea = str(row['Linea']).strip()
    dist = float(row['Distancia_km'])

    if G.has_edge(u, v):
        G.edges[u, v]['lineas'].append(linea)
        if abs(G.edges[u, v]['distancia_km'] - dist) > 1e-6:
            print(f"⚠️  Discrepancia en distancia para {u}-{v}: {G.edges[u,v]['distancia_km']} vs {dist}")
    else:
        G.add_edge(u, v, distancia_km=dist, lineas=[linea])

    # Guardar línea principal en el nodo si no tiene
    for node in [u, v]:
        if node not in G.nodes or 'linea_principal' not in G.nodes[node]:
            G.nodes[node]['linea_principal'] = linea

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

print(f"\n📊 Estadísticas del grafo:")
print(f"   Estaciones únicas : {num_estaciones}")
print(f"   Tramos físicos    : {num_tramos}")
print(f"   Longitud total    : {total_km:.2f} km")
print(f"   Longitud media    : {media_km:.3f} km")
print(f"   Tramo más largo   : {max_km:.3f} km")
print(f"   Tramo más corto   : {min_km:.3f} km")

print("\n🔍 Ejemplos de tramos:")
for i, (u, v, data) in enumerate(G.edges(data=True)):
    if i >= 5: break
    lineas_str = ', '.join(map(str, data['lineas']))
    print(f"   {u} — {v} : {data['distancia_km']} km (líneas: {lineas_str})")

# ------------------------------------------------------------
# 4. Paleta de colores por línea (colores oficiales Metro Madrid)
# ------------------------------------------------------------
COLORES_LINEA = {
    '1':  '#00AAEF',   # Azul claro
    '2':  '#E0001B',   # Rojo
    '3':  '#FFD700',   # Amarillo
    '4':  '#6E4B7B',   # Marrón/morado
    '5':  '#009A44',   # Verde
    '6':  '#929497',   # Gris (circular)
    '7':  '#F47920',   # Naranja
    '8':  '#E91E8C',   # Rosa
    '9':  '#9B1C6E',   # Morado oscuro
    '10': '#1A3E72',   # Azul oscuro
    '11': '#008000',   # Verde oscuro
    '12': '#A8C800',   # Verde lima
    'R':  '#C0392B',   # Ramal
}

def get_color_linea(linea):
    return COLORES_LINEA.get(str(linea), '#888888')

# ------------------------------------------------------------
# 5. Calcular posiciones con spring_layout escalado por componente
# ------------------------------------------------------------
# Usamos spring layout con pesos invertidos (más distancia = resorte más largo)
# para que la topología refleje mejor la geografía

# Construir posición con spring layout usando semilla fija para reproducibilidad
# El peso en spring_layout funciona al revés: mayor peso = más juntos
# Queremos que mayor distancia = más separados, por eso usamos 1/dist
for u, v in G.edges():
    d = G.edges[u, v]['distancia_km']
    G.edges[u, v]['peso_layout'] = 1.0 / (d + 0.001)

pos = nx.spring_layout(
    G,
    weight='peso_layout',
    k=2.5,          # distancia ideal entre nodos
    iterations=200,
    seed=42
)

# ------------------------------------------------------------
# 6. Determinar color de cada nodo (línea con más apariciones)
# ------------------------------------------------------------
# Contar apariciones de cada línea por estación
estacion_lineas = defaultdict(list)
for _, row in df.iterrows():
    for est in [str(row['Estacion1']).strip(), str(row['Estacion2']).strip()]:
        estacion_lineas[est].append(str(row['Linea']).strip())

def linea_predominante(estacion):
    lineas = estacion_lineas[estacion]
    return max(set(lineas), key=lineas.count)

node_colors = [get_color_linea(linea_predominante(n)) for n in G.nodes()]

# Nodos de transbordo (grado alto) en blanco con borde negro
node_sizes = []
node_edge_colors = []
for n in G.nodes():
    deg = G.degree(n)
    if deg >= 4:
        node_sizes.append(80)
        node_edge_colors.append('black')
    elif deg == 3:
        node_sizes.append(45)
        node_edge_colors.append('#333333')
    else:
        node_sizes.append(18)
        node_edge_colors.append('none')

# ------------------------------------------------------------
# 7. Color de cada arista según su línea (o multicolor si varias)
# ------------------------------------------------------------
edge_colors = []
edge_widths = []
for u, v, data in G.edges(data=True):
    lineas = data['lineas']
    if len(lineas) == 1:
        edge_colors.append(get_color_linea(lineas[0]))
        edge_widths.append(1.2)
    else:
        # Tramo compartido: usar gris oscuro y más grueso
        edge_colors.append('#444444')
        edge_widths.append(2.0)

# ------------------------------------------------------------
# 8. Etiquetas: solo estaciones de transbordo o alta conectividad
# ------------------------------------------------------------
umbral_etiqueta = 4  # grado mínimo para etiquetar
etiquetas = {n: n for n in G.nodes() if G.degree(n) >= umbral_etiqueta}

# ------------------------------------------------------------
# 9. Visualización final
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(22, 18))
fig.patch.set_facecolor('#1a1a2e')
ax.set_facecolor('#1a1a2e')

# — Aristas —
nx.draw_networkx_edges(
    G, pos,
    edge_color=edge_colors,
    width=edge_widths,
    alpha=0.75,
    ax=ax
)

# — Nodos —
nx.draw_networkx_nodes(
    G, pos,
    node_color=node_colors,
    node_size=node_sizes,
    edgecolors=node_edge_colors,
    linewidths=0.8,
    ax=ax
)

# — Etiquetas de transbordos —
nx.draw_networkx_labels(
    G, pos,
    labels=etiquetas,
    font_size=6,
    font_color='white',
    font_weight='bold',
    ax=ax,
    bbox=dict(
        boxstyle='round,pad=0.15',
        facecolor='#1a1a2e',
        edgecolor='none',
        alpha=0.7
    )
)

# — Leyenda de líneas —
lineas_presentes = sorted(df['Linea'].astype(str).unique())
leyenda_patches = [
    mpatches.Patch(
        color=get_color_linea(l),
        label=f'Línea {l}'
    )
    for l in lineas_presentes
]
legend = ax.legend(
    handles=leyenda_patches,
    loc='lower left',
    ncol=2,
    fontsize=8,
    framealpha=0.85,
    facecolor='#0f0f1a',
    edgecolor='#555555',
    labelcolor='white',
    title='Líneas',
    title_fontsize=9
)
legend.get_title().set_color('white')

# — Estadísticas en esquina superior —
stats_text = (
    f"Estaciones: {num_estaciones}   |   "
    f"Tramos: {num_tramos}   |   "
    f"Red total: {total_km:.1f} km"
)
ax.text(
    0.5, 0.98, stats_text,
    transform=ax.transAxes,
    ha='center', va='top',
    fontsize=9, color='#aaaacc',
    fontfamily='monospace'
)

# — Título —
ax.set_title(
    "Red de Metro de Madrid",
    fontsize=18,
    fontweight='bold',
    color='white',
    pad=16
)

ax.axis('off')
plt.tight_layout()

# Guardar imagen
output_path = '/home/tetuan/Documentos/Personal/ESCOM/IA/Pract_6/Testing/metro_madrid_grafo.png'
plt.savefig(output_path, dpi=180, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"\n🖼️  Grafo guardado en: {output_path}")
plt.show()

# ------------------------------------------------------------
# 10. Guardar grafo en GML
# ------------------------------------------------------------
gml_path = '/home/tetuan/Documentos/Personal/ESCOM/IA/Pract_6/Testing/metro_madrid.gml'
nx.write_gml(G, gml_path)
print(f"💾 Grafo GML guardado en: {gml_path}")
