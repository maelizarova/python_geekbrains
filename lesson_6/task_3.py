class Worker():
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._position = None
        self._income = {'wage': None, 'bonus': None}
    def set_income(self, wage, bonus):
        self._income = {'wage': wage, 'bonus': bonus}

    def set_position(self, position):
        self._position = position


class Position(Worker):
    def get_full_name(self):
        return self._name, self._surname

    def get_total_income(self):
        return self._income


if __name__ == '__main__':
    pos_1 = Position('Иван', 'Иванов')
    pos_1.set_position('менеджер')
    pos_1.set_income(40000, 3000)
    print(pos_1.get_full_name())
    print(pos_1.get_total_income())
