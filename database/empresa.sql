CREATE DATABASE empresa;

USE empresa;

CREATE TABLE clientes (
		id INT PRIMARY KEY AUTO_INCREMENT,
		nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE,
        telefone VARCHAR(20) NOT NULL,
        horario TIME NOT NULL,
        servicos VARCHAR(100) NOT NULL
);

SELECT * FROM clientes;