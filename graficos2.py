import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo JSON
with open('datos.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

df_especies = pd.DataFrame(datos)

# Cantidad de especies en Cundinamarca por tipo
df_cundinamarca = df_especies[df_especies['Habitat'].str.contains('Cundinamarca', case=False, na=False)]
def contar(nombre, vec):
#Para esta funcion nombre es el criterio para contar (nombre) y vec es la lista donde contar
    contador=0
    for i in vec:
        if i==nombre:
            contador+=1
    return contador
#etiquetas únicas en tipo
lista_tipo = df_cundinamarca['Tipo'].unique()
lista_habitat = df_cundinamarca['Habitat'].unique()
lista_tipo_especie = list(df_cundinamarca['Tipo'])
lista_tipo_habitat = list(df_cundinamarca['Habitat'])
#Armar otra lista con el conteo
lista_valores=[]
for elemento in lista_tipo:
    cantidad=contar(elemento,lista_tipo_especie)
    lista_valores.append(cantidad)
#Diagrama de barras
colores = plt.cm.tab20.colors
fig, diagx = plt.subplots(figsize=(10, 6))
barras = diagx.bar(lista_tipo, lista_valores, color=colores[:len(lista_tipo)])
diagx.set_title('Cantidad de Especies por Tipo en Cundinamarca')
diagx.set_xlabel('Tipo de Especie')
diagx.set_ylabel('Cantidad')
# Añadir etiquetas a las barras
for barra in barras:
    yval = barra.get_height()
    diagx.text(barra.get_x() + barra.get_width() / 2, yval, int(yval), ha='center', va='bottom')  
fig.savefig('Cantidad_especies_cundinamarca.png')
plt.show()

#--------------------Crear el gráfico de barras en 3D cundinamarca--------------------------------#
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Datos para el gráfico
x_pos = np.arange(len(lista_tipo))
y_pos = np.zeros(len(lista_tipo))  # Coordenada y es cero para un gráfico de barras simple en 3D
z_pos = np.zeros(len(lista_tipo))  # Coordenada z es cero para un gráfico de barras simple en 3D
dx = np.ones(len(lista_tipo))  # Ancho de las barras en x
dy = np.ones(len(lista_tipo))  # Ancho de las barras en y
dz = lista_valores  # Altura de las barras

# Definir colores para cada tipo
colores = plt.cm.tab20.colors 
# Crear las barras en 3D
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colores[:len(lista_tipo)])

# Añadir títulos y etiquetas
ax.set_title('Cantidad de Especies por Tipo en cundinamarca')
ax.set_xlabel('Tipo de Especie')
ax.set_ylabel('Categoría')
ax.set_zlabel('Cantidad')

# Configurar etiquetas en el eje x
ax.set_xticks(x_pos)
ax.set_xticklabels(lista_tipo, rotation=45, ha='right')

fig.savefig('Cantidad_Especies_Cundinamarca_3D.png')
plt.show()

#----------------------------Sección Boyaca---------------------------------------------------#

# Cantidad de especies en Boyacapor tipo
df_boyaca= df_especies[df_especies['Habitat'].str.contains('Boyaca', case=False, na=False)]
def contar(nombre, vec):
#Para esta funcion nombre es el criterio para contar (nombre) y vec es la lista donde contar
    contador=0
    for i in vec:
        if i==nombre:
            contador+=1
    return contador

#etiquetas únicas en tipo
lista_tipo = df_boyaca['Tipo'].unique()
lista_habitat = df_boyaca['Habitat'].unique()
lista_tipo_especie = list(df_boyaca['Tipo'])
lista_tipo_habitat = list(df_boyaca['Habitat'])

#Armar otra lista con el conteo
lista_valores=[]
for elemento in lista_tipo:
    cantidad=contar(elemento,lista_tipo_especie)
    lista_valores.append(cantidad)

#Diagrama de barras
colores = plt.cm.tab20.colors
fig, diagx = plt.subplots(figsize=(10, 6))
barras = diagx.bar(lista_tipo, lista_valores, color=colores[:len(lista_tipo)])
diagx.set_title('Cantidad de Especies por Tipo en Boyacá')
diagx.set_xlabel('Tipo de Especie')
diagx.set_ylabel('Cantidad')
# Añadir etiquetas a las barras
for barra in barras:
    yval = barra.get_height()
    diagx.text(barra.get_x() + barra.get_width() / 2, yval, int(yval), ha='center', va='bottom')   
fig.savefig('Cantidad_especies_boyaca.png')
plt.show()

#----------------------Crear el gráfico de barras en 3D------------------------------------------#
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Datos para el gráfico
x_pos = np.arange(len(lista_tipo))
y_pos = np.zeros(len(lista_tipo))  # Coordenada y es cero para un gráfico de barras simple en 3D
z_pos = np.zeros(len(lista_tipo))  # Coordenada z es cero para un gráfico de barras simple en 3D
dx = np.ones(len(lista_tipo))  # Ancho de las barras en x
dy = np.ones(len(lista_tipo))  # Ancho de las barras en y
dz = lista_valores  # Altura de las barras

# Definir colores para cada tipo
colores = plt.cm.tab20.colors 
# Crear las barras en 3D
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colores[:len(lista_tipo)])

# Añadir títulos y etiquetas
ax.set_title('Cantidad de Especies por Tipo en Boyacá')
ax.set_xlabel('Tipo de Especie')
ax.set_ylabel('Categoría')
ax.set_zlabel('Cantidad')

# Configurar etiquetas en el eje x
ax.set_xticks(x_pos)
ax.set_xticklabels(lista_tipo, rotation=45, ha='right')

fig.savefig('Cantidad_especies_boyaca_3D.png')
plt.show()