from Human import Human
from Subject import Subject
from typing import Set, Optional
from Class import Class
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
        super()._verify_class(homeroom_class)

        self._subjects = subjects
        self._homeroom_class = homeroom_class
        if self._homeroom_class:
            self._homeroom_class._homeroom_teacher = self

    def set_class(self, new_class_assignment):
        """Метод сеттер для указания присвоения класса учителю"""
        super()._verify_class(new_class_assignment)
        if self._homeroom_class == new_class_assignment:
            print(f'Учитель {self} уже является классным руководителем класса {new_class_assignment}')
        else:
            self._homeroom_class = new_class_assignment
            if self._homeroom_class:
                self._homeroom_class._homeroom_teacher = self
                print(f'Учитель {self} стал классным руководителем класса {new_class_assignment}')

    def get_class(self):
        """Метод геттер для получения значения класса школьника"""
        return self._homeroom_class

    @staticmethod
    def __verify_subject(subj_container):
        """Метод верифицирует, является ли переданное значение экземпляром или наследником класса Subject"""
        pass
        # if isinstance(subj_container, Iterable):
        #     for subj in subj_container:
        #         if not isinstance(subj, Subject):
        #             raise TypeError("В качестве предмета можно назначить только объект типа Subject")
        # else:
        #     if not isinstance(subj_container, Subject):
        #         raise TypeError("В качестве предмета можно назначить только объект типа Subject")
