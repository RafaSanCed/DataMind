from flask import Flask
from app.routes import init_routes  

app = Flask(__name__)

# Registra las rutas
init_routes(app)

if __name__ == '__main__':
    app.run(port=5000)
