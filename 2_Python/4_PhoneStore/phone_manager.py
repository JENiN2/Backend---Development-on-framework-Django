class Phones:
    """Класс для работы с БД, таблицей phones."""
    # Принимает соединение с БД и курсор.
    def __init__(self, connection, cursor):
        self.cursor = cursor
        self.connection = connection

    def get_all_phones(self):
        self.cursor.execute('SELECT * FROM phones;')
        return self.cursor.fetchall()

    def add_phone(self, title, rom, ram, proc):
        self.cursor.execute('INSERT INTO phones (title, rom, ram, processor) VALUES (%s, %s, %s, %s)',
                            (title, rom, ram, proc))
        self.connection.commit()

    def del_phone_by_id(self, del_product):
        self.cursor.execute('DELETE FROM phones WHERE id=(%s)', (del_product,))
        self.connection.commit()
