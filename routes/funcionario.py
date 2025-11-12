from flask import Blueprint, request, jsonify
from services.funcionario_service import FuncionarioService

funcionario_bp = Blueprint('Usuario', __name__)
funcionario_service= FuncionarioService()

@funcionario_bp.route('/')
def login_page():
    return 'Login page!'

@funcionario_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json() 
    if not data:
        return jsonify({
            "sucess":False,
            "message":"Nenhum dado recebido!"
        }), 400
    nome = data.get('nome')
    senha = data.get('senha')
    cargo= data.get('cargo')
    if not nome or not senha or not cargo:
        return jsonify({
            "sucess":False,
            "message":"Os campos nome, senha e cargo são obrigatórios!"
        }),400
    create_user = funcionario_service.create_user(nome,senha,cargo)
    if create_user:
        return jsonify({
            "sucess":True,
            "message": "Funcionário cadstrado com sucesso!"
        })
    return jsonify({
        "sucess": False,
        "message": "Erro ao cadastrar usuário"
    }), 500


    