from flask import Blueprint, request, jsonify
from services.comanda_service import ComandaService
from datetime import datetime

comanda_service= ComandaService()
comanda_bp = Blueprint('Comanda',__name__)

@comanda_bp.route('/',methods=['POST'])
def create_comanda():
    data = request.get_json()
    if not data:
        return jsonify({
            "sucess":False,
            "message":"Nenhum dado recebido no corpo da requisição!"
        }),400
    id_mesa=data.get('id_mesa')
    id_funcionario=data.get('id_funcionario')
    data_abertura = datetime.now()
    if not id_mesa or not id_funcionario:
        return jsonify({
            "sucess":False,
            "message":"Todos os campos são obrigatórios!"
        }),400
    create = comanda_service.create_comanda(id_mesa,id_funcionario,data_abertura)
    if create:
        return jsonify({
            "sucess":True,
            "message":"Comanda registrada com sucesso!"
        }),200
    return jsonify({
        "sucess":False,
        "message":"Erro interno do servidor ou desconhecido!"
    }),500
    