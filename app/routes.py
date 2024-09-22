from flask import render_template, request, jsonify
from .embeddings import generate_bigram_vector, find_closest_point, get_initial_data, pca, reduced_embeddings, titles, bigram_to_index
import json

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