from models.models import Categoria
from db_config import db

class CategoriaRepository:
    def get_all(self):
        categorias = Categoria.query.all()

    def create_category(self, nome):
        nova_categoria = Categoria(
            nome=nome
        )
        db.session.add(nova_categoria)
        db.session.flush()
        return True