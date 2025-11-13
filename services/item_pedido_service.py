from repositories.item_pedido_repository import ItemPedidoRepository
from db_config import db

class ItemPedidoService:
    def __init__(self):
        self.repo = ItemPedidoRepository()

    def create_item_pedido(self, id_pedido, id_produto, quantidade, preco_unitario, observacoes):

        if not id_pedido or not id_produto or not quantidade or not preco_unitario or not observacoes:
            return False
        if observacoes =="":
            observacoes="Nenhuma observação!"

        create = self.repo.create_item_pedido(id_pedido,id_produto,quantidade,preco_unitario,observacoes)
        if create:
            db.session.commit()
            return True
        return False