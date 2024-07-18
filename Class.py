from typing import Set, Optional
from string import ascii_uppercase
from collections.abc import Iterable
import csv
from Human import Human
from Teacher import Teacher
from Student import Student
from Subject import Subject

class Class(set):
    """Класс "Школьный класс", являющийся подклассом стандартного класса set, расширяющий его параметры атрибутами
    grade (номер класса), letter (буква класса), homeroom_teacher (учитель - классный руководитель), students (школьники)
    а также переопределяющий часть дандер-методов и методы add и remove"""
    _grade: int
    _letter: str
    _students: Optional[Set["Student"]]
    _homeroom_teacher: "Teacher"


    def __init__(self, grade, letter, homeroom_teacher, students=None):

        self.__verify_grade(grade)
        self.__verify_letter(letter)
        self.__verify_teacher(homeroom_teacher)
        if students is None:
            students = set()
        else:
            if students:
                for student in set(students):
                    self.__verify_student(student)

        self._grade = grade
        self._letter = str(letter).upper()
        self._homeroom_teacher = homeroom_teacher
        if self._homeroom_teacher:
            self._homeroom_teacher._homeroom_class = self

        self._students = set(students)
        if self._students:
            for student in self._students:
                student.classroom = self

    def __getitem__(self, name):
        result = set(student for student in self._students if str(student).upper().find(str(name).upper()) > -1)
        if len(result) == 0:
            return None
        return result

    def __len__(self):
        return len(self._students)

    def __iter__(self):
        self.__temp_students_set = self._students.copy()
        self.__temp_students_set = sorted(self.__temp_students_set, reverse=True)
        return self

    def __next__(self):
        if len(self.__temp_students_set) > 0:
            return self.__temp_students_set.pop()
        else:
            del self.__temp_students_set
            raise StopIteration

    def __repr__(self):
        return str(self._grade)+self._letter

    def __str__(self):
        return str(self._grade)+self._letter

    def __eq__(self, other):
        if self is None or other is None:
            return False
        return (str(self._grade)+self._letter) == (str(other._grade)+other._letter)

    def __bool__(self):
        return True if self._grade else False

    @staticmethod
    def __verify_grade(grade):
        """Метод верифицирует, является ли переданное значение номера класса - валидным значением (число от 1 до 11 включительно)"""
        if not(type(grade) == int and 0 < grade < 12):
            raise TypeError("В качестве параметра grade необходимо указать целое число от 1 (включительно) до 11 (включительно)")

    @staticmethod
    def __verify_letter(letter):
        """Метод верифицирует, является ли переданное значение буквы класса - валидным значением (одна латинская буква)"""
        if not(str(letter).upper() in ascii_uppercase and len(letter) == 1):
            raise TypeError("В качестве параметра letter необходимо указать одну букву латинского алфавита")

    @staticmethod
    def __verify_teacher(other):
        """Метод верифицирует, является ли переданное значение экземпляром или наследником класса Teacher"""
        if not isinstance(other, Teacher):
            raise TypeError("В качестве учителя можно назначить только объект типа Teacher")

    @staticmethod
    def __verify_student(other):
        """Метод верифицирует, является ли переданное значение экземпляром или наследником класса Student"""
        if not isinstance(other, Student):
            raise TypeError("В качестве школьника можно назначить только объект типа Student")

    def add(self, container):
        """Переопределенный метод add, добавляющий школьника(-ов) в переменную _students"""
        if container is None and self._students is None:
            self._students = set()
        elif container is None:
            pass
        elif isinstance(container, Iterable):
            for student in container:
                self.__verify_student(student)
                self._students = self._students.union(container)
                student._class_assignment = self
        else:
            self.__verify_student(container)
            self._students = self._students.union({container})
            container._class_assignment = self
        # for student in self._students:
        #     student._class_assignment = self

    def remove(self, container):
        """Переопределенный метод remove, удаляющий школьника(-ов) из переменной _students"""
        if container is None:
            self._students = set()
        elif isinstance(container, Iterable):
            for student in container:
                self.__verify_student(student)
                self._students = self._students.difference(container)
                student._class_assignment = None
        else:
            self.__verify_student(container)
            self._students = self._students.difference({container})
            container._class_assignment = None

    @staticmethod
    def is_class():
        return True

    def write_csv(self, class_file_name=""):
        """Метод для выгрузки всей информации о классе в csv"""
        if not class_file_name:
            class_file_name = f"Class '{self._grade}{self._letter}'.csv"
        with open(class_file_name, 'w') as f:
            writer = csv.writer(f, delimiter=';', lineterminator='\r')
            writer.writerow(["ID", "Last Name", "Name", "Surname", "IsTeacher"])
            writer.writerow([self._homeroom_teacher._get_id(), self._homeroom_teacher._last_name, self._homeroom_teacher._name, self._homeroom_teacher._surname, "Y"])
            for st in self._students:
                writer.writerow([st._get_id(), st._last_name, st._name, st._surname, ""])

        with open("_subjects.csv", 'w') as f:
            writer = csv.writer(f, delimiter=";", lineterminator='\r')
            writer.writerow(["Subject"])
            if isinstance(self._homeroom_teacher._subjects, Iterable):
                for subj in self._homeroom_teacher._subjects:
                    writer.writerow([subj.name])
            else:
                 writer.writerow([self._homeroom_teacher._subjects])

        with open("_class_name.csv", 'w') as f:
            writer = csv.writer(f, delimiter=";", lineterminator='\r')
            writer.writerow(["Grade", "Letter"])
            writer.writerow([self._grade, self._letter])

    @staticmethod
    def read_csv(class_file_name):
        """Метод для загрузки все информации о классе из csv. Формат возвращаемого значения - кортеж (класс, учитель, [список школьников]"""
        with open("_subjects.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader)
            subjects = []
            for subject in reader:
                subjects.append(Subject[subject[0]])

        with open("_class_name.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader)
            temp = next(reader)
            grade, letter = temp[0].split(";")

        with open(class_file_name, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            students = []
            for person in reader:
                pers_id, last_name, name, surname, is_teacher = person[0].split(";")
                if is_teacher:
                    teacher = Teacher(id=int(pers_id), last_name=last_name, name=name, surname=surname, subjects=subjects)
                else:
                    students.append(Student(id=int(pers_id), last_name=last_name, name=name, surname=surname))

        class_obj = Class(grade=int(grade), letter=letter, homeroom_teacher=teacher, students=students)
        return class_obj, teacher, students


