Q_createUsers = """
CREATE TABLE IF NOT EXISTS users (
id serial NOT NULL,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
patronymic VARCHAR(50) NOT NULL,
login VARCHAR (50) UNIQUE NOT NULL,
password TEXT NOT NULL,
role VARCHAR(50) NOT NULL,
exist boolean
);
"""

Q_createPhones = """
CREATE TABLE IF NOT EXISTS phones (
id serial NOT NULL,
title VARCHAR(50) NOT NULL,
rom int NOT NULL,
ram int NOT NULL,
processor VARCHAR (50) NOT NULL
);
"""

Q_insertAdmin = """
INSERT INTO users (first_name, last_name, patronymic, login, password, role, exist) VALUES
('Викторов', 'Алексей', 'Иванович', 'admin', 'admin', 'admin', True);
"""

Q_insertPhones = """
INSERT INTO phones (id, title, rom, ram, processor) VALUES
(1, 'Fly', 8, 1, 'ARM'),
(2, 'Samsung', 16, 1, 'ARM'),
(3, 'ASUS', 32, 2, 'ARM'),
(4, 'ASUS', 64, 4, 'ARM'),
(5, 'Vivo', 128, 6, 'ARM');
"""
