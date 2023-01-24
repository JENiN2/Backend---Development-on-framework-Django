import psycopg2

connection = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='1',
    host='localhost',
    port='5433'
)

print(connection)

cursor = connection.cursor()
Q_createEmployee = """
CREATE TABLE IF NOT EXISTS employee (
id serial NOT NULL,
firstname VARCHAR(50) NOT NULL,
name VARCHAR(50) NOT NULL,
salary int NOT NULL
);
"""

Q_insertEmployee = """
INSERT INTO employee (firstname, name, salary) VALUES
('Робертов', 'Алексей', 65000),
('Мантиева', 'Екатерина', 71000);
"""

Q_selectEmployee = """
SELECT * FROM employee;
"""

cursor.execute(Q_createEmployee)
cursor.execute(Q_insertEmployee)
cursor.execute(Q_selectEmployee)

print(f'Вывод одной записи {cursor.fetchone()}')
print(f'Вывод одной записи {cursor.fetchone()}')
# or
print(f'Вывод нескольких записи {cursor.fetchmany(2)}')
# or
print(f'Вывод всех записи {cursor.fetchall()}')

firstname = input('Введите фамилию ')
name = input('Введите имя ')
salary = int(input('Введите оклад '))

cursor.execute(
    "INSERT INTO employee (firstname, name, salary) VALUES (%s, %s, %s)",
    (firstname, name, salary)
)

cursor.execute(Q_selectEmployee)
print(f'Вывод всех записи {cursor.fetchall()}')

connection.commit()
cursor.close()

connection.close()
