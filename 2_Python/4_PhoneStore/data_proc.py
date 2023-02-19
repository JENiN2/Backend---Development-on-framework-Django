ph_lst = []
usrs_lst = []


def print_phones(phones):
    for i in phones:
        print(f'{i[0]} - {i[1]}, {i[2]}, {i[3]}, {i[4]}')


def print_users(users):
    for i in users:
        print(f'{i[0]} - {i[1]} {i[2]} {i[3]}, login - {i[4]}, password - {i[5]}, role - {i[6]}, exist - {i[7]}')


def users_id(users):
    for i in users:
        usrs_lst.append(i[0])
    return usrs_lst


def phones_id(phones):
    for i in phones:
        ph_lst.append(i[0])
    return ph_lst
