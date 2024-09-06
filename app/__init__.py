from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        # Otras configuraciones aquí si es necesario
    )

    # Importar y registrar rutas
    from .routes import init_routes
    init_routes(app)

    return app
