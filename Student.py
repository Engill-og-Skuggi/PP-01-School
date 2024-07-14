from Human import Human
from typing import Optional
from Class import Class


class Student(Human):
    """Класс "школьник", являющийся подклассом Human и расширяющий его параметры атрибутом class_assignment (присвоение школьного класса) и методами set_class и get_class"""
    _class_assignment: Optional["Class"]

    def __init__(self, last_name, name, surname, class_assignment=None, id=None):
        super().__init__(last_name, name, surname, id)
        super()._verify_class(class_assignment)

        self._class_assignment = class_assignment
        if self._class_assignment:
            self._class_assignment.add({self})

    def set_class(self, new_class_assignment):
        """Метод сеттер для указания присвоения класса школьнику"""
        super()._verify_class(new_class_assignment)
        if self._class_assignment == new_class_assignment:
            print(f'Ученик {self} уже учится в классе {new_class_assignment}')
        else:
            self._class_assignment = new_class_assignment
            if self._class_assignment:
                self._class_assignment.add({self})
                print(f'Ученик {self} перешел в класс {new_class_assignment}')

    def get_class(self):
        """Метод геттер для получения значения класса школьника"""
        return self._class_assignment
