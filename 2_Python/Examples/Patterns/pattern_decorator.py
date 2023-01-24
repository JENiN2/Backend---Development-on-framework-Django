class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f'Привет, я {self.name}, мне {self.age} лет.')


class Axe:
    def __init__(self, person):
        self.person = person

    def work(self):
        print(f'Рублю деревья и имя мне {self.person.name}')

    def __getattr__(self, item):
        return getattr(self.person, item)


john = Person('John', 29)
john.say()

axeMan_john = Axe(john)
axeMan_john.work()
axeMan_john.say()
