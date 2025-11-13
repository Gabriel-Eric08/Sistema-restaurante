from flask import Blueprint, request, jsonify
from services.categoria_service import CategoriaService

categoria_service = CategoriaService()
categoia_bp = Blueprint('Categoria', __name__)

@categoia_bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json()
    if not data:
        return jsonify({
            "sucess":False,
            "message": "Nenhum dado recebido na requisição!"
        }),400
    nome = data.get('nome')
    if not nome:
        return jsonify({
            "sucess":False,
            "message":"Nome não recebido no corpo da requisição!"
        }),400
    create_category = categoria_service.create_category(nome)
    if create_category:
        return jsonify({
            "scuess":True,
            "message":"Categoria registrada com sucesso!"
        }), 200