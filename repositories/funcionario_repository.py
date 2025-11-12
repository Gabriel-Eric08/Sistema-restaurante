from models.models import Funcionario
from db_config import db

class FuncionarioRepository:
    def get_all(self):
        funcionarios = Funcionario.query.all()
        return funcionarios
    def create_funcionario(self, nome,senha,cargo):
        novo_funcionario=Funcionario(
            nome=nome,
            senha_hash=senha,
            cargo=cargo
        )
        db.session.add(novo_funcionario)
        db.session.flush()