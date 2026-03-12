import pandas as pd
import numpy as np
import os

# ------------------------------------------------------------
# 1. Función haversine
# ------------------------------------------------------------
def haversine(lon1, lat1, lon2, lat2):
    """
    Calcula la distancia en kilómetros entre dos puntos
    de la Tierra especificados por longitud y latitud en grados.
    """
    R = 6371  # Radio de la Tierra en km
    # Convertir a radianes
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c

# ------------------------------------------------------------
# 2. Cargar datos
# ------------------------------------------------------------
# Si el script está en la misma carpeta que el CSV, usamos ruta relativa
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'metro_madrid_completo.csv')

# Si no, cambia la ruta o coloca el archivo en el mismo directorio
df = pd.read_csv(csv_path)

# ------------------------------------------------------------
# 3. Calcular distancias por línea
# ------------------------------------------------------------
resultados = []  # Lista para guardar cada tramo

for linea, grupo in df.groupby('Linea'):
    estaciones = grupo['Estación'].tolist()
    coords = list(zip(grupo['x'], grupo['y']))  # (lon, lat)

    for i in range(len(estaciones) - 1):
        est1 = estaciones[i]
        est2 = estaciones[i+1]
        lon1, lat1 = coords[i]
        lon2, lat2 = coords[i+1]

        dist = haversine(lon1, lat1, lon2, lat2)

        resultados.append({
            'Linea': linea,
            'Estacion1': est1,
            'Estacion2': est2,
            'Distancia_km': round(dist, 3)
        })

# Convertir a DataFrame para facilitar el análisis
df_distancias = pd.DataFrame(resultados)

# ------------------------------------------------------------
# 4. Mostrar resumen
# ------------------------------------------------------------
print("📏 Distancias entre estaciones consecutivas por línea:")
print(df_distancias.head(10))  # Mostrar los primeros 10

print("\n📊 Estadísticas globales:")
total_km = df_distancias['Distancia_km'].sum()
media_km = df_distancias['Distancia_km'].mean()
max_km = df_distancias['Distancia_km'].max()
min_km = df_distancias['Distancia_km'].min()

print(f"   Distancia total de la red: {total_km:.2f} km")
print(f"   Distancia media por tramo: {media_km:.3f} km")
print(f"   Tramo más largo: {max_km:.3f} km")
print(f"   Tramo más corto: {min_km:.3f} km")

# ------------------------------------------------------------
# 5. (Opcional) Guardar resultados en un nuevo CSV
# ------------------------------------------------------------
df_distancias.to_csv('distancias_metro_madrid.csv', index=False)
print("\n✅ Resultados guardados en 'distancias_metro_madrid.csv'")