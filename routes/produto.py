from flask import Blueprint, render_template,request, jsonify
from services.produto_service import ProdutoService

produto_service=ProdutoService()

produto_bp = Blueprint('Blueprint', __name__)

@produto_bp.route('/')
def produtos_page():
    produtos = produto_service.get_all()
    return render_template('produtos.html.j2', produtos=produtos)

@produto_bp.route('/', methods=['POST'])
def cadastrar_produto():
    data = request.get_json()
    if not data:
        return jsonify({
            "sucess":False,
            "message":"Dados não recebidos na requisição!"
        }), 400
    
    nome = data.get('nome')
    descricao = data.get('descricao')
    preco = data.get('preco')
    id_categoria = data.get('id_categoria')
    if not nome or not descricao or not id_categoria or not preco:
        return jsonify({
            "sucess":False,
            "message":"Todos os campos são obrigatórios!"
        }),400
    
    create_product=produto_service.create_product(nome,descricao,preco,id_categoria)
    if create_product:
        return jsonify({
            "sucess":True,
            "message":"Produto cadastrado com sucesso!"
        }), 200

    