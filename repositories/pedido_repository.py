from models.models import Pedido
from db_config import db

class PedidoRepository:
    def get_pedidos_por_comanda(self, id_comanda):
        pedidos= Pedido.query.filter_by(id_comanda=id_comanda).all()
        return pedidos
    def create_pedido(self, id_comanda, id_funcionario, data_pedido, status_pedido):
        novo_pedido= Pedido(
            id_comanda=id_comanda,
            id_funcionario=id_funcionario,
            data_pedido=data_pedido,
            status_pedido=status_pedido
        )
        db.session.add(novo_pedido)
        db.session.flush()
        return True
