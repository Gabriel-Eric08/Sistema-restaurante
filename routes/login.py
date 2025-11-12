from flask import Blueprint, render_template, request, make_response, jsonify

from services.funcionario_service import FuncionarioService

funcionario_service=FuncionarioService()

login_bp = Blueprint('Login',__name__)

@login_bp.route('/')
def login_page():
    return render_template('login.html')

@login_bp.route('/', methods=['POST'])
def auth():
    data = request.get_json()
    nome = data.get('nome')
    senha = data.get('senha')

    if not data:
        return jsonify({
            "sucess":False,
            "message":"Requisição enviada sem dados!"
        }),400
    
    if not nome or not senha:
        return jsonify({
            "sucess":False,
            "message": "Os campos usuário e senha são obrigatórios no corpo da requisição!"
        }), 400
    
    validate = funcionario_service.validate_user(nome, senha)
    if validate:
        resp = make_response(jsonify({
            "sucess":True,
            "message":"Usuário autenticado com sucesso!"
        }))
        resp.set_cookie('nome',value=nome)
        resp.set_cookie('senha',value=senha)
        return resp
    return jsonify({
        "sucess": False,
        "message": "Usuário não autenticado!"
    })