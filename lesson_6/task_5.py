class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Пишем ручкой.')


class Pencil(Stationary):
    def draw(self):
        print('Пишем карандашом.')


class Handle(Stationary):
    def draw(self):
        print('Пишем маркером.')


if __name__ == '__main__':
    stat = Stationary('Кисть')
    stat.draw()
    pen = Pen('Ручка')
    pen.draw()
    pencil = Pencil('Карандаш')
    pencil.draw()
    handle = Handle('Маркер')
    handle.draw()