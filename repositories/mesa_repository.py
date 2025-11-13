from models.models import Mesa
from db_config import db

class MesaRepository:
    def get_all(self):
        mesas = Mesa.query.all()
        return mesas
    def create_mesa(self, numero, capacidade, status):
        nova_mesa = Mesa(
            numero=numero,
            capacidade=capacidade,
            status=status
        )
        db.session.add(nova_mesa)
        db.session.flush()
        return True