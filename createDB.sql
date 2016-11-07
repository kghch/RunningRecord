create database forpy;

use database forpy;

create table user(
id int(4) not null primary key auto_increment,
username varchar(20) not null,
password varchar(20) not null,
mail varchar(30)
);


insert into user(username,password) values('wanghan', 'wanghan');

create table records(
id int(5) not null primary key auto_increment,
username varchar(20) not null,
rundate date not null,
runtime varchar(15),
length int(5),
feeling varchar(60),
dt datetime not null default current_timestamp
);