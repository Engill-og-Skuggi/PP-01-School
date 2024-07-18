from Human import Human
from typing import Optional
# from Class import Class


class Student(Human):
    """Класс "школьник", являющийся подклассом Human и расширяющий его параметры атрибутом class_assignment
     (присвоение школьного класса) а также геттером и сеттером по property 'classroom'"""
    _class_assignment: Optional["Class"]

    def __init__(self, last_name, name, surname, class_assignment=None, id=None):
        super().__init__(last_name, name, surname, id)

        if not hasattr(self, "_class_assignments"):
            self._class_assignment = None
        self.classroom = class_assignment
        if self._class_assignment:
            self._class_assignment.add({self})

    @property
    def classroom(self):
        """Метод геттер для получения значения класса школьника"""
        return self._class_assignment

    @classroom.setter
    def classroom(self, new_class_assignment):
        """Метод сеттер для указания присвоения класса школьнику"""
        try:
            new_class_assignment is None or new_class_assignment.is_class()
        except TypeError("В качестве класса, в котором учится школьник, можно назначить только объект типа Class или None"):
            pass
        if self._class_assignment == new_class_assignment and self._class_assignment is not None and new_class_assignment is not None:
            print(f'Ученик {self} уже учится в классе {new_class_assignment}')
        else:
            if self._class_assignment:
                self._class_assignment.remove(self)
            self._class_assignment = new_class_assignment
            if self._class_assignment:
                self._class_assignment.add({self})
                print(f'Ученик {self} перешел в класс {new_class_assignment}')
