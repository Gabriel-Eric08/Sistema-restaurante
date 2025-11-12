import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

# 2. Criar a instância principal do aplicativo Flask
app = Flask(__name__)

# 3. Configurar o aplicativo
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')

# 4. Criar a instância do SQLAlchemy, ligando-a ao aplicativo Flask
db = SQLAlchemy(app)