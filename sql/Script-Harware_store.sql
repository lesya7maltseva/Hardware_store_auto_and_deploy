*create table Shops (
	id serial primary key,
	shop_name varchar(50) not null,
	shop_city varchar(50) not null,
	shop_street varchar(50) not null
);

create table Sales (
	sale_id serial primary key,
	doc_id varchar(20) not null,
	item varchar (200) not null,
	category varchar (200) not null,	
	amount int not null,	
	discount int, 
	price decimal not null,	
	date timestamp,
	shop_id int not null,
	till_id int not null,
	foreign key(shop_id) references Shops (id)
);

