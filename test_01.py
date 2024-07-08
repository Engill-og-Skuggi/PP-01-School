from enum import Enum
from typing import Set
from string import ascii_uppercase
from typing import Optional

class Subject(Enum):
    MATH = 'Математика'
    RUSSIAN_LANG = 'Русcкий Язык'
    FOREAN_LANG = 'Английский Язык'
    PHISICS = "Физика"
    GEOGRAPHY = "География"
    BIOLOGY = "Биология"
    HISTORY = "История"
    CHEMISTRY = "Химия"

class Human:

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
        if not isinstance(other, Human):
            raise TypeError("Сравнение должно выполняться с объектом типа Human")

    @classmethod
    def _verify_class(cls, other):
        if not isinstance(other, Class) and other is not None:
            raise TypeError("В качестве класса, в котором учится школьник, можно назначить только объект типа Class или None")

class Student(Human):
    _class_assignment: Optional["Class"]

    def __init__(self, last_name, name, surname, class_assignment=None, id=None):
        super().__init__(last_name, name, surname, id)
        super()._verify_class(class_assignment)

        self._class_assignment = class_assignment
        if self._class_assignment:
            self._class_assignment.add({self})

    def set_class(self, new_class_assignment):
        super()._verify_class(new_class_assignment)
        if self._class_assignment == new_class_assignment:
            print(f'Ученик {self} уже учится в классе {new_class_assignment}')
        else:
            self._class_assignment = new_class_assignment
            if self._class_assignment:
                self._class_assignment.add({self})
                print(f'Ученик {self} перешел в класс {new_class_assignment}')

    def get_class(self):
        return self._class_assignment

class Teacher(Human):

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
        super()._verify_class(new_class_assignment)
        if self._homeroom_class == new_class_assignment:
            print(f'Учитель {self} уже является классным руководителем класса {new_class_assignment}')
        else:
            self._homeroom_class = new_class_assignment
            if self._homeroom_class:
                self._homeroom_class._homeroom_teacher = self
                print(f'Учитель {self} стал классным руководителем класса {new_class_assignment}')

    def get_class(self):
        return self._homeroom_class

    @staticmethod
    def __verify_subject(subj_container):
        for subj in subj_container:
            if not isinstance(subj, Subject):
                raise TypeError("В качестве класса, в котором учится школьник, можно назначить только объект типа Class или None")


class Class(set):

  # При вызове методов "листа" - работает с набором школьников

  # На основе этого создайте запись и чтения и записи объекта типа Сlass на диск. Предлагаемый путь - сделать два статических метода класса - Class.read_csv(filename) и Class.write_csv(filename).
  # Ваша задача - попробовать уместить информацию о группе детей и преподавателе внутри файла, чтобы можно было завершить сессию, начать её заного,
  #  и из файла восстановить класс! Изначально рекомендую вам попробовать записать только информацию о наборе школьников, без преподавателя, номера и буквы класса.
  # Далее можете попробовать добавить функционал с информацией о преподавателе.

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
                student._class_assignment = self

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
        return (str(self._grade)+self._letter) == (str(other._grade)+other._letter)

    def add(self, container):
        if container is None:
            container = set()
        else:
            if container:
                for student in set(container):
                    self.__verify_student(student)

        self._students = self._students.union(container)
        for student in self._students:
            student._class_assignment = self

    def __bool__(self):
        return True if self._grade else False

    @staticmethod
    def __verify_grade(grade):
        if not(type(grade) == int and 0 < grade < 12):
            raise TypeError("В качестве параметра grade необходимо указать целое число от 1 (включительно) до 11 (включительно)")

    @staticmethod
    def __verify_letter(letter):
        if not(str(letter).upper() in ascii_uppercase and len(letter) == 1):
            raise TypeError("В качестве параметра letter необходимо указать одну букву латинского алфавита")

    @staticmethod
    def __verify_teacher(other):
        if not isinstance(other, Teacher):
            raise TypeError("В качестве учителя можно назначить только объект типа Teacher")

    @staticmethod
    def __verify_student(other):
        if not isinstance(other, Student):
            raise TypeError("В качестве школьника можно назначить только объект типа Student")


teacher_1 = Teacher("Ivanova", "Maria", "Ivanovna", [Subject.MATH])
teacher_2 = Teacher("Ivanova", "Galina", "Ivanovna", [Subject.BIOLOGY])
student_1 = Student("Vasilenko", "Denis", "Mikhailovich")
student_2 = Student("Vasilenko", "Artem", "Mikhailovich")
class_1 = Class(11, "A", teacher_1)
class_2 = Class(11, "B", teacher_2)

teacher_1.set_class(class_2)
class_1.add({student_1, student_2})
student_2.set_class(class_1)

print(student_2.get_class())



