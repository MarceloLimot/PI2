create database bdpi2

use bdpi2

create table LoginPrestador(
	nome varchar(255),
    telefone varchar(16),
    email varchar(100),
    senha varchar(15),
    cep varchar(10),
    numero varchar(10),
    complemento varchar(100),
    profissao varchar(25)
)


select * from LoginPrestador

insert into LoginPrestador(nome, telefone, email, senha, cep, 
numero, complemento, profissao)
values('Marcelo','11991826089','marcelolimot@gmail.com','72186287',
'08410-440','1112','casa','motociclista');
