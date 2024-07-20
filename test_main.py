import unittest
from Human import Human
from Class import Class
from Subject import Subject
from Student import Student
from Teacher import Teacher


class TestSchool(unittest.TestCase):
    """Тестирование приложения Школа"""

    def test_teacher_creation(self):

        teacher_1 = Teacher("Ivanova", "Maria", "Ivanovna", Subject.MATH)   #Один предмет
        self.assertEqual(teacher_1._subjects, Subject.MATH)

        teacher_2 = Teacher("Ivanova", "Galina", "Ivanovna", [Subject.BIOLOGY, Subject.MATH])   #Список предметов
        self.assertEqual(teacher_2._subjects, [Subject.BIOLOGY, Subject.MATH])

        teacher_3 = Teacher("Ivanova", "Tatiana", "Ivanovna", Subject.MATH, id=99)  #Ручное задание ID
        self.assertEqual(teacher_3._get_id(), 99)


    def test_class_creation(self):
        teacher_5 = Teacher("Sidorova", "Maria", "Ivanovna", Subject.MATH)
        correct_class_names = [(1, "A"), (5, "z"), (11, "F")]
        incorrect_class_names = [(0, "A"), (12, "z"), (1, "Ff"), ("1", "Ю")]
        for class_name in correct_class_names:
            class_1 = Class(class_name[0], class_name[1], teacher_5)
            self.assertEqual(class_1._grade, class_name[0])
            self.assertEqual(class_1._letter, str(class_name[1]).upper())
        for class_name in incorrect_class_names:
            with self.assertRaises(TypeError):
                class_1 = Class(class_name[0], class_name[1], teacher_5)
            self.assertNotEqual(class_1._grade, class_name[0])
            self.assertNotEqual(class_1._letter, str(class_name[1]).upper())

    def test_student_creation(self):
        student_1 = Student("Vasilenko", "Artem", "Mikhailovich", id=100)
        self.assertEqual(student_1._get_id(), 100)
        with self.assertRaises(Exception):
            student_2 = Student("Vasilenko", "Andrey", "Mikhailovich", id=100)

    def test_data_integrity(self):
        t1 = Teacher("Ivanova", "Maria", "Ivanovna", Subject.MATH)
        t2 = Teacher("Ivanova", "Maria", "Ivanovna", Subject.MATH)
        s1 = Student("Vasilenko", "Denis", "Mikhailovich")
        s2 = Student("Vasilenko", "Artem", "Mikhailovich")
        students = [s1, s2]
        cl1 = Class(11, "B", t1, students)
        self.assertEqual(cl1._homeroom_teacher, t1)
        self.assertEqual(t1.classroom, cl1)
        for student in students:
            self.assertTrue(student in cl1._students)
            self.assertEqual(student.classroom, cl1)

        cl1.remove(s1)
        self.assertTrue(s1 not in cl1._students)
        self.assertEqual(s1.classroom, None)

        cl1.add(s1)
        self.assertTrue(s1 in cl1._students)
        self.assertEqual(s1.classroom, cl1)

if __name__ == "__main__":
    unittest.main()


