from models.models import ItemPedido
from db_config import db

class ItemPedidoRepository:
    def create_item_pedido(self, id_pedido, id_produto, quantidade, preco_unitario, observacoes):
        novo_item_pedido = ItemPedido(
            id_pedido=id_pedido,
            id_produto=id_produto,
            quantidade=quantidade,
            preco_unitario_momento=preco_unitario,
            observacoes=observacoes
        )
        db.session.add(novo_item_pedido)
        db.session.flush()
        return True