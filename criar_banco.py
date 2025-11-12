from db_config import app, db
import models.models 

with app.app_context():
    print("Iniciando a criação do banco de dados...")
    db.create_all()
    print("Banco de dados 'database.db' e tabelas criados com sucesso!")