from easygui import fileopenbox
from PIL import Image

ruta = fileopenbox(msg="Seleccione Archivo", title="Seleccione Archivo JSON", filetypes=["*.json"])

img = Image.open(ruta)

# Se lee la imagen de entrada
img_rgb = img.convert("RGB")

# Se crea una imagen por cada color
img_nueva_rojo = Image.new(mode="RGB", size=(img_rgb.width, img_rgb.height))
img_nueva_verde = Image.new(mode="RGB", size=(img_rgb.width, img_rgb.height))
img_nueva_azul = Image.new(mode="RGB", size=(img_rgb.width, img_rgb.height))

# Iteramos por cada una de las imagenes pixel por pixel
for x in range(0,img_rgb.width):
    for y in range(0,img_rgb.height):
        rojo, verde, azul = img_rgb.getpixel((x,y)) #Obtenemos la participación de cada color
        img_nueva_rojo.putpixel((x,y), (rojo, 0, 0)) #Dejamos unicamente la participación del rojo en la imagen roja
        img_nueva_verde.putpixel((x,y), (0, verde, 0))#Dejamos unicamente la participación del verde en la imagen verde
        img_nueva_azul.putpixel((x,y), (0, 0, azul)) #Dejamos unicamente la participación del azul en la imagen azul


#Salvamos las imagenes
img_nueva_rojo.save('rojo.jpg')
img_nueva_verde.save('verde.jpg')
img_nueva_azul.save('azul.jpg')