from repositories.funcionario_repository import FuncionarioRepository
import hashlib

class FuncionarioService:
    def __init__(self):
        self.repo = FuncionarioRepository()
    
    def create_user(self, nome, senha, cargo):

        senha_em_bytes = senha.encode('utf-8')
        hash_obj = hashlib.sha256(senha_em_bytes)
        hash_hex=hash_obj.hexdigest()
        
        self.repo.create_funcionario(nome,hash_hex,cargo)