-- Tabela para armazenar as categorias dos produtos
CREATE TABLE categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

-- Tabela para armazenar os produtos (cardápio)
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL, -- DECIMAL vira REAL
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);

-- Tabela simples de funcionários
CREATE TABLE funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    senha_hash TEXT NOT NULL,
    cargo TEXT NOT NULL
);

-- Tabela para cadastrar as mesas do restaurante
CREATE TABLE mesas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero INTEGER NOT NULL UNIQUE,
    capacidade INTEGER DEFAULT 2,
    status TEXT DEFAULT 'Livre'
);

-- Tabela de Comandas (ou Contas)
CREATE TABLE comandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_mesa INTEGER NOT NULL,
    id_funcionario_abertura INTEGER NOT NULL,
    data_abertura TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, -- DATETIME vira TEXT
    data_fechamento TEXT,
    status TEXT NOT NULL DEFAULT 'Aberta',
    valor_total REAL DEFAULT 0.00, -- DECIMAL vira REAL
    FOREIGN KEY (id_mesa) REFERENCES mesas(id),
    FOREIGN KEY (id_funcionario_abertura) REFERENCES funcionarios(id)
);

-- Tabela de Pedidos
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_comanda INTEGER NOT NULL,
    id_funcionario INTEGER NOT NULL,
    data_pedido TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, -- DATETIME vira TEXT
    status_pedido TEXT DEFAULT 'Pendente',
    FOREIGN KEY (id_comanda) REFERENCES comandas(id),
    FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
);

-- Tabela de Itens do Pedido
CREATE TABLE itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL DEFAULT 1,
    preco_unitario_momento REAL NOT NULL, -- DECIMAL vira REAL
    observacoes TEXT,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id),
    FOREIGN KEY (id_produto) REFERENCES produtos(id)
);