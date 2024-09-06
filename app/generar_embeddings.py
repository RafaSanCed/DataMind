import requests
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import pickle

# Función para generar bigramas de una palabra
def generate_bigrams(word):
    return [word[i:i+2] for i in range(len(word) - 1)]

# Función para obtener datos de razas de perros de The Dog API
def fetch_dog_breeds(limit=100):
    url = 'https://api.thedogapi.com/v1/breeds'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        titles = [breed['name'] for breed in data[:limit]]
        return titles
    else:
        print("Error fetching data from The Dog API")
        return []

# Obtener nombres de razas de perros
titles = fetch_dog_breeds(100)

# Crear un conjunto de todos los bigramas en la base de datos
all_bigrams = set()
for title in titles:
    bigrams = generate_bigrams(title)
    all_bigrams.update(bigrams)

# Crear un diccionario de bigramas con índices únicos
bigram_to_index = {bigram: idx for idx, bigram in enumerate(all_bigrams)}

# Crear una función para generar el vector de bigramas para una palabra
def generate_bigram_vector(word, bigram_to_index):
    bigrams = generate_bigrams(word)
    vector = [0] * len(bigram_to_index)
    for bigram in bigrams:
        if bigram in bigram_to_index:
            vector[bigram_to_index[bigram]] = 1
    return vector

# Generar los vectores de bigramas para todos los nombres
title_vectors = {title: generate_bigram_vector(title, bigram_to_index) for title in titles}

# Convertir el diccionario de embeddings a un DataFrame
title_vectors_df = pd.DataFrame.from_dict(title_vectors, orient='index')

# Aplicar PCA para reducir los embeddings a 3 dimensiones
pca = PCA(n_components=3)
reduced_embeddings = pca.fit_transform(title_vectors_df)

# Guardar los embeddings y PCA en un archivo
with open('embeddings.pkl', 'wb') as f:
    pickle.dump({
        'titles': titles,
        'bigram_to_index': bigram_to_index,
        'reduced_embeddings': reduced_embeddings,
        'pca': pca
    }, f)

print("Embeddings and PCA model saved successfully.")
