import psycopg2

# В последнюю очередь импортируются мои модули.
# Запросы в БД.
import db_init
# Обработка запросов в таблицу users.
from user_manager import Users
# Обработка запросов в таблицу phones.
from phone_manager import Phones
# Модуль с функциями, которые обрабатывают данные.
import data_proc as dp

# Подключение к БД.
connection = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='1',
    host='localhost',
    port='5433'
)

# cursor() позволяет коду Python выполнять команду PostgreSQL в сеансе базы данных.
cursor = connection.cursor()

# В классе Users прописано взаимодействие с БД (таблицей users). Создаем экземпляр класса
# Users (передаем в класс соединение и курсор созданные ранее) - usr_manager
usr_manager = Users(connection, cursor)
# В классе Phones прописано взаимодействие с БД (таблицей phones). Создаем экземпляр класса
# Phones (передаем в класс соединение и курсор созданные ранее) - phone_mngr
phone_mngr = Phones(connection, cursor)

# Выполняет запрос к бд (вынесенный в модуль db_init) для создания таблицы users.
cursor.execute(db_init.Q_createUsers)
# Выполняет запрос к бд (вынесенный в модуль db_init) для создания таблицы phones.
cursor.execute(db_init.Q_createPhones)
# Закрепляет выполненные изменения в бд.
connection.commit()

# Добавление администратора.
if not usr_manager.get_all_usrs():
    cursor.execute(db_init.Q_insertAdmin)
    connection.commit()
else:
    pass

# Заполнение таблицы с телефонами.
if not phone_mngr.get_all_phones():
    cursor.execute(db_init.Q_insertPhones)
    connection.commit()
else:
    pass

print('Вас приветствует программа "Магазин телефонов"!')

# Определение пекременных.
user = None
admin_check = False
com = 0
login = ''
pas = ''

