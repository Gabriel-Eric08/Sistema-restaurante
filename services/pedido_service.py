from repositories.pedido_repository import PedidoRepository
from datetime import datetime
from db_config import db

class PedidoService:
    def __init__(self):
        self.repo = PedidoRepository()
    
    def create_pedido(self,id_comanda, id_funcionario):

        if not id_comanda or not id_funcionario:
            return False
        data_pedido = datetime.now()
        status="Aberto"

        create = self.repo.create_pedido(id_comanda,id_funcionario,data_pedido,status)
        if create:
            db.session.commit()
            return True
        return False