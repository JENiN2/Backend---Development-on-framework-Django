def file_name(file):
    file_n = ''
    for i in file[::-1]:
        if i == '\\' or i == '/':
            break
        else:
            file_n += i
    return file_n[::-1]


print('Здравствуйте! Это программа "FileManager"\nСправка: \nРежим работы с файлом может быть: '
      'r - чтение, w - создание и запись, a - добавление.\nДля выхода из режима введите "q", '
      'для завершения программы "quit".')

while True:
    path = input('Введите путь: ')
    if path == 'quit':
        break
    mode = input('Введите режим (r, w, a): ')
    if mode == 'quit':
        break

    name = file_name(path)

    try:
        file = open(path, mode)
    except FileNotFoundError:
        print('Файл не найден. Возможно вы ввели неправильный'
              ' путь/название. Чтобы создать новый файл выберите режим w.')
        continue
    except ValueError:
        print('Режим работы с файлом может быть: r - чтение, w - создание и запись, a - добавление.')
        continue

    if mode == 'r':
        try:
            print(f'------------{name}---чтение файла---\n{file.read()}\n------------{name}---конец файла---')
        except UnicodeDecodeError as err:
            print(err)
        file.close()

    elif mode == 'w':
        count = 0
        print(f'------------{name}---заполнение файла---')
        while True:
            s = input(f'стр. {count}: ')
            if s != 'q':
                file.write(s + '\n')
                count += 1
            else:
                file.close()
                break
        print(f'------------{name}---конец файла---')

    elif mode == 'a':
        count = 0
        file_read = open(path, 'r')
        print(f'------------{name}---чтение файла---')

        for i in file_read:
            print(i, end='')
            count += 1
        print(f'------------{name}---конец файла---\n------------{name}---дозаполнение файла---')

        while True:
            s = input(f'стр. {count}: ')
            if s != 'q':
                file.write(s + '\n')
                count += 1
            else:
                file.close()
                file_read.close()
                break
        print(f'------------{name}---конец файла---')
