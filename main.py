"""
Необходимо создать систему регистрации экскурсионных поездок на разных видах транспорта с
возможностью узнать сколько тот или иной транспорт сможет проехать на выданном
количестве топлива.

Сейчас фирма располагает экскурсионными автомобилями и легкими самолетами.

Принято, что:

средний расход автомобилей 12л/100км
средний расход самолетов 200кг топлива на час полета
Предполагается — программа будет создана при помощи ООП.

Поскольку парк транспортных средств может (и будет!) расширяться, кажется целесообразным
использовать ООП.
"""


# TODO: сделать класс экскурсий
# TODO: написать ручные тесты


class Transport:
    def __init__(self, fuel):
        self.fuel = fuel
        self.trips = []

    def add_trip(self, trip):
        self.trips.append(trip)

    def sum_trips_distances(self):
        return sum(self.trips)

    def calc_remained_distance(self):
        raise NotImplementedError()


class CarTransport(Transport):
    FUEL_PER_100KM = 12

    def calc_remained_distance(self):
        distance = self.sum_trips_distances()
        fuel_wasted = distance / 100 * self.FUEL_PER_100KM
        return (self.fuel - fuel_wasted) / self.FUEL_PER_100KM * 100


class AirTransport(Transport):
    FUEL_PER_HOUR = 200

    def calc_remained_distance(self):
        distance = self.sum_trips_distances()
        fuel_wasted = distance * self.FUEL_PER_HOUR
        return (self.fuel - fuel_wasted) / self.FUEL_PER_HOUR


class ElectricityCarTransport(CarTransport):
    def __init__(self):
        super().__init__(100)


t1 = CarTransport(100)
t2 = AirTransport(50)
t3 = ElectricityCarTransport()

t1.add_trip(4)
t1.add_trip(40)
print(t1.sum_trips_distances())
print(t1.calc_remained_distance())

t2.add_trip(2)
print(t2.calc_remained_distance())
