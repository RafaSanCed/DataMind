
# Proyecto de Machine Learning con Embeddings

Este proyecto está enfocado en la generación y uso de embeddings para el procesamiento de datos en aplicaciones de machine learning. Utiliza Flask como backend para crear rutas que interactúan con los embeddings generados. Los embeddings son útiles para representar datos textuales o de imágenes en un formato numérico que los modelos de machine learning pueden procesar.

## Características
- Generación de embeddings con `generar_embeddings.py`.
- Almacenamiento y carga de embeddings con `embeddings.py` y `embeddings.pkl`.
- Un servidor Flask con rutas definidas en `routes.py` para interactuar con los embeddings.
  
## Archivos Principales

1. **`__init__.py`**: Archivo principal de la aplicación Flask, que inicializa el servidor y define su estructura.
2. **`embeddings.py`**: Contiene la lógica para manejar los embeddings generados, así como funciones para cargarlos y manipularlos.
3. **`embeddings.pkl`**: Archivo binario que contiene los embeddings preprocesados.
4. **`generar_embeddings.py`**: Script encargado de generar embeddings a partir de datos. Este script convierte datos textuales o de otro tipo en vectores numéricos utilizando modelos preentrenados o técnicas específicas.
5. **`routes.py`**: Define las rutas del servidor Flask que permiten interactuar con los embeddings. A través de estas rutas, los usuarios pueden consultar o actualizar los embeddings.

## Requisitos

- **Python 3.x**
- Paquetes necesarios listados en `requirements.txt` (si no lo tienes, asegúrate de crear uno incluyendo Flask y las bibliotecas para generar embeddings).

Ejemplo de cómo crear el archivo `requirements.txt`:
```txt
Flask
pickle
numpy
scikit-learn
# Añadir cualquier otra dependencia que estés usando
```

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repo.git
   cd nombre-del-repo
   ```

2. **Crear un entorno virtual** (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   Ejecuta el servidor Flask:
   ```bash
   python -m flask run
   ```

   O bien, ejecuta el archivo principal `__init__.py`:
   ```bash
   python __init__.py
   ```

## Uso

El proyecto utiliza un servidor Flask con varias rutas para interactuar con los embeddings. Una vez que el servidor esté ejecutándose, puedes acceder a las rutas expuestas por la API.

Ejemplo de rutas expuestas (basado en `routes.py`):
- **`/generate_embeddings`**: Genera nuevos embeddings a partir de los datos suministrados.
- **`/get_embedding/<id>`**: Recupera el embedding correspondiente a un identificador específico.

## Contribuciones

Si deseas contribuir al proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tus cambios: `git checkout -b feature/nueva-funcionalidad`.
3. Haz commit de tus cambios: `git commit -m 'Añadir nueva funcionalidad'`.
4. Empuja la rama: `git push origin feature/nueva-funcionalidad`.
5. Envía un Pull Request.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
