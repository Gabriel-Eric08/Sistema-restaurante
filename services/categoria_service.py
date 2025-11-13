from repositories.categoria_repository import CategoriaRepository
from db_config import db

class CategoriaService:
    def __init__(self):
        self.repo = CategoriaRepository()
    
    def create_category(self,nome):
        if not nome:
            return False
        
        create = self.repo.create_category(nome)
        db.session.commit()
        if create:
            return True