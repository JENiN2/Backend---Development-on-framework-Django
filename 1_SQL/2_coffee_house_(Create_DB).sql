--CREATE DATABASE coffee_house;

CREATE TABLE IF NOT EXISTS post 
(
	id serial NOT NULL PRIMARY KEY,
	name varchar(50) NOT NULL,
	salary numeric(10,2) NOT NULL
);

SELECT * FROM post;

DROP TABLE post;

CREATE TABLE IF NOT EXISTS employee
(
	id serial NOT NULL PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	middle_name varchar(50) NOT NULL,
	phone varchar(18) NOT NULL,
	datebirth date NOT NULL,
	--post_id integer NOT NULL REFERENCES post(id)
	post_id integer NOT NULL,
	FOREIGN KEY (post_id) REFERENCES post(id)
);

ALTER TABLE employee 
RENAME COLUMN last_name TO name;

ALTER TABLE employee 
RENAME COLUMN middle_name TO patronymic;

CREATE TABLE IF NOT EXISTS orders
(
	id serial NOT NULL PRIMARY KEY,
	registration_date timestamp NOT NULL,
	total_price numeric(10,2) NOT NULL,
	order_status varchar(50) NOT NULL,
	end_date timestamp NULL,
	employee_id integer NOT NULL,
	FOREIGN KEY (employee_id) REFERENCES employee(id)
);

CREATE TABLE IF NOT EXISTS coffee
(
	id serial NOT NULL PRIMARY KEY,
	name varchar(50) NOT NULL,
	price numeric(10,2) NOT NULL,
	volume integer NOT NULL,
	description text NULL,
	recept text NOT NULL
);

CREATE TABLE IF NOT EXISTS order_position
(
	id serial NOT NULL PRIMARY KEY,
	count varchar(50) NOT NULL,
	coffee_id integer NOT NULL REFERENCES coffee(id),
	order_id integer NOT NULL REFERENCES orders(id),
	UNIQUE (coffee_id, order_id)
);

CREATE TABLE IF NOT EXISTS topping
(
	id serial NOT NULL PRIMARY KEY,
	name varchar(50) NOT NULL,
	price numeric(10,2) NOT NULL,
	description text NULL
);

CREATE TABLE IF NOT EXISTS coffee_topping
(
	id serial NOT NULL PRIMARY KEY,
	topping_id integer NOT NULL REFERENCES topping(id),
	order_position_id integer NOT NULL REFERENCES order_position(id),
	UNIQUE (topping_id, order_position_id)
);

CREATE TABLE IF NOT EXISTS ingredients
(
	id serial NOT NULL PRIMARY KEY,
	name varchar(50) NOT NULL,
	price numeric(10,2) NOT NULL,
	description text NULL
);

CREATE TABLE IF NOT EXISTS coffee_ingredients
(
	id serial NOT NULL PRIMARY KEY,
	volume_ing integer NOT NULL,
	volume_type varchar(10) NOT NULL,
	coffee_id integer NOT NULL REFERENCES coffee(id),
	ingredients_id integer NOT NULL REFERENCES ingredients(id),
	UNIQUE (coffee_id, ingredients_id)
);

INSERT INTO post (name, salary)
VALUES
('Директор', 70000.00),
('Бухгалтер', 50000.00),
('Бариста-кассир', 40000.00),
('Уборщик', 25600.00);

SELECT id, name, salary FROM post;

INSERT INTO employee (first_name, name, patronymic, datebirth, phone, post_id)
VALUES
('Викторов', 'Артем', 'Леонидович', '1986-04-28', '+7(939)898-12-31', 1),
('Морозова', 'Виктория', 'Ивановна', '1982-06-12', '+7(912)391-42-12', 2),
('Александрова', 'Ева', 'Васильевна', '1998-12-11', '+7(239)596-74-75', 3),
('Илларионов', 'Евгений', 'Александрович', '1997-10-11', '+7(539)229-17-45', 3),
('Васильев', 'Иван', 'Дмитриевич', '1994-02-28', '+7(624)495-75-86', 4);

SELECT 
	employee.id,
	employee.first_name,
	employee.name,
	employee.phone,
	post.name,
	post.salary
FROM employee INNER JOIN post 
	ON employee.post_id = post.id;
	
