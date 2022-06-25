use bdpi2

create table login(
id smallint primary key auto_increment ,
nome varchar(30) not null,
login varchar(20) not null,
senha varchar(10) not null
);



insert into login( nome, login, senha)
values('Limot','L1','1234');

select * from login

drop table login

/*contador de registros */
select count(*) as "qtd. registros", id as ID, nome as nome,
login as Login, senha as Senha from login



