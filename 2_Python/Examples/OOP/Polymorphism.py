class Transport:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def start_engine(self):
        print('Start engine')

    def stop_engine(self):
        print('Stop engine')

    def info(self):
        print(f'Name: {self.name}.')
        print(f'Mass: {self.mass}.')
        print()


class Car(Transport):
    pass


class Truck(Transport):
    pass


class Motocycle(Transport):
    pass


class Bus(Transport):
    pass


car_bmw = Car('BMW', 2500)
truck_man = Truck('MAN', 4200)
moto_nissan = Motocycle('Nissan', 800)
bus_ikarus = Bus('Ikarus', 3700)


class Service_without_poly:
    def TO_car(self, car: Car):
        print('Проводится проверка')
        car.start_engine()
        car.stop_engine()
        car.info()
        print('Проверка завершена')
        print()

    def TO_truck(self, truck: Truck):
        print('Проводится проверка')
        truck.start_engine()
        truck.stop_engine()
        truck.info()
        print('Проверка завершена')
        print()

    def TO_moto(self, moto: Motocycle):
        print('Проводится проверка')
        moto.start_engine()
        moto.stop_engine()
        moto.info()
        print('Проверка завершена')
        print()

    def TO_bus(self, bus: Bus):
        print('Проводится проверка')
        bus.start_engine()
        bus.stop_engine()
        bus.info()
        print('Проверка завершена')
        print()


autoService_Car = Service_without_poly()
autoService_Car.TO_car(car_bmw)
autoService_Car.TO_truck(truck_man)
autoService_Car.TO_moto(moto_nissan)
# autoService_Car.TO_bus()


class Service_poly:
    def TO(self, transport: Transport):
        print('Проводится проверка')
        transport.start_engine()
        transport.stop_engine()
        transport.info()
        print('Проверка завершена')
        print()


autoService = Service_poly()
autoService.TO(car_bmw)
autoService.TO(truck_man)
autoService.TO(moto_nissan)
autoService.TO(bus_ikarus)

