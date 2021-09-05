class Stationery:
    def __init__(self, title):
        self.title = title

    def draw (self):
        print('Запуск отрисовки')


class Pen (Stationery):
    def draw(self):
        print('ручка рисует')

class Pencil (Stationery):
    def draw(self):
        print('карандаш рисует')

class Handle (Stationery):
    def draw(self):
        print('маркер рисует')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()