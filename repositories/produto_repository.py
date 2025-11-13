from models.models import Produto
from db_config import db

class ProdutoRepository:

    def get_all(self):
        produtos = Produto.query.all()
        return produtos
    
    def get_produto_by_id(self,id):
        produto = Produto.query.filter_by(id=id)
        return produto
    
    def create_product(self, nome, descricao, preco, id_categoria):
        novo_produto = Produto(
            nome=nome,
            descricao=descricao,
            preco=preco,
            id_categoria=id_categoria
        )
        db.session.add(novo_produto)
        db.session.flush()
        return True