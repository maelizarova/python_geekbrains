import time

class TrafficLight:
    
    def __init__(self):
        self.__color = None

    def running(self):
        start = time.time()
        print('Загорелся красный.')
        self.__color = 'red'
        while time.time() - start < 7:
            pass
        start = time.time()
        print('Загорелся желтый.')
        self.__color = 'yellow'
        while time.time() - start < 2:
            pass
        start = time.time()
        print('Загорелся зеленый.')
        self.__color = 'green'
        while time.time() - start < 5:
            pass
        print('Светофор выключился.')
        self.__color = None


if __name__ == '__main__':
    light = TrafficLight()
    light.running()
