"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
 и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} едет!'.format(self.name))

    def stop(self):
        print('{} остановилась'.format(self.name))

    def turn(self, direction):
        print('{} повернула на {}'.format(self.name, direction))

    def show_speed(self):
        print('Текущая скорость', self.speed)

class TawnCar (Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Вы привысили лимит скорости!')

class SportCar (Car):
    pass

class WorkCar (Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Вы привысили лимит скорости!')

class PoliceCar (Car):
    pass


tawn_car = TawnCar(120, 'Night Blue', 'BMW', False)
sport_car = SportCar(240, 'Grey', 'McLaren', False)
work_car = WorkCar(40, 'Green', 'ZiL', False)
police_car = PoliceCar(160, 'White', 'Ford', True)

tawn_car.show_speed()
tawn_car.stop()
tawn_car.turn('право')
sport_car.show_speed()
sport_car.go()
work_car.show_speed()
police_car.show_speed()



