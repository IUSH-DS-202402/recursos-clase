import requests
import json

# Llamamos a la API de pokemon solicitando los primeros 10 pokemones
r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10', verify=False)

# El resultado lo convertimos a un diccionario (Map)
dict_pokemon = r.json()

# Iteramos por cada uno de los resultados
for pokemon in dict_pokemon['results']:
    url_arr = pokemon['url'].split("/") # Tomamos la URL y la partimos para sacar el número del pokemon
    numero = url_arr[-2] # Traemos el número que nos entrega
    print(f"\nNumero: {numero}")
    print(f"Nombre: {pokemon['name']}")

pokemon_json = json.dumps(dict_pokemon['results'], indent=2) #Convertimos el diccionario a JSON

with open("pokemon.json","w") as archivo: # Escribimos el archivo
    archivo.write(pokemon_json)