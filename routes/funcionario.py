from flask import Blueprint, request, jsonify
from services.funcionario_service import FuncionarioService

funcionario_bp = Blueprint('Usuario', __name__)
funcionario_service= FuncionarioService()

@funcionario_bp.route('/')
def login_page():
    return 'Login page!'

@funcionario_bp.route('/')
def create_user():
    data = request.get_json() 
    if not data:
        return jsonify({
            "sucess":False,
            "message":"Nenhum dado recebido!"
        }), 400
    nome = data['nome']
    senha = data['senha']
    cargo=['cargo']
    if not nome or not senha or not cargo:
        return jsonify({
            "sucess":False,
            "message":"Os campos nome, senha e cargo são obrigatórios!"
        }),400
    funcionario_service.create_user(nome,senha,cargo)
    return jsonify({
        "sucess":True,
        "message": "Funcionário cadstrado com sucesso!"
    })

    