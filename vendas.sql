#drop database vendas;
create database vendas;
use vendas;

create table produtos(
cod int auto_increment primary key,
descr varchar(30),
fabricante varchar(30),
quantidade int
);

select * from produtos





