class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f'Hello, my name is {self.name} and i"m {self.age} year old.')


ivan = Person('Ivan', 28)
ivan.say()


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def teach(self):
        print(f'Я сейчас учусь в {self.university}')

    def say(self):
        print(f'Надо побыстрее сделать лабораторную из {self.university}')


oleg = Student('Олег', 20, 'РЭУ')
oleg.say()
oleg.teach()


class Employee(Person):
    def work(self):
        print(f'Я сейчас работаю, {self.name}.')

    def say(self):
        print(f'Я хочу отдохнуть, я {self.name}, мне {self.age}.')


john = Employee('Джон', 38)
john.work()
john.say()


class WorkingStudent(Student, Employee):
    pass


anna = WorkingStudent('Анна', 22, 'РЭУ')

anna.say()
anna.teach()
anna.work()
