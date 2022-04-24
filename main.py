from random import randint


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал'

    def show_speed(self):
        return f'Скорость {self.speed}'

    def stop(self):
        return f'Автомобиль {self.name} остановился!'

    def turn(self):
        return f'Автомобиль {self.name} сделал маневр.'


class TownCar(Car):

    def show_speed(self):
        print(f'Скорость {self.speed}')
        if self.speed > 60:
            speeding = self.speed - 60
            return f'Скорость превышена на {speeding}км/ч снизте скорость!'
        else:
            return f'Едем дальше!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость {self.speed}')
        if self.speed > 40:
            speeding = self.speed - 40
            return f'Скорость превышена на {speeding}км/ч снизте скорость!'
        else:
            return f'Едем дальше!'



class PoliceCar(Car):
    pass


speed_car = randint(10, 110)
car_town = TownCar(speed_car, 'Yelow', 'Vaz')

speed_car_2 = randint(10, 110)
car_work = WorkCar(speed_car_2, 'White', 'Haval')

print(car_town.go())
print(car_town.show_speed())
print(car_town.turn())
print(car_town.stop())
print(car_work.go())
print(car_work.show_speed())
