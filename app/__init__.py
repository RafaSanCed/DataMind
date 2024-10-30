from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_mapping(
        SECRET_KEY='dev',
        # Agrega otras configuraciones si es necesario
    )

    # Importar y registrar rutas
    from .routes import init_routes
    init_routes(app)

    return app
