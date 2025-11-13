from flask import Blueprint, request, jsonify
from services.mesa_service import MesaService

mesa_service = MesaService()

mesa_bp = Blueprint('Mesa', __name__)

@mesa_bp.route('/', methods=['POST'])
def create_mesa():
    data = request.get_json()
    if not data:
        return jsonify({
            "sucess":False,
            "message":"Nenhum dado recebido na requisição!"
        }),400
    numero = data.get('numero')
    capacidade = data.get('capacidade')
    status = data.get('status')
    if not numero or  not capacidade or not status:
        return jsonify({
            "sucess":False,
            "message":"Todos os campos são obrigatórios!"
        }), 400
    create = mesa_service.create_mesa(numero,capacidade,status)
    if create:
        return jsonify({
            "sucess":True,
            "message":"Mesa cadastrada com sucesso!"
        }),200