class Circle:
    def __init__(self, radius):
        self.set_radius(radius)
    def set_radius(self, radius):
            self.radius = radius
    def square(self):
        return 3.14 * self.radius * self.radius
    def length(self):
        return 2 * 3.14 * self.radius
while True:
    try:
        radius = float(input("Введите радиус круга: "))
        if radius <= 0:
            print("Ошибка, введите положительный радиус")
        else:
            c = Circle(radius)
            print("Радиус круга:", c.radius)
            print("Площадь круга:", c.square())
            print("Длина круга:", c.length())
            another = input("Хотите ввести радиус еще раз?(да/нет): ")
            if another.lower() != "да":
                break
    except ValueError:
        print("Ошибка, введите числовое значение радиуса.")
