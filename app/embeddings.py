import pickle
import pandas as pd
import numpy as np
from scipy.spatial import distance

# Cargar los embeddings y el modelo PCA desde el archivo
with open('app/embeddings.pkl', 'rb') as f:
    data = pickle.load(f)
    titles = data['titles']
    bigram_to_index = data['bigram_to_index']
    reduced_embeddings = data['reduced_embeddings']
    pca = data['pca']

# Crear un DataFrame con las dimensiones reducidas
reduced_df = pd.DataFrame(reduced_embeddings, columns=['PC1', 'PC2', 'PC3'])
reduced_df['title'] = titles

# Función para generar bigramas de una palabra
def generate_bigrams(word):
    return [word[i:i+2] for i in range(len(word) - 1)]

# Crear una función para generar el vector de bigramas para una palabra
def generate_bigram_vector(word, bigram_to_index):
    bigrams = generate_bigrams(word)
    vector = [0] * len(bigram_to_index)
    for bigram in bigrams:
        if bigram in bigram_to_index:
            vector[bigram_to_index[bigram]] = 1
    return vector

# Función para encontrar el punto más cercano
def find_closest_point(new_vector, reduced_embeddings, titles):
    distances = [distance.euclidean(new_vector, vec) for vec in reduced_embeddings]
    min_index = np.argmin(distances)
    return titles[min_index], distances[min_index], min_index

# Crear los datos iniciales para Plotly
def get_initial_data():
    return [
        {
            'x': reduced_df['PC1'].tolist(),
            'y': reduced_df['PC2'].tolist(),
            'z': reduced_df['PC3'].tolist(),
            'text': reduced_df['title'].tolist(),
            'mode': 'markers',
            'type': 'scatter3d',
            'marker': {'size': 3}
        }
    ]
