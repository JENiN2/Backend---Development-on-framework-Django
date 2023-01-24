from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
        print('AAAAAA')

    @abstractmethod  # Аннотация
    def info(self):
        pass


class Capybara(Animal):
    def info(self):
        print('Капибара')
        print(f'Имя: {self.name}.')
        print(f'Возраст: {self.age}.')


henry = Capybara('Генри', 3)
henry.info()
henry.voice()