INSERT INTO coffee (name, price, volume, description, recept)
VALUES
('Эспрессо', 90, 50, 'Свежеобжаренная арабика.', 'Соотношение молотого кофе и воды 1 к 2.'),
('Капучино', 90, 250, 'Молочный кофейный напиток на основе эспрессо и нежного взбитого молока.',
 'Порция эспрессо смешивается с молоком и молочной пеной в соотношении один к одному. Лучше использовать молоко жирностью 3,2-3,5%. 
 Сначала взбивается молоко, а затем варится эспрессо. Температура капучино при подаче гостю должна составлять 60-70 градусов.'),
('Американо', 90, 250, 'Классический кофе на основе эспрессо с добавлением воды.',
 'Двойной эспрессо смешать с горячей водой 1 к 1.'),
('Латте', 140, 350, 'Лёгкий молочно-кофейный напиток на основе нежно взбитого молока с добавлением эспрессо.', 
 'Взбить молоко. Приготовить чёрный кофе. Тонкой струйкой влить молоко. При этом жидкости должны смешаться, а на поверхности – образоваться пенка толщиной около 1 см.');
 
SELECT * FROM coffee;
 
INSERT INTO ingredients (name, price, description)
VALUES
('Молотый кофе', 20, 'Перемолотые кофейные зёрна.'),
('Молоко', 10, 'Питательная жидкость.'),
('Вода', 1, 'Бинарное неорганическое соединение, молекула которого состоит из двух атомов водорода и одного — кислорода, которые соединены между собой ковалентной связью.');

SELECT * FROM ingredients;

INSERT INTO coffee_ingredients (volume_ing, volume_type, coffee_id, ingredients_id)
VALUES
(5, 'гр', 1, 1),
(45, 'мл', 1, 3),
(10, 'гр', 2, 1),
(165, 'мл', 2, 2),
(75, 'мл', 2, 3),
(10, 'гр', 3, 1),
(240, 'мл', 3, 3),
(5, 'гр', 4, 1),
(165, 'мл', 4, 2),
(80, 'мл', 4, 3);

--М к М
SELECT
	co.name AS "Кофе",
	co.price AS "Цена",
	ci.coffee_id,
	i.name AS "Название ингредиента",
	ci.ingredients_id
FROM coffee_ingredients ci 
INNER JOIN coffee co
	ON ci.coffee_id = co.id
INNER JOIN ingredients i 
	ON ci.ingredients_id = i.id;

INSERT INTO topping (name, price, description)
VALUES
('Шоколадный', 30, 'Придает шоколадный вкус.'),
('Карамель', 20, 'Придает легкий карамельный аромат.'),
('Кокосовый', 20, 'Придает легкий аромат тропиков.');

SELECT * FROM orders;

INSERT INTO orders (registration_date, total_price, order_status, end_date, employee_id)
VALUES
('2022-12-04 10:23:54', 110, 'Выполнен', '2022-12-04 10:27:35', 3),
('2022-12-04 10:28:11', 210, 'Выполнен', '2022-12-04 10:37:22', 4),
('2022-12-04 10:39:23', 220, 'Готовится', NULL, 3);

INSERT INTO order_position (count, coffee_id, order_id)
VALUES
(1, 4, 1),
(2, 2, 2),
(1, 1, 3),
(1, 3, 3);

SELECT * FROM topping;

INSERT INTO coffee_topping (topping_id, order_position_id)
VALUES
(2, 1),
(1, 2),
(3, 4),
(2, 3);

SELECT 
	employee.id,
	employee.first_name AS "Фамилия",
	employee.name AS "Имя",
	employee.patronymic AS "Отчество",
	employee.datebirth AS "Дата рождения",
	employee.phone AS "Телефон",
	post.name AS "Должность",
	post.salary AS "Оклад"
FROM employee INNER JOIN post 
	ON employee.post_id = post.id;
	
--М к М
SELECT
	co.name AS "Кофе",
	co.price AS "Цена",
	co.volume AS "Объем",
	ci.coffee_id,
	i.name AS "Название ингредиента",
	i.price AS "Цена ингредиента",
	i.description AS "Описание ингредиента",
	ci.ingredients_id
FROM coffee_ingredients ci 
INNER JOIN coffee co
	ON ci.coffee_id = co.id
INNER JOIN ingredients i 
	ON ci.ingredients_id = i.id;
	
SELECT
	orders.registration_date AS "Начало заказа",
	orders.total_price AS "Общая цена",
	orders.order_status AS "Статус заказа",
	orders.end_date AS "Готовность заказа",	
	coffee.name AS "Кофе",
	coffee.price AS "Цена",
	coffee.volume AS "Объем",
	order_position.count,
	order_position.order_id
FROM order_position
INNER JOIN orders
	ON order_position.order_id = orders.id
INNER JOIN coffee
	ON order_position.coffee_id = coffee.id;
	
SELECT
	topping.name AS "Название топпинга",
	topping.price AS "Цена топпинга",
	topping.description AS "Описание",
	order_position.order_id
FROM coffee_topping
INNER JOIN topping
	ON coffee_topping.topping_id = topping.id
INNER JOIN order_position
	ON coffee_topping.order_position_id = order_position.id;
	
SELECT
	orders.registration_date AS "Начало заказа",
	orders.total_price AS "Общая цена",
	orders.order_status AS "Статус заказа",
	orders.end_date AS "Готовность заказа",
	employee.id,
	employee.first_name AS "Фамилия",
	employee.name AS "Имя",
	employee.patronymic AS "Отчество",
	employee.datebirth AS "Дата рождения",
	employee.phone AS "Телефон"
FROM orders INNER JOIN employee
	ON orders.employee_id = employee.id;