from Human import Human
from Student import Student
from Teacher import Teacher
from Subject import Subject
from Class import Class

"""ТЕСТИРОВАНИЕ"""

"""Инициализация учителя"""
teacher_1 = Teacher("Ivanova", "Maria", "Ivanovna", Subject.MATH)   #Один предмет
teacher_2 = Teacher("Ivanova", "Galina", "Ivanovna", [Subject.BIOLOGY, Subject.MATH])   #Список предметов
teacher_3 = Teacher("Ivanova", "Tatiana", "Ivanovna", Subject.MATH, id=99)  #Ручное задание ID
teacher_4 = Teacher("Ivanova", "Olga", "Ivanovna", Subject.MATH)  #Новый ID=2, а не 100
print("Инициализация учителя")
print(teacher_1.__dict__)
print(teacher_2.__dict__)
print(teacher_3.__dict__)
print(teacher_4.__dict__)
print()
# teacher_error_1 = Teacher("Ivanova", "Galina", "Ivanovna", "Subject.MATH")  #Ошибка: В качестве предмета можно назначить только объект типа Subject
# teacher_error_2 = Teacher("Ivanova", "Galina", "Ivanovna", Subject.MATH, id=1)    #Ошибка: Переданный id уже существует!

"""Инициализация класса"""
class_1 = Class(11, "A", teacher_1)
print("Инициализация класса с указанием учителя")
print(class_1.__dict__)     #У класса значение teacher_1 прописывается в атрибут _homeroom_teacher
print(teacher_1.__dict__)   #У учителя значение class_1 прописывается в атрибут _homeroom_class
print()
# class_error_1 = Class(11, "A", "teacher_1")   #Ошибка: В качестве учителя можно назначить только объект типа Teacher
# class_error_2 = Class(20, "A", teacher_1)   #Ошибка: В качестве параметра grade необходимо указать целое число от 1 (включительно) до 11 (включительно)
# class_error_3 = Class(11, "Ц", teacher_1)   #Ошибка: В качестве параметра letter необходимо указать одну букву латинского алфавита

"""Инициализация школьника"""
print("Инициализация школьника")
student_1 = Student("Vasilenko", "Denis", "Mikhailovich", class_1)  #Уведомление о поступлении в класс (можно отключить)
student_2 = Student("Vasilenko", "Artem", "Mikhailovich")
print(student_1.__dict__)
print(student_2.__dict__)
print(class_1.__dict__) #У класса значение student_1 прописывается в атрибут _students
print()
# student_error_1 = Student("Vasilenko", "Denis", "Mikhailovich", 1) #Ошибка: TypeError("В качестве класса, в котором учится школьник, можно назначить только объект типа Class или None")


"""Отображение в printe"""
print("Отображение в print\'e")
print(f"class_1: {class_1}")
print(f"teacher_1: {teacher_1}")
print(f"student_1: {student_1}")
print()

"""Инициализация класса со школьниками"""
print("Инициализация класса со школьниками")
class_2 = Class(11, "B", teacher_2, [student_1, student_2])
print(class_2.__dict__)
print(student_1.__dict__)
print(student_2.__dict__)
print()
# class_error_3 = Class(11, "C", teacher_2, [student_1, "student"])   #TypeError: В качестве школьника можно назначить только объект типа Student

"""Тестирование переприсвоения класса"""
print("Тестирование переприсвоения класса")

teacher_2.classroom = class_1
print(teacher_2.__dict__)
print(class_1.__dict__)   #_homeroom_teacher переопределился на teacher_2
print(class_2.__dict__)  #_homeroom_teacher переопределился на None

student_1.classroom = class_1
print(class_1.__dict__)   #в атрибуте _students поддерживаются консистентные данные
print(class_2.__dict__)  #в атрибуте _students поддерживаются консистентные данные

student_2.classroom = class_1
print(class_1.__dict__)   #в атрибуте _students поддерживаются консистентные данные
print(class_2.__dict__)  #в атрибуте _students поддерживаются консистентные данные
print()


print("Поиск школьников")
print(class_1["Vas"])
print(class_1["den"])
print(class_1["TEM"])
print()

print("Цикл по школьникам в алфавитном порядке")
for student in class_1:
    print(student)
print()

"""Методы add/remove"""
print("Методы add/remove")
class_1.remove(class_1["den"])
print(class_1.__dict__)
print(student_1.__dict__)
class_1.add(student_1)
print(class_1.__dict__)
print(student_1.__dict__)
print()

print("Булевы операции")
print(class_1 == class_2)
print(class_1 == class_1)
print(student_1 == student_1)
print(student_1 == student_2)
print(student_1 > student_2)
print()

"""Выгрузка в csv"""
class_1.write_csv()

"""Для выполнения кода ниже необходимо закомментировать весь код выше (кроме импортов)"""
# import_result = Class.read_csv("Class '11A'.csv")
# print(import_result[0].__dict__)
# print(import_result[1].__dict__)
# print(import_result[2])





