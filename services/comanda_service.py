from repositories.comanda_repository import ComandaRepository
from db_config import db

class ComandaService:
    def __init__(self):
        self.repo = ComandaRepository()

    def create_comanda(self,id_mesa,id_funcionario,data_abertura):

        if not id_mesa or not id_funcionario or not data_abertura:
            return False
        status="Aberta"
        valor_total=0
        create =self.repo.create_comanda(id_mesa,id_funcionario,data_abertura, status, valor_total)
        if create:
            db.session.commit()
            return True
        return False