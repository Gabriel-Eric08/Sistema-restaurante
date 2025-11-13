from flask import Blueprint, request, jsonify
from services.item_pedido_service import ItemPedidoService
from services.produto_service import ProdutoService

item_pedido_service=ItemPedidoService()
produto_service = ProdutoService()

item_pedido_bp =Blueprint('ItemPedido',__name__)

@item_pedido_bp.route('/',methods=['POST'])
def cadastrar_item_pedido():
    data = request.get_json()
    if not data:
        return jsonify({
            "sucess":False,
            "message":"Nenhum dado recebido no corpo da requisição!"
        }), 400
    
    id_pedido = data.get('id_pedido')
    id_produto = data.get('id_produto')
    quantidade = data.get('quantidade')
    observacoes = data.get('observacoes')
    
    if not id_pedido or not id_produto or not quantidade:
        return jsonify({
            "sucess":False, # Corrigido de True para False
            "message":"ID do pedido, ID do produto e quantidade são obrigatórios!"
        }), 400
    
    # --- CORREÇÃO AQUI ---
    # 1. Desempacote a tupla em 'sucess' e 'preco'
    preco = produto_service.price_by_id(id_produto)
    
    # 2. Verifique o 'sucess'
    if not preco:
        return jsonify({
            "sucess":False,
            "message":"Não foi possível obter o preço do produto (Produto não encontrado?)"
        }), 500 # Ou 404
    
    # 3. Passe APENAS a variável 'preco' (que agora é 10.5)
    create = item_pedido_service.create_item_pedido(
        id_pedido,
        id_produto,
        quantidade,
        preco, # <-- Agora 'preco' é um float, não uma tupla
        observacoes
    )
    
    if create:
        return jsonify({
            "sucess":True,
            "message":"Item adicionado ao pedido com sucesso!"
        }), 201 # Use 201 (Created)
    
    return jsonify({
        "sucess":False,
        "message":"Erro ao salvar item no pedido."
    }), 500
