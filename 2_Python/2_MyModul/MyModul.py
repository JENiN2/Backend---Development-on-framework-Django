def square(a):
    """
    Вычисляет  квадрата.
    :param a: Сторона квадрата
    :return: Int, Float or None
    """
    if type(a) == int or type(a) == float:
        return a ** 2
    else:
        print('Вы ввели не число.')


def rectangle(a, b):
    """
    Вычисляет площадь прямоугольника.

    :param a: Сторона прямоугольника
    :param b: Сторона прямоугольника
    :return: Int, Float or None
    """
    if type(a) == int or type(a) == float and type(b) == int or type(b) == float:
        return a * b
    else:
        print('Вы ввели не число.')


def circle(r):
    """
    Вычисляет площадь круга.

    :param r: Радиус круга
    :return: Float or None
    """

    if type(r) == int or type(r) == float:
        return 3.14*(r**2)
    else:
        print('Вы ввели не число.')


def trapezoid(m, h):
    """
    Вычисляет площадь трапеции.

    :param m: Средняя линия
    :param h: Высота
    :return: Int, Float or None
    """
    if type(m) == int or type(m) == float and type(h) == int or type(h) == float:
        return m * h
    else:
        print('Вы ввели не число.')


def rhomb(h, a):
    """
    Вычисляет площадь ромба.

    :param h: Высота
    :param a: Основание
    :return: Int, Float or None
    """
    if type(h) == int or type(h) == float and type(a) == int or type(a) == float:
        return a * h
    else:
        print('Вы ввели не число.')


def cube(a):
    """
    Вычисляет объем куба.

    :param a: Сторона куба
    :return: Int, Float or None
    """
    try:
        return a ** 3
    except TypeError:
        print('Вы ввели не число.')


def pyramid(s, h):
    """
    Вычисляет объем пирамиды.

    :param s: Площадь основания
    :param h: Высота
    :return: Float or None
    """
    try:
        return 1/3*s*h
    except TypeError:
        print('Вы ввели не число.')


def cylinder(r, h):
    """
    Вычисляет объем цилиндра.
    :param r: Радиус цилиндра
    :param h: Высота цилиндра
    :return: Int, Float or None
    """
    try:
        return 3.14*(r**2)*h
    except TypeError:
        print('Вы ввели не число.')


def cone(r, h):
    """
    Вычисляет объем конуса.
    :param r: Радиус основания конуса
    :param h: Высота конуса
    :return: Float or None
    """
    try:
        return 1/3*3.14*(r**2)*h
    except TypeError:
        print('Вы ввели не число.')


if __name__ == '__main__':
    print(square(2.2))
    print(rectangle('e', '2'))
    print(circle(3))
    print(trapezoid(4, 2))
    print(rhomb('э', 2))
    print(rhomb(2, 2))
    print(cube('2'))
    print(cube(3.1))
    print(pyramid('10', 3))
    print(pyramid(10, 3))
    print(cylinder('5', 10))
    print(cylinder(3, 4))
    print(cone('2', 4))
    print(cone(2, 4))
