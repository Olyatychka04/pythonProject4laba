class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": income["wage"], "bonus": income["bonus"]}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

def input_valid_name(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        else:
            print("Ошибка, введите корректное имя")

def input_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка, введите числовое значение.")

name = input_valid_name("Введите имя сотрудника: ")
surname = input_valid_name("Введите фамилию сотрудника: ")
position = input_valid_name("Введите должность сотрудника: ")
wage = input_valid_float("Введите оклад сотрудника: ")
bonus = input_valid_float("Введите премию сотрудника: ")
employee = Position(name, surname, position, {"wage": wage, "bonus": bonus})
print(f" ФИ сотрудника: {employee.get_full_name()}")
print(f" Доход сотрудника С премией: {employee.get_total_income()}")





