from flask import Flask
from app.routes import init_routes  # Importa `init_routes` desde la carpeta `app`

app = Flask(__name__)

# Configuración de la aplicación
app.config.from_mapping(
    SECRET_KEY='dev',
    # Otras configuraciones si es necesario
)

# Registra las rutas
init_routes(app)

if __name__ == '__main__':
    app.run(port=5000)
