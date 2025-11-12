from repositories.funcionario_repository import FuncionarioRepository
import hashlib
from db_config import db

class FuncionarioService:
    def __init__(self):
        self.repo = FuncionarioRepository()
    def create_user(self, nome, senha, cargo):

        if not nome or not senha or not cargo:
            return False
        
        hash_hex = hash_senha(senha)
        self.repo.create_funcionario(nome,hash_hex,cargo)
        db.session.commit()

        return True
    
    def validate_user(self, nome, senha):
        if not nome or not senha:
            return False
        hash_hex = hash_senha(senha)
        funcionario = self.repo.get_funcionario(nome,hash_hex)
        if funcionario:
            return True
        return False
    
def hash_senha(senha):
        senha_em_bytes = senha.encode('utf-8')
        hash_obj = hashlib.sha256(senha_em_bytes)
        hash_hex=hash_obj.hexdigest()
        return hash_hex