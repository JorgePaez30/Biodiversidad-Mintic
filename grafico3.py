import json
import pandas as pd
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
fig, diagx = plt.subplots()
diagx.bar(lista_tipo,lista_valores)
fig.savefig('Cantidad_especies_cundinamarca.png')
plt.show()


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
fig, diagx = plt.subplots()
diagx.bar(lista_tipo,lista_valores)
fig.savefig('Cantidad_especies_boyaca.png')
plt.show()