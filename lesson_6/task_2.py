class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def asphalt(self, mass, thickness):
        return self.__length * self.__width * mass * thickness


if __name__ == '__main__':
    road = Road(20, 5000)
    print(road.asphalt(25, 5))