from db_config import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)

class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Float, nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    categoria = db.relationship('Categoria', backref=db.backref('produtos', lazy=True))

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=False)
    senha_hash = db.Column(db.Text, nullable=False)
    cargo = db.Column(db.String(50), nullable=False)

class Mesa(db.Model):
    __tablename__ = 'mesas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.Integer, unique=True, nullable=False)
    capacidade = db.Column(db.Integer, default=2)
    status = db.Column(db.String(50), default='Livre')

class Comanda(db.Model):
    __tablename__ = 'comandas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_mesa = db.Column(db.Integer, db.ForeignKey('mesas.id'), nullable=False)
    id_funcionario_abertura = db.Column(db.Integer, db.ForeignKey('funcionarios.id'), nullable=False)
    data_abertura = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    data_fechamento = db.Column(db.DateTime)
    status = db.Column(db.String(50), nullable=False, default='Aberta')
    valor_total = db.Column(db.Float, default=0.00)
    mesa = db.relationship('Mesa', backref=db.backref('comandas', lazy=True))
    funcionario = db.relationship('Funcionario', backref=db.backref('comandas_abertas', lazy=True))

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_comanda = db.Column(db.Integer, db.ForeignKey('comandas.id'), nullable=False)
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionarios.id'), nullable=False)
    data_pedido = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    status_pedido = db.Column(db.String(50), default='Pendente')
    comanda = db.relationship('Comanda', backref=db.backref('pedidos', lazy=True))
    funcionario = db.relationship('Funcionario', backref=db.backref('pedidos_registrados', lazy=True))

class ItemPedido(db.Model):
    __tablename__ = 'itens_pedido'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    preco_unitario_momento = db.Column(db.Float, nullable=False)
    observacoes = db.Column(db.Text)
    pedido = db.relationship('Pedido', backref=db.backref('itens', lazy=True))
    produto = db.relationship('Produto')