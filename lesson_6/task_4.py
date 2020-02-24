class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        print(f'Машина поехала со скоростью {speed}')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на{direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        print(f'Текущая скорость: {self.speed}.')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        print(f'Текущая скорость: {self.speed}.')


class SportCar(Car):
    def accelerate(self, pace):
        self.speed += pace


class PoliceCar(Car):
    def pull_over(self, Car):
        Car.speed = 0


if __name__ == '__main__':
    pol = PoliceCar('Mazda', 'black')
    car = Car('BMW', 'white')
    car.go(120)
    pol.pull_over(car)
    car.show_speed()
