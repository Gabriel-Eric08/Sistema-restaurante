from flask import Blueprint, request, jsonify
from services.pedido_service import PedidoService

pedido_service=PedidoService()
pedido_bp=Blueprint('Pedido',__name__)

@pedido_bp.route('/',methods=['POST'])
def create_pedido():
    data = request.get_json()
    if not data:
        return jsonify({
            "sucess":False,
            "message":"Nenhum dado enviada na requisição!"
        }), 400
    id_funcionario = data.get('id_funcionario')
    id_comanda = data.get('id_comanda')
    if not id_funcionario or not id_comanda:
        return jsonify({
            "sucess":False,
            "message":"Todos os campos são obrigatórios!"
        }),400
    create = pedido_service.create_pedido(id_comanda,id_funcionario)
    if create:
        return jsonify({
            "sucess":True,
            "message":"Pedido registrado com sucesso!"
        }), 200
    return jsonify({
        "sucess":False,
        "message":"Erro interno do servidor"
    }), 500