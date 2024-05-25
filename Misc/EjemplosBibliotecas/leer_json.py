from easygui import fileopenbox
import json

# Mostramos el menú para abrir el archivo JSON
ruta = fileopenbox(msg="Seleccione Archivo", title="Seleccione Archivo JSON", filetypes=["*.json"])

with open(ruta, "r") as archivo:
    contenido_json = archivo.read() #Leemos el archivo

dic_productos = json.loads(contenido_json) #Lo convertimos a un diccionario

for producto in dic_productos:
    print(f"Nombre del producto: {producto['name']}")