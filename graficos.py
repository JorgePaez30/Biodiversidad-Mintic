import json
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo JSON
with open('datos.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

# Filtrar las observaciones para aquellas que tienen "Boyaca" en el campo "Habitat"
observaciones_filtradas = [obs for obs in datos if 'Boyaca' in obs['Habitat']]

# Contar las especies por tipo
conteo_tipos = {}
for obs in observaciones_filtradas:
    tipo = obs['Tipo']
    if tipo in conteo_tipos:
        conteo_tipos[tipo] += 1
    else:
        conteo_tipos[tipo] = 1

# Preparar los datos para la gráfica circular
nombres = list(conteo_tipos.keys())
valores = list(conteo_tipos.values())

# Crear la gráfica circular
plt.figure(figsize=(8, 6))
plt.pie(valores, labels=nombres, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de especies por tipo en Boyacá')
plt.axis('equal')  # Asegurar que el gráfico sea un círculo
# Guardar la gráfica como archivo de imagen
plt.savefig('distribucion_especies_boyaca.png')
plt.show()

# Filtrar las observaciones para aquellas que tienen "Cundinamarca" en el campo "Habitat"
observaciones_filtradas = [obs for obs in datos if 'Cundinamarca' in obs['Habitat']]

# Contar las especies por tipo
conteo_tipos = {}
for obs in observaciones_filtradas:
    tipo = obs['Tipo']
    if tipo in conteo_tipos:
        conteo_tipos[tipo] += 1
    else:
        conteo_tipos[tipo] = 1

# Preparar los datos para la gráfica circular
nombres = list(conteo_tipos.keys())
valores = list(conteo_tipos.values())

# Crear la gráfica circular
plt.figure(figsize=(8, 6))
plt.pie(valores, labels=nombres, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de especies por tipo en Cundinamarca')
plt.axis('equal')  # Asegurar que el gráfico sea un círculo
plt.savefig('distribucion_especies_cundinamarca.png')
plt.show()


