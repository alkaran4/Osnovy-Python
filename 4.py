class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехал')

    def stop(self):
        print(f'{self.color} {self.name} остановился')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернул {direction}')

    def show_speed(self, real_speed):
        print(f'текущая скорость авто {real_speed}')


class TownCar(Car):

    def town_speed(self):
        if self.speed < 200:
            print(f'{self.name} - городской автомобиль')
        else:
            print(f'{self.name} - не для города')

    def show_speed(self, real_speed):
        if real_speed > 60:
            print("Скорость превышена")

class SportCar(Car):

    def sport_speed(self):
        if self.speed > 200:
            print(f'{self.name} - спортивный автообиль')
        else:
            print(f'{self.name} будет отставать в соревнованиях')

class WorkCar(Car):

    def __init__(self, name, speed, color, length):
        super().__init__(name, speed, color)
        self.length = length

    def work_car(self):
        if self.length < 5:
            print(f'Автомобиль {self.name} не подходит для работы, требуется авто большего размера')
        else:
            print(f'Автомобиль {self.name} отлично подходит для работы')

    def show_speed(self, real_speed):
        if real_speed > 40:
            print('Скорость превышена')

class PoliceCar(Car):

    def __init__(self, name, speed, color, is_police = False):
        super().__init__(name, speed, color)
        self.is_police = is_police

    def police(self):
        if self.is_police:
            print(f"{self.name} - полицейский автомобиль")





Audi = Car("Audi", 250, "Черный")
Ford = WorkCar("Ford", 150, "Белый", 6)
Chevrolet = PoliceCar('Chevrolet', 220, 'бело-синий', is_police=True)


Audi.go()
Audi.stop()
Audi.turn('налево')

Ford.work_car()
Chevrolet.police()

Chevrolet.show_speed(150)

Ford.show_speed(35)

