from db_config import app
import models.models
from flask import Blueprint
from routes.login import login_bp
from routes.home import home_bp

app.register_blueprint(login_bp)
app.register_blueprint(home_bp, url_prefix='/home')

if __name__ == "__main__":
    print("Iniciando o servidor Flask...")
    # Usamos o 'app' importado para rodar a aplicação
    app.run(port=80, debug=True)