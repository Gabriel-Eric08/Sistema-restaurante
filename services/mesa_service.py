from repositories.mesa_repository import MesaRepository
from db_config import db

class MesaService:
    def __init__(self):
        self.repo = MesaRepository()
    
    def create_mesa(self, numero, capacidade, status):
        if not numero or not capacidade or not status:
            return False
        
        create = self.repo.create_mesa(numero,capacidade,status)
        if create:
            db.session.commit()
            return True
        return False