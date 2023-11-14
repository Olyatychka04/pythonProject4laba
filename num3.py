class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Начало выполнения отрисовки ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Кульминация отрисовки карандашом")

class Handle(Stationery):
    def draw(self):
        print("Завершение отрисовки маркером")

st = Stationery("Общая канцелярская принадлежность")
st.draw()
p = Pen("Ручка")
p.draw()

pn = Pencil("Карандаш")
pn.draw()

h = Handle("Маркер")
h.draw()
