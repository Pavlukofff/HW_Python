create table seller(
	id int unsigned primary key auto_increment,
    company varchar(64) unique not null,
    phone varchar(20) null
);

create table users(
	id int unsigned primary key auto_increment,
    username varchar(64) not null,
    password varchar(64) not null,
    email varchar(256) unique,
    phone varchar(20) null
);

create table products(
	id int unsigned primary key auto_increment,
    name varchar(256) not null,
    cost int,
    count int,
    content text,
    seller_id int unsigned not null,

    foreign key (seller_id) references seller (id)
);

create table orders(
	id int unsigned primary key auto_increment,
    count int,
    user_id int unsigned not null,
    product_id int unsigned not null,

    foreign key (user_id) references users (id),
    foreign key (product_id) references products (id)
);
