from repositories.produto_repository import ProdutoRepository
from db_config import db

class ProdutoService:
    def __init__(self):
        self.repo = ProdutoRepository()
    
    def create_product(self, nome, descricao, preco, id_categoria):
        if not nome or not descricao or not preco or not id_categoria:
            return False
        
        create = self.repo.create_product(nome, descricao, preco, id_categoria)
        if create:
            db.session.commit()
            return True
        return False
    
    def get_all(self):
        return self.repo.get_all()