while True:
    # Проверка, если пользователь залогинен, авторизация не предлагается.
    if user is None:
        print('------Выберите действие:---q-выход-')
        com = input('1 - Авторизация\n2 - Регистрация\n')
    if com == '1':  # Auth
        # Проверка на администратора.
        if admin_check is False:
            print('------введите логин и пароль---')
            login = input('Логин: ')
            pas = input('Пароль: ')
            user = usr_manager.get_usr_by_login(login)
            # Проверка, если логин правильный (по нему достается запись из бд), в user ecть запись.
            if user is None:
                print('------Вы ввели неверный логин.---')
                print('------')
                # Если логин неверный то начинаем с начала цикла.
                continue
            # Проверка, залогинился админ или нет.
            if user is not None:
                admin_check = user[6] == 'admin'
        # Если логин верный и в user есть запись, сравнивает логин и пароль, проверяет что это не админ и exist is True.
        if login == user[4] and pas == user[5] and admin_check is False and user[7] is True:  # Customer
            print(f'------вы вошли в систему как {user[4]}---')
            print('------Телефоны в наличии:---')
            # Функция для вывода на экран списка телефонов print_phones из модуля data_proc принимает результат
            # работы метода geta_all_phones() класса Phones, который вытаскивает все данные из таблицы phones.
            dp.print_phones(phone_mngr.get_all_phones())
            # Далее клиент может только разлогиниться и попасть на первый экран.
            input("Нажмите enter, чтобы продолжить")
            # user is None, чтобы попасть на первый экран.
            user = None
            # В начало цикла.
            continue
        # Эта проверка, если логинится админ.
        if login == user[4] and pas == user[5] and user[6] == 'admin' and user[7] is True:  # Admin
            print(f'------вы вошли в систему как {user[4]} (Администратор)---')
            # Меню выбора из 5 пунктов.
            com_a = input('1 - Добавить товар\n2 - Удалить товар\n3 - Информация о пользователях\n'
                          '4 - Смена роли пользователю\n5 - Завершить сеанс\n')
            if com_a == '1':  # If Add a new product
                print('------Телефоны в наличии:---')
                dp.print_phones(phone_mngr.get_all_phones())
                print('------Добавить новый тлефон:---cancel-отмена действия-')
                # Далее запрашиваются характеристики телефона по очереди, также я добавил возможность отмены действия,
                # добавив проверку после каждого input.
                title = input('Введите название: ')
                if title == 'cancel':
                    continue
                rom = input('Введите кол-во памяти (число): ')
                if rom == 'cancel':
                    continue
                # Из за cancel пришлось еще добавить проверку на число.
                try:
                    int(rom)
                except ValueError:
                    print('------Вы ввели не число!---')
                    continue
                ram = input('Введите кол-во оперативной памяти (число): ')
                if ram == 'cancel':
                    continue
                try:
                    int(ram)
                except ValueError:
                    print('------Вы ввели не число!---')
                    continue
                proc = input('Введите название процессора: ')
                if proc == 'cancel':
                    continue
                # Метод add_phone() отправляет запрос на добавления нового телефона в бд используя переменные с нашими
                # значениями.
                phone_mngr.add_phone(title, rom, ram, proc)
                print('------Телефон добавлен!---')
                print('------Телефоны в наличии (обновленный список):---')
                dp.print_phones(phone_mngr.get_all_phones())
            elif com_a == '2':  # Delete
                print('------Телефоны в наличии:---')
                # all_phones используется чтобы не обращаться к БД 2 раза.
                all_phones = phone_mngr.get_all_phones()
                dp.print_phones(all_phones)
                print('------Удалить тлефон:---cancel-отмена действия-')
                del_product = input('Введите номер телефона, который хотите удалить:')
                if del_product == 'cancel':
                    continue
                try:
                    int(del_product)
                except ValueError:
                    print('------Вы ввели не число!---')
                    continue
                else:
                    # В функцию phones_id (создает список с id телефонов), передаем переменную all_phones, которой
                    # ранее присвоили результат работы метода get_all_phones()
                    if int(del_product) in dp.phones_id(all_phones):
                        phone_mngr.del_phone_by_id(del_product)
                        print('------Телефон удален!---')
                    else:
                        print('------Такого номера нет в списке---')
                        continue
            elif com_a == '3':  # Info
                print('------Информация о пользователях:---')
                # Тут все как и с телефонами, но теперь с пользователями.
                dp.print_users(usr_manager.get_all_usrs())
            elif com_a == '4':  # Role
                print('------Информация о пользователях:---')
                # Снова переменная исп-я, чтобы не обращаться к БД 2 раза.
                all_users = usr_manager.get_all_usrs()
                # Принтует обработанную запись всех пользователей.
                dp.print_users(all_users)
                print('------Смена роли пользователя:---cancel-отмена действия-')
                usr_id = input('Чтобы сменить роль пользователю, выберите его номер: ')
                if usr_id == 'cancel':
                    continue
                try:
                    int(usr_id)
                except ValueError:
                    print('------Вы ввели не число!---')
                    continue
                else:
                    if int(usr_id) in dp.users_id(all_users):
                        # Метод называется get_role_by_id, но после получения он сам меняет роль, что наверное
                        # неправильно, получается в переменной role уже измененная роль.
                        role = usr_manager.get_role_by_id(usr_id)
                        # А метод change_role просто обновляет запись where id=usr_id в таблице users.
                        usr_manager.change_role(role, usr_id)
                    else:
                        print('------Такого номера нет в списке---')
                        continue
                print('------Роль успешно изменена!---')
            # Разлогинивание. Выйти из программы можно только на первом экране.
            elif com_a == '5':
                print('------cеанс завершен---')
                # Все обнуляем
                user = None
                admin_check = False
                continue
        # Сюда попадаем если логин верный а пароль нет.
        else:
            print(f'------Проблемы с правами доступа, обратитесь к администратору---')
            print('------')
            user = None
            continue
    elif com == '2':  # Registration
        print('------регистрация нового пользователя---')
        first_name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        patronymic = input('Введите отчество:')
        login = input('Введите логин: ')
        password = input('Введите пароль:')
        # Метод, создающий новую запись в таблице users.
        usr_manager.create_user(first_name, last_name, patronymic, login, password)
        print('------регистрация завершена---')
    # Завершение программы (только на первом экране).
    elif com == 'q':
        break
    # Если не 1 или 2.
    else:
        print('Вы ввели неверное значение')
        continue

# Закрытие курсора.
cursor.close()

# Закрытие соединения с бд.
connection.close()
