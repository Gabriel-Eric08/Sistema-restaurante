from db_config import app
import models.models
from flask import Blueprint
from routes.login import login_bp
from routes.home import home_bp
from routes.funcionario import funcionario_bp
from routes.produto import produto_bp
from routes.categoria import categoia_bp
from routes.mesa import mesa_bp
from routes.comanda import comanda_bp
from routes.pedido import pedido_bp

app.register_blueprint(login_bp)
app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(funcionario_bp, url_prefix='/funcionario')
app.register_blueprint(produto_bp, url_prefix='/produto')
app.register_blueprint(categoia_bp, url_prefix='/categoria')
app.register_blueprint(mesa_bp, url_prefix='/mesa')
app.register_blueprint(comanda_bp, url_prefix='/comanda')
app.register_blueprint(pedido_bp, url_prefix='/pedido')

if __name__ == "__main__":
    print("Iniciando o servidor Flask...")
    app.run(port=80, debug=True)