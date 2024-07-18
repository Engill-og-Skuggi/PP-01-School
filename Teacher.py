from Human import Human
from Subject import Subject
from typing import Set, Optional
from Human import Human
from collections.abc import Iterable


class Teacher(Human):
    """Класс "Учитель", являющийся подклассом Human и расширяющий его параметры атрибутами homeroom_class (присвоение школьного класса) и subjects (предметы учителя), а также
     методами set_class и get_class"""

    _homeroom_class: Optional["Class"]
    _subjects: Set["Subject"]

    def __init__(self, last_name, name, surname, subjects, homeroom_class=None, id=None):
        super().__init__(last_name, name, surname, id)
        self.__verify_subject(subjects)

        if not hasattr(self, "_homeroom_class"):
            self._homeroom_class = None
        self.classroom = homeroom_class

        self._subjects = subjects
        # self._homeroom_class = homeroom_class
        if self._homeroom_class:
            self._homeroom_class._homeroom_teacher = self

    @property
    def classroom(self):
        """Метод геттер для получения значения класса школьника"""
        return self._homeroom_class

    @classroom.setter
    def classroom(self, new_class_assignment):
        """Метод сеттер для указания присвоения класса учителю"""
        try:
            new_class_assignment is None or new_class_assignment.is_class()
        except TypeError("В качестве класса, в котором учится школьник, можно назначить только объект типа Class или None"):
            pass
        if self._homeroom_class == new_class_assignment and self._homeroom_class is not None and new_class_assignment is not None:
            print(f'Учитель {self} уже является классным руководителем класса {new_class_assignment}')
        else:
            if self._homeroom_class:
                self._homeroom_class._homeroom_teacher = None
            self._homeroom_class = new_class_assignment
            if self._homeroom_class:
                self._homeroom_class._homeroom_teacher = self
                print(f'Учитель {self} стал классным руководителем класса {new_class_assignment}')

    @staticmethod
    def __verify_subject(subj_container):
        """Метод верифицирует, является ли переданное значение экземпляром или наследником класса Subject"""
        if isinstance(subj_container, Iterable):
            for subj in subj_container:
                if not isinstance(subj, Subject):
                    raise TypeError("В качестве предмета можно назначить только объект типа Subject")
        else:
            if not isinstance(subj_container, Subject):
                raise TypeError("В качестве предмета можно назначить только объект типа Subject")

