class Users:
    """Класс для работы с БД, таблицей users."""
    # Принимает соединение с БД и курсор.
    def __init__(self, connection, cursor):
        self.cursor = cursor
        self.connection = connection

    def create_user(self, first_name, last_name, patronymic, login, password):
        self.cursor.execute('INSERT INTO users (first_name, last_name, patronymic, login, password, role, exist) '
                            '    VALUES (%s, %s, %s, %s, %s, %s, %s)',
                            (first_name, last_name, patronymic, login, password, 'customer', True))
        self.connection.commit()

    def get_all_usrs(self):
        self.cursor.execute('SELECT * FROM users;')
        return self.cursor.fetchall()

    def get_usr_by_login(self, login):
        self.cursor.execute('SELECT * FROM users WHERE login = %s;', (login,))
        return self.cursor.fetchone()

    def get_role_by_id(self, usr_id):
        self.cursor.execute('SELECT role FROM users WHERE id=(%s);', (usr_id,))
        role = self.cursor.fetchone()
        if role == ('admin',):
            role = 'customer'
        elif role == ('customer',):
            role = 'admin'
        else:
            role = 'customer'
        return role

    def change_role(self, role, usr_id):
        self.cursor.execute('UPDATE users SET role=(%s) WHERE id=(%s);', (role, usr_id))
        self.connection.commit()
