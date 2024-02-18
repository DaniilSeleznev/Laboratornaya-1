import doctest


class Card:
    def __init__(self, limit: int, balance: (int, float)):
        """
        Создание и подготовка к работе объекта "Кредитная карта"

        :param limit: Лимит карты
        :param balance: Текущий баланс карты

        Примеры:
        >>> card = Card(10000, 3000)  # инициализация экземпляра класса
        """
        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть типа int или float")
        if not isinstance(limit, int):
            raise TypeError("Лимит должен быть типа int")
        if balance < 0 or balance > limit:
            raise ValueError("Баланс не должен быть меньше нуля или больше лимита")
        self.balance = balance
        self.limit = limit

    def add_money(self, money: (int, float)) -> None:
        """
        Добавление денег на счет.
        :param money: Количество добавляемых средств

        :raise ValueError: Если количество добавляемых средств выходит за пределы лимита, то вызываем ошибку

        Примеры:
        >>> card = Card(10000, 3000)
        >>> card.add_money(5000)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Количество денег должен быть типа float или int")
        if money <= 0:
            raise ValueError("Количество денег должно быть положительным")
        self.balance += money

    def remove_money(self, money: (int, float)) -> None:
        """
        Снятие денег со счета.
        :param money: Количество снимаемых средств

        :raise ValueError: Если количество снимаемых средств выходит за пределы лимита, то вызываем ошибку

        Примеры:
        >>> card = Card(10000, 3000)
        >>> card.remove_money(2000)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Количество денег должен быть типа float или int")
        if money <= 0:
            raise ValueError("Количество денег должно быть положительным")
        self.balance -= money


if __name__ == "__main__":
    doctest.testmod()


class Spell:
    def __init__(self, mana: int, damage: int, recharge: bool):
        """
        Создание и подготовка к работе объекта "Способность"

        :param mana: Сколько маны требуется для использования
        :param damage: Сколько способность нанесет урона
        :param recharge: Находится ли способность на перезарядке

        Примеры:
        >>> spell = Spell(25, 50, True)  # инициализация экземпляра класса
        """
        if not isinstance(mana, int):
            raise TypeError("Урон должен быть типа int")
        if not isinstance(damage, int):
            raise TypeError("Мана должна быть типа int")
        if not isinstance(recharge, bool):
            raise TypeError("Перезарядка должна быть типа bool")
        self.mana = mana
        self.damage = damage
        self.recharge = recharge

    def level_up(self) -> None:
        """
        Повышение уровня способности.
        """
        self.mana += 50
        self.damage += 100
        self.recharge = True

    def recharge(self) -> None:
        """
        Перезарядка способности.
        """
        if self.recharge is True:
            raise ValueError("Способность уже перезаряжена")
        else:
            self.recharge = True

    def cast_spell(self) -> str:
        """
        Использование способности.
        """
        if self.recharge is False:
            raise ValueError("Способность не перезаряжена")
        else:
            return f'Способность нанесла"{self.damage}" урона и потратила "{self.mana}" маны'


if __name__ == "__main__":
    doctest.testmod()


class Machine:
    def __init__(self, current_speed: int, max_speed: int):
        """
        Создание и подготовка к работе объекта "Машина"

        :param current_speed: Текущая скорость машины
        :param max_speed: Максимальная скорость машины

        Примеры:
        >>> machine = Machine(500, 1000)  # инициализация экземпляра класса
        """
        if not isinstance(current_speed, int):
            raise TypeError("Тeкущая скорость должна быть типа int")
        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть типа int")
        if current_speed < 0 or current_speed > max_speed:
            raise ValueError("Текущая скорость должна быть в пределах нормы")
        self.current_speed = current_speed
        self.max_speed = max_speed

    def add_speed(self, speed: int) -> None:
        """
        Увеличение скорости.
        :param speed: Добавляемая скорость

        :raise ValueError: Если количество скорости выходит за пределы нормы, то вызываем ошибку

        Примеры:
        >>> machine = Machine(500, 1000)
        >>> machine.add_speed(400)
        """
        if not isinstance(speed, int):
            raise TypeError("Добавляемая скорость должна быть типа int")
        if speed <= 0:
            raise ValueError("Добавляемая скорость должна быть положительной")
        self.current_speed += speed

    def remove_speed(self, speed: int) -> None:
        """
        Снижение скорости.
        :param speed: Уменьшаемая скорость

        :raise ValueError: Если количество скорости выходит за пределы нормы, то вызываем ошибку

        Примеры:
        >>> machine = Machine(500, 1000)
        >>> machine.remove_speed(200)
        """
        if not isinstance(speed, int):
            raise TypeError("Убавляемая скорость должна быть типа int")
        if speed <= 0:
            raise ValueError("Убавляемая скорость должна быть положительной")
        self.current_speed -= speed

    def stop(self) -> str:
        """
        Аварийная остановка машины.
        """
        if self.current_speed == 0:
            ValueError("Машина уже остановлена")
        else:
            self.current_speed = 0
            return "Машина успешно остановлена"


if __name__ == "__main__":
    doctest.testmod()
