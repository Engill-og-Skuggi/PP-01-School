
class Human:
    """Класс 'Человек', являющийся суперклассом для подклассов Teacher и Student.
    Определяет основные общие атрибуты (ФИО, id) и методы для работы с объектом 'человек' """
    _name: str
    _last_name: str
    _surname: str
    __id: int
    __ids = set()

    def __init__(self, last_name, name, surname, id=None):
        self._last_name = str(last_name)
        self._name = str(name)
        self._surname = str(surname)
        if id is not None:
            if id in self.__ids:
                raise Exception("Переданный id уже существует!")
            self.__id = id
        elif self.__ids:
            # Создаем генератор, который будет возвращать первый незанятый id в диапазоне от 0 до "максимального уже существующего id"+1
            id_gen = (i for i in range(max(self.__ids)+2) if i not in self.__ids)
            self.__id = id_gen.__next__()
        else:
            self.__id = 0
        self.__ids.add(self.__id)

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        self.__verify_human(other)
        return self.__id == other.__id

    def __str__(self):
        return f"{self._last_name} {self._name} {self._surname}"

    def __repr__(self):
        return f"{self.__id} {self._last_name} {self._name} {self._surname}"

    def __lt__(self, other):
        self.__verify_human(other)
        return True if self._last_name+self._name+self._surname < other._last_name+other._name+other._surname else False

    def __le__(self, other):
        self.__verify_human(other)
        return True if self._last_name+self._name+self._surname <= other._last_name+other._name+other._surname else False

    def __bool__(self):
        return True if self.__id > -1 else False

    @staticmethod
    def __verify_human(other):
        """Метод верифицирует, является ли переданное значение экземпляром или наследником класса Human"""
        if not isinstance(other, Human):
            raise TypeError("Сравнение должно выполняться с объектом типа Human")

    def _get_id(self):
        """Геттер, возвращающий приватный атрибут ID (int)"""
        return self.__id
