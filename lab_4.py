class Vehicle:
    """
    Базовый класс "Транспортное средство"
    """

    def __init__(self, brand: str, fuel_type: str):
        """
        Конструктор класса "Транспортное средство"

        :param brand: Марка транспортного средства
        :param fuel_type: Тип топлива
        """
        self.brand = brand
        self.fuel_type = fuel_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта

        :return: Строковое представление объекта
        """
        return f"{self.brand} ({self.fuel_type})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для вывода в интерактивной оболочке Python

        :return: Строковое представление объекта
        """
        return f"{self.brand} ({self.fuel_type})"

    def move(self, speed: float) -> None:
        """
        Движение транспортного средства

        :param speed: Скорость движения
        """
        print(f"{self.brand} движется со скоростью {speed} км/ч")


class Car(Vehicle):
    """
    Дочерний класс "Легковой автомобиль"
    """

    def __init__(self, brand: str, fuel_type: str, num_seats: int):
        """
        Конструктор класса "Легковой автомобиль"

        :param brand: Марка автомобиля
        :param fuel_type: Тип топлива
        :param num_seats: Количество сидений
        """
        super().__init__(brand, fuel_type)
        self.num_seats = num_seats

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта

        :return: Строковое представление объекта
        """
        return f"Легковой автомобиль: {super().__str__()}, сидений: {self.num_seats}"

    def start_engine(self) -> None:
        """
        Запуск двигателя автомобиля
        """
        print(f"{self.brand}: Двигатель запущен")

    def open_trunk(self) -> None:
        """
        Открытие багажника автомобиля
        """
        print(f"{self.brand}: Багажник открыт")


class Truck(Vehicle):
    """
    Дочерний класс "Грузовой автомобиль"
    """

    def __init__(self, brand: str, fuel_type: str, max_load: int):
        """
        Конструктор класса "Грузовой автомобиль"

        :param brand: Марка автомобиля
        :param fuel_type: Тип топлива
        :param max_load: Максимальная грузоподъемность
        """
        super().__init__(brand, fuel_type)
        self.max_load = max_load

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта

        :return: Строковое представление объекта
        """
        return f"Грузовой автомобиль: {super().__str__()}, грузоподъемность: {self.max_load} кг"

    def start_engine(self) -> None:
        """
        Запуск двигателя автомобиля
        """
        print(f"{self.brand}: Двигатель запущен")

    def load_cargo(self, weight: int) -> None:
        """
        Погрузка груза

        :param weight: Вес груза
        """
        print(f"Грузовой автомобиль {self.brand}: Погружен груз весом {weight} кг")

    def unload_cargo(self, weight: int) -> None:
        """
        Разгрузка груза

        :param weight: Вес груза
        """
        print(f"Грузовой автомобиль {self.brand}: Разгружен груз весом {weight} кг")


if __name__ == '__main__':
    car = Car("Toyota", "бензин", 5)
    print(car)
    car.start_engine()
    car.move(100)

    print()

    truck = Truck("Volvo", "дизель", 1500)
    print(truck)
    truck.load_cargo(1000)
    truck.move(60)
