import os
import cv2
import numpy as np
import math
import requests
import shutil

# Ruta donde se guardarán las imágenes
IMAGES_FOLDER = 'tiles/'

if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)

# Función para convertir latitud y longitud a coordenadas de tile
def latlng_to_tile(lat, lng, zoom):
    x = int((lng + 180) / 360 * (2**zoom))
    y = int((1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * (2**zoom))
    return x, y

# Función para descargar el mosaico (tile) desde Google Maps
def download_google_tile(x, y, z, filename):
    if os.path.exists(filename):
        print(f"Tile {filename} encontrado en caché.")
        return
 
    url = f"https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(f"Error al descargar el tile. Código de estado: {response.status_code}")

# Función para limpiar la carpeta de imágenes
def limpiar_carpeta_imagenes():
    if os.path.exists(IMAGES_FOLDER):
        shutil.rmtree(IMAGES_FOLDER)
    os.makedirs(IMAGES_FOLDER)

# Función para calcular el porcentaje de vegetación en la imagen
def calcular_porcentaje_vegetacion(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    green_lower = np.array([54, 30, 0])
    green_upper = np.array([170, 255, 255])
    mask = cv2.inRange(hsv_image, green_lower, green_upper)
    total_pixels = image.shape[0] * image.shape[1]
    green_pixels = cv2.countNonZero(mask)
    green_percentage = (green_pixels / total_pixels) * 100
    return green_percentage
