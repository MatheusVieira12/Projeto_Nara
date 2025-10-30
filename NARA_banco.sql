CREATE DATABASE NARA;

USE NARA;

-- Tabela de Clientes
CREATE TABLE tb_clientes (
	ID_Cliente INT PRIMARY KEY AUTO_INCREMENT,
	Nome VARCHAR(100),
	Idade INT,
	Sexo VARCHAR(20),
	Cidade VARCHAR(100),
	Estado VARCHAR(2),
	Canal_aquisicao VARCHAR(50)
);

-- Tabela de Produtos
CREATE TABLE tb_produto (
	ID_Produto INT PRIMARY KEY AUTO_INCREMENT,
	Nome_Produto VARCHAR(100),
	Categoria VARCHAR(100),
	Preco FLOAT,
	Marca VARCHAR(30)
);

-- Tabela de Atendimentos
CREATE TABLE tb_atendimentos (
	ID_Atendimento INT PRIMARY KEY AUTO_INCREMENT,
	ID_Cliente INT,
	Tipo VARCHAR(50),
	Tempo_Resposta FLOAT,
	`Data` DATE,
    Nota_Satisfacao INT,
	FOREIGN KEY (ID_Cliente) REFERENCES tb_clientes(ID_Cliente)
);

-- Tabela de Campanhas
CREATE TABLE tb_campanhas (
	ID_Campanha INT PRIMARY KEY AUTO_INCREMENT,
	Canal VARCHAR(50),
	Custo FLOAT,
	Data_Inicio DATE,
	Data_Fim DATE,
	Tipo_Campanha VARCHAR(100)
);

-- Tabela de Avaliações
CREATE TABLE tb_avaliacoes (
	ID_Cliente INT,
	ID_Produto INT,
	Nota INT,
	Data_Avaliacao DATE,
	Comentario VARCHAR(255),
	FOREIGN KEY (ID_Cliente) REFERENCES tb_clientes(ID_Cliente),
	FOREIGN KEY (ID_Produto) REFERENCES tb_produto(ID_Produto)
);

-- Tabela de Vendas (com ID_Campanha adicionado)
CREATE TABLE tb_vendas (
	ID_Venda INT PRIMARY KEY AUTO_INCREMENT,
	ID_Cliente INT,
	ID_Produto INT,
	ID_Campanha INT,
	`Data` DATE,
	Quantidade INT,
	Canal VARCHAR(50),
	Valor_Total FLOAT,
	FOREIGN KEY (ID_Cliente) REFERENCES tb_clientes(ID_Cliente),
	FOREIGN KEY (ID_Produto) REFERENCES tb_produto(ID_Produto),
	FOREIGN KEY (ID_Campanha) REFERENCES tb_campanhas(ID_Campanha)
);


SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE 'C:/Users/PC/Desktop/projetos/NARA/clientes.csv'
INTO TABLE tb_clientes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Cliente, Nome, Idade, Sexo, Cidade, Estado, Canal_Aquisicao);


LOAD DATA LOCAL INFILE 'C:/Users/PC/Desktop/projetos/NARA/produtos.csv'
INTO TABLE tb_produto
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Produto, Nome_Produto, Categoria, Preco, Marca);

LOAD DATA LOCAL INFILE 'C:/Users/PC/Desktop/projetos/NARA/atendimentos.csv'
INTO TABLE tb_atendimentos
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Atendimento, ID_Cliente, Tipo, `Data`, Tempo_Resposta, Nota_Satisfacao);

LOAD DATA LOCAL INFILE 'C:/Users/PC/Desktop/projetos/NARA/avaliacoes.csv'
INTO TABLE tb_avaliacoes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Cliente, ID_Produto, Nota, `Data_Avaliacao`, Comentario);

LOAD DATA LOCAL INFILE 'C:/Users/PC/Desktop/projetos/NARA/campanhas_corrigido.csv'
INTO TABLE tb_campanhas
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Campanha, Canal, `Data_Inicio`, `Data_Fim`, Tipo_Campanha, Custo);

LOAD DATA LOCAL INFILE 'C:/Users/PC/Desktop/projetos/NARA/vendas.csv'
INTO TABLE tb_vendas
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Venda, ID_Cliente, ID_Produto, ID_Campanha, `Data`, Quantidade, Canal, Valor_Total);



DROP TABLE tb_vendas;

DROP TABLE tb_avaliacoes;

DROP TABLE tb_atendimentos;

DROP TABLE tb_campanhas;

DROP TABLE tb_produto;

DROP TABLE tb_clientes;


SELECT * FROM tb_clientes;

SELECT * FROM tb_produto;

SELECT * FROM tb_atendimentos;

SELECT * FROM tb_campanhas;

SELECT * FROM tb_avaliacoes;

SELECT * FROM tb_vendas;


