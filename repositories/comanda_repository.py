from models.models import Comanda
from db_config import db

class ComandaRepository:
    def get_all(self):
        comandas= Comanda.query.all()
        return comandas
    
    def create_comanda(self, id_mesa, id_funcionario_abertura, data_abertura, status, valor_total):
        nova_comanda = Comanda(
            id_mesa = id_mesa,
            id_funcionario_abertura=id_funcionario_abertura,
            data_abertura=data_abertura,
            status=status,
            valor_total=valor_total
        )
        db.session.add(nova_comanda)
        db.session.flush()
        return True