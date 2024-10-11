from flask import render_template, request, jsonify
from .embeddings import generate_bigram_vector, find_closest_point, get_initial_data, pca, reduced_embeddings, titles, bigram_to_index
import json
from .geogreen_processing import latlng_to_tile, download_google_tile, limpiar_carpeta_imagenes, calcular_porcentaje_vegetacion  # Importamos las funciones del archivo de procesamiento
import os

def init_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/predictions')
    def predictions():
        return render_template('predictions.html')

    @app.route('/blog')
    def blog():
        return render_template('blog.html')

    @app.route('/historIA')
    def historIA():
        return render_template('historIA.html')

    @app.route('/visualize', methods=['GET', 'POST'])
    def visualize():
        if request.method == 'POST':
            # Manejo de POST para cuando se introduce texto
            new_text = request.form['text_input']
            new_vector = generate_bigram_vector(new_text, bigram_to_index)
            new_reduced_vector = pca.transform([new_vector])[0]
        
            closest_title, closest_distance, closest_index = find_closest_point(new_reduced_vector, reduced_embeddings, titles)
        
            # Solo devuelve los datos relevantes (limpios) al frontend para renderizar la nueva gráfica
            return jsonify({
                "new_vector": new_reduced_vector.tolist(),
                "closest_title": str(closest_title),
                "closest_distance": float(closest_distance),
                "closest_index": int(closest_index)
            })
        else:
            # Preparar datos para el gráfico inicial
            initial_data = get_initial_data()  # Función que convierte los embeddings en un formato procesable para Plotly
            initial_data_json = json.dumps(initial_data)  # Convertir initial_data a JSON string
            return render_template('visualize.html', initial_data=initial_data_json)
        
    @app.route('/GeoGreenView')
    def geogreen():
        return render_template('geogreen.html')
    
    @app.route('/process_tile', methods=['POST'])
    def process_tile():
        try:
            data = request.json
            lat = data['lat']
            lng = data['lng']
            zoom = 15

            # Convertir a coordenadas de tile
            x, y = latlng_to_tile(lat, lng, zoom)

            # Descargar el tile y guardarlo en la carpeta
            tile_path = os.path.join('tiles/', f"tile_{x}_{y}.png")
            download_google_tile(x, y, zoom, tile_path)

            # Calcular el porcentaje de vegetación
            porcentaje_vegetacion = calcular_porcentaje_vegetacion(tile_path)

            return jsonify({'porcentaje_vegetacion': porcentaje_vegetacion})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/start_analysis', methods=['POST'])
    def start_analysis():
        try:
            # Limpiar las imágenes antes de realizar el análisis
            limpiar_carpeta_imagenes()
            return jsonify({'message': 'Carpeta limpiada con éxito, lista para nuevo análisis'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